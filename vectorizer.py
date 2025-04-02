#!/usr/bin/env python3

import os
import json
import argparse
from typing import List, Dict, Any
from tqdm import tqdm
import chromadb
from sentence_transformers import SentenceTransformer
from datetime import datetime

# "dunzhang/stella_en_400M_v5"

class ChunkVectorizer:
    """从文本块生成嵌入向量并存储在ChromaDB向量数据库中。"""
    
    def __init__(
        self,
        input_file: str,
        db_directory: str,
        model_name: str,
        batch_size: int = 32
    ):
        """
        初始化向量化器
        Args:
            input_file: 包含文本块的输入JSONL文件路径
            db_directory: ChromaDB存储向量数据库的目录
            model_name: 要使用的sentence-transformer模型名称
            batch_size: 生成嵌入向量的批处理大小
        """
        self.input_file = input_file
        self.db_directory = db_directory
        collection_base_name = os.path.basename(input_file).replace('.jsonl', '')
        
        # 创建集合名称并限制为63个字符（数据库限制）
        # 提取模型名称的简短版本（例如，从完整路径中提取"all-MiniLM-L6-v2"）
        model_short_name = model_name.split('/')[-1] if '/' in model_name else model_name
        collection_name = f"{collection_base_name}_{model_short_name}"
        
        # 如果超过63个字符则截断
        if len(collection_name) > 63:
            collection_name = collection_name[:63]
        
        self.collection_name = collection_name
        print(f"集合名称: {self.collection_name} ({len(self.collection_name)} 个字符)")
        
        # 初始化ChromaDB客户端
        print(f"在 {db_directory} 初始化ChromaDB")
        self.client = chromadb.PersistentClient(path=db_directory)
        
        # 如果集合已存在则删除
        try:
            self.client.delete_collection(name=self.collection_name)
            print(f"已删除现有集合: {self.collection_name}")
        except Exception as e:
            print(f"没有现有集合可删除: {e}")
        
        # 使用sentence transformer创建嵌入函数
        self.embedding_function = CustomEmbeddingFunction(model_name)
        
        # 创建新集合
        self.collection = self.client.create_collection(
            name=self.collection_name,
            embedding_function=self.embedding_function,
            metadata={"hnsw:space": "cosine"}  # 使用余弦相似度进行语义搜索
        )
        print(f"已创建新集合: {self.collection_name}")
        
        # 将集合名称追加到artifacts/collections.txt
        collections_file = "artifacts/vector_stores/collections.txt"
        os.makedirs(os.path.dirname(collections_file), exist_ok=True)
        with open(collections_file, 'a+', encoding='utf-8') as f:
            f.seek(0)  # 移动到文件开头
            timestamp = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
            f.write(f"{self.collection_name} ({timestamp}) - 原始模型: {model_name}\n")
        self.batch_size = batch_size
        
        # 加载嵌入模型
        print(f"使用模型: {model_name}")
        self.model = SentenceTransformer(model_name)
        print(f"模型已加载: {model_name} (嵌入维度: {self.model.get_sentence_embedding_dimension()})")
        
    def load_chunks(self) -> List[Dict[str, Any]]:
        """
        从输入JSONL文件加载文本块
        Returns:
            文本块列表
        """
        chunks = []
        
        print(f"从 {self.input_file} 加载文本块")
        with open(self.input_file, 'r', encoding='utf-8') as f:
            for line in f:
                if line.strip():
                    chunk = json.loads(line)
                    chunks.append(chunk)
        
        print(f"已加载 {len(chunks)} 个文本块")
        return chunks
    
    def process_and_store_chunks(self, chunks: List[Dict[str, Any]]) -> None:
        """
        批量处理文本块并将它们存储在ChromaDB中
        Args:
            chunks: 要处理的文本块列表
        """
        # 提取ChromaDB所需的数据
        chunk_ids = [chunk['id'] for chunk in chunks]
        texts = [chunk['text'] for chunk in chunks]
        metadatas = [{'source': chunk['source']} for chunk in chunks]
        
        print(f"以 {self.batch_size} 为批次处理 {len(chunks)} 个文本块")
        
        # 分批处理和添加
        for i in tqdm(range(0, len(chunks), self.batch_size)):
            batch_ids = chunk_ids[i:i+self.batch_size]
            batch_texts = texts[i:i+self.batch_size]
            batch_metadatas = metadatas[i:i+self.batch_size]
            
            # 使用add方法时，ChromaDB会自动计算嵌入向量
            self.collection.add(
                ids=batch_ids,
                documents=batch_texts,
                metadatas=batch_metadatas
            )
        
        print(f"已成功将 {len(chunks)} 个文本块存储到ChromaDB")
        
        # 获取集合统计信息
        collection_count = self.collection.count()
        print(f"集合中的文档总数: {collection_count}")
        
    def run(self) -> None:
        """运行完整的向量化处理流程"""
        chunks = self.load_chunks()
        self.process_and_store_chunks(chunks)
        print(f"向量数据库已成功创建于: {os.path.abspath(self.db_directory)}")
        print("现在可以使用ChromaDB的查询API查询数据库。")


class CustomEmbeddingFunction:
    """使用sentence-transformers的ChromaDB自定义嵌入函数。"""
    
    def __init__(self, model_name: str = "sentence-transformers/all-MiniLM-L6-v2"):
        """
        使用特定模型初始化
        Args:
            model_name: 要使用的模型名称
        """
        self.model = SentenceTransformer(model_name)
        
    def __call__(self, input: List[str]) -> List[List[float]]:
        """
        为文本列表生成嵌入向量
        Args:
            input: 要嵌入的文本列表（参数名必须为'input'以符合ChromaDB要求）
        Returns:
            浮点数列表形式的嵌入向量列表
        """
        embeddings = self.model.encode(input)
        return embeddings.tolist()


if __name__ == "__main__":
    # 创建命令行参数解析器
    parser = argparse.ArgumentParser(description="从文本块生成嵌入向量并存储在ChromaDB中。")
    parser.add_argument("--input", "-i", help="包含文本块的输入JSONL文件")
    parser.add_argument("--db", "-d", default="artifacts/vector_stores/chroma_db",
                        help="ChromaDB存储向量数据库的目录（默认：artifacts/vector_stores/chroma_db）")
    parser.add_argument("--model", "-m", default="sentence-transformers/all-MiniLM-L6-v2", 
                        help="要使用的sentence-transformer模型名称（默认：sentence-transformers/all-MiniLM-L6-v2）")
    parser.add_argument("--batch-size", "-b", type=int, default=32,
                        help="生成嵌入向量的批处理大小（默认：32）")
    
    args = parser.parse_args()
    
    # 创建向量化器实例并运行
    vectorizer = ChunkVectorizer(
        input_file=args.input,
        db_directory=args.db,
        model_name=args.model,
        batch_size=args.batch_size
    )
    vectorizer.run()