#!/usr/bin/env python3

import os
import json
import hashlib
import argparse
from typing import List, Dict, Any
from langchain.text_splitter import RecursiveCharacterTextSplitter


class TextChunker:
    """将Markdown文件处理成文本块并保存为JSONL格式。"""
    
    def __init__(
        self, 
        input_dir: str, 
        chunk_size: int = 400,
        chunk_overlap: int = 20
    ):
        """
        初始化文本分块器
        Args:
            input_dir: 输入目录路径
            chunk_size: 每个文本块的最大字符数（默认：400）
            chunk_overlap: 文本块之间的重叠字符数（默认：20）
        """
        self.input_dir = input_dir
        
        # 从目录获取基础域名
        base_domain = os.path.basename(input_dir)
        # 确保域名命名一致，即使通过不同的流水线阶段
        if '.' in base_domain:
            base_domain = base_domain.replace('.', '-')
            
        self.output_file = f"artifacts/chunks/{base_domain}_chunks_SZ_{chunk_size}_O_{chunk_overlap}.jsonl"
        
        # 初始化LangChain的递归字符文本分割器
        self.splitter = RecursiveCharacterTextSplitter.from_language(
            language="markdown",
            chunk_size=chunk_size,
            chunk_overlap=chunk_overlap,
            add_start_index=True,
        )
        
    def _generate_uid(self, file_path: str) -> str:
        """
        基于文件路径生成唯一ID
        Args:
            file_path: 文件路径
        Returns:
            文件的唯一ID
        """
        # 创建文件路径的哈希值
        return hashlib.md5(file_path.encode()).hexdigest()
        
    def process_file(self, file_path: str) -> List[Dict[str, Any]]:
        """
        处理单个Markdown文件为文本块
        Args:
            file_path: 要处理的文件路径
        Returns:
            包含文本块信息的字典列表
        """
        try:
            # 读取文件内容
            with open(file_path, 'r', encoding='utf-8', errors='ignore') as f:
                content = f.read()
                
            # 基于文件路径生成唯一ID
            uid = self._generate_uid(file_path)
            
            # 使用LangChain的分割器将内容分割成块
            chunks = self.splitter.split_text(content)
            
            # 为每个块创建JSON对象
            result = []
            for i, chunk in enumerate(chunks):
                # 跳过空块
                if not chunk.strip():
                    continue
                    
                chunk_data = {
                    'id': f'{uid}-{i}',
                    'text': chunk,
                    'source': file_path
                }
                result.append(chunk_data)
                
            print(f"已处理 {file_path}: {len(result)} 个文本块")
            return result
            
        except Exception as e:
            print(f"处理出错 {file_path}: {e}")
            return []
            
    def process_directory(self) -> List[Dict[str, Any]]:
        """
        处理输入目录中的所有Markdown文件
        Returns:
            所有文件的文本块列表
        """
        all_chunks = []
        file_count = 0
        
        # 遍历输入目录
        for root, _, files in os.walk(self.input_dir):
            for file in files:
                if file.endswith('.md'):
                    file_path = os.path.join(root, file)
                    chunks = self.process_file(file_path)
                    all_chunks.extend(chunks)
                    file_count += 1
                    
        print(f"\n已处理 {file_count} 个文件，共 {len(all_chunks)} 个文本块。")
        return all_chunks
        
    def save_jsonl(self, chunks: List[Dict[str, Any]]) -> None:
        """
        将文本块保存到JSONL文件
        Args:
            chunks: 要保存的文本块列表
        """
        # 创建输出文件目录（如果需要）
        output_dir = os.path.dirname(self.output_file)
        if output_dir:
            os.makedirs(output_dir, exist_ok=True)
        
        # 如果输出文件已存在，则删除
        if os.path.exists(self.output_file):
            os.remove(self.output_file)
            
        # 将文本块写入JSONL文件
        with open(self.output_file, 'w', encoding='utf-8') as f:
            for chunk in chunks:
                f.write(json.dumps(chunk, ensure_ascii=False) + '\n')
                
        print(f"已将 {len(chunks)} 个文本块保存到 {self.output_file}")
        
    def run(self) -> None:
        """运行完整的分块处理流程"""
        chunks = self.process_directory()
        self.save_jsonl(chunks)


if __name__ == "__main__":
    # 创建命令行参数解析器
    parser = argparse.ArgumentParser(description="将Markdown文件分割成文本块并保存为JSONL格式。")
    parser.add_argument("--input", "-i", 
                        help="包含Markdown文件的输入目录")
    parser.add_argument("--chunk-size", "-s", type=int, default=400,
                        help="文本块的最大字符数（默认：400）")
    parser.add_argument("--chunk-overlap", "-v", type=int, default=20,
                        help="文本块之间的重叠字符数（默认：20）")
    
    args = parser.parse_args()
    
    # 创建文本分块器实例并运行
    chunker = TextChunker(
        input_dir=args.input,
        chunk_size=args.chunk_size,
        chunk_overlap=args.chunk_overlap
    )
    chunker.run()