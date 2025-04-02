import chromadb
from sentence_transformers import SentenceTransformer
import argparse
import os
from typing import List, Dict, Any
import json
import re

class GodotDocMCP:
    def __init__(self, collection_name: str, db_path: str = "artifacts/vector_stores/chroma_db"):
        """
        初始化 Godot 文档 MCP
        
        Args:
            collection_name: ChromaDB 集合名称
            db_path: ChromaDB 数据库路径
        """
        # 初始化向量数据库客户端
        self.client = chromadb.PersistentClient(path=db_path)
        
        # 从完整集合名称中提取基本名称
        self.collection_name = collection_name.split(" (")[0]
        
        try:
            # 尝试直接获取集合
            self.collection = self.client.get_collection(name=self.collection_name)
        except Exception as e:
            raise ValueError(f"无法获取集合 {self.collection_name}: {str(e)}")
        
        # 加载模型
        self.model = SentenceTransformer('sentence-transformers/all-MiniLM-L6-v2')
    
    def get_godot_context(self, query: str, n_results: int = 20) -> List[Dict[str, Any]]:
        """
        获取最新的 Godot 文档内容。由于 Godot 引擎发展迅速，预训练知识可能已经过时，
        此工具会根据查询检索最新的相关文档片段。当涉及 Godot 引擎相关问题时，
        包括 API 和类引用，即使您很确定，也应该调用此函数。如果检索到的内容与您的知识有冲突，
        应该以检索到的内容为准。
        
        Args:
            query: 与 Godot 引擎相关的关键词
            n_results: 返回结果数量
            
        Returns:
            包含相关文档/引用片段的列表
        """
        try:
            # 将查询转换为向量并搜索
            results = self.collection.query(
                query_embeddings=self.model.encode([query]).astype(float).tolist(),
                n_results=n_results
            )
            
            # 格式化结果
            formatted_results = []
            for i in range(len(results['ids'][0])):
                formatted_results.append({
                    'id': results['ids'][0][i],
                    'document': results['documents'][0][i],
                    'metadata': results['metadatas'][0][i],
                    'distance': results['distances'][0][i],
                    'relevance': 1 - results['distances'][0][i]
                })
            
            return formatted_results
        except Exception as e:
            return {"error": f"查询 ChromaDB 失败: {str(e)}"}

    def process_query(self, query: str) -> str:
        """处理查询并返回 JSON 格式的响应"""
        results = self.get_godot_context(query)
        return json.dumps(results, ensure_ascii=False, indent=2)

def interactive_mode(mcp: GodotDocMCP):
    """交互式搜索模式"""
    print("Godot 文档搜索系统 (输入 'exit' 退出)")
    while True:
        query = input("\n请输入搜索查询: ")
        if query.lower() == 'exit':
            break
        
        results = mcp.get_godot_context(query)
        if "error" in results:
            print(f"\n错误: {results['error']}")
            continue
            
        print("\n搜索结果:")
        for i, result in enumerate(results, 1):
            print(f"\n{i}. 文档 ID: {result['id']}")
            print(f"   相关度: {result['relevance']:.2f}")
            print(f"   来源: {result['metadata']['source']}")
            print(f"   内容: {result['document'][:200]}...")

def get_godot_context(query: str, n_results: int = 20) -> List[Dict[str, Any]]:
    """
    获取 Godot 文档上下文的简化接口
    
    Args:
        query: 查询字符串
        n_results: 返回结果数量
        
    Returns:
        包含相关文档的列表
    """
    # 默认数据库路径和集合名称
    db_path = "artifacts/vector_stores/chroma_db"
    collection_name = "godotengine_chunks_SZ_400_O_20_all-MiniLM-L6-v2"
    
    try:
        # 初始化客户端
        client = chromadb.PersistentClient(path=db_path)
        collection = client.get_collection(name=collection_name)
        
        # 加载模型
        model = SentenceTransformer('sentence-transformers/all-MiniLM-L6-v2')
        
        # 执行查询
        results = collection.query(
            query_embeddings=model.encode([query]).astype(float).tolist(),
            n_results=n_results
        )
        
        # 格式化结果
        formatted_results = []
        for i in range(len(results['ids'][0])):
            formatted_results.append({
                'id': results['ids'][0][i],
                'document': results['documents'][0][i],
                'metadata': results['metadatas'][0][i],
                'distance': results['distances'][0][i],
                'relevance': 1 - results['distances'][0][i]
            })
        
        return formatted_results
    except Exception as e:
        return [{"error": f"查询失败: {str(e)}"}]

def main():
    parser = argparse.ArgumentParser(description='Godot RAG MCP 服务器')
    parser.add_argument('--chromadb-path', '-d', type=str, 
                       default="artifacts/vector_stores/chroma_db",
                       help='ChromaDB 数据库路径')
    parser.add_argument('--collection-name', '-c', type=str,
                       help='要查询的 ChromaDB 集合名称')
    parser.add_argument('--interactive', '-i', action='store_true',
                       help='启动交互式模式')
    parser.add_argument('--query', '-q', type=str,
                       help='直接执行查询并返回结果')
    
    args = parser.parse_args()
    
    # 如果没有指定集合名称，尝试从文件读取
    if not args.collection_name:
        collections_file = "artifacts/vector_stores/collections.txt"
        if os.path.exists(collections_file):
            with open(collections_file, 'r', encoding='utf-8') as f:
                args.collection_name = f.read().strip()
        else:
            print("错误：未指定集合名称，且无法从 collections.txt 读取")
            return
    
    # 初始化 MCP
    try:
        mcp = GodotDocMCP(args.collection_name, args.chromadb_path)
        print(f"成功连接到数据库：{args.chromadb_path}")
        print(f"使用集合：{mcp.collection_name}")
    except Exception as e:
        print(f"错误：无法连接到数据库：{str(e)}")
        return
    
    if args.query:
        # 直接执行查询模式
        print(mcp.process_query(args.query))
    elif args.interactive:
        # 交互式模式
        interactive_mode(mcp)
    else:
        # 标准输入/输出模式
        try:
            while True:
                query = input()
                if not query:
                    continue
                print(mcp.process_query(query))
        except (EOFError, KeyboardInterrupt):
            pass

if __name__ == "__main__":
    main() 