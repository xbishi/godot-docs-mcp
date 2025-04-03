import chromadb
from sentence_transformers import SentenceTransformer
import os
import argparse

class InteractiveDocsQuery:
    def __init__(self, db_path, collection_name):
        """初始化交互式文档查询系统"""
        self.db_path = db_path
        self.collection_name = collection_name
        
        # 初始化 ChromaDB 客户端
        print("正在初始化向量数据库...")
        self.client = chromadb.PersistentClient(path=db_path)
        self.collection = self.client.get_collection(collection_name)
        
        # 初始化模型
        print("正在加载语言模型...")
        self.model = SentenceTransformer("sentence-transformers/all-MiniLM-L6-v2")
        print("系统初始化完成！\n")

    def search(self, query, n_results=5):
        """搜索文档"""
        try:
            # 生成查询向量
            embeddings = self.model.encode([query]).astype(float).tolist()
            
            # 执行查询
            results = self.collection.query(
                query_embeddings=embeddings,
                n_results=n_results
            )
            
            # 格式化并返回结果
            formatted_results = []
            for i in range(len(results['ids'][0])):
                formatted_results.append({
                    'id': results['ids'][0][i],
                    'document': results['documents'][0][i],
                    'metadata': results['metadatas'][0][i],
                    'relevance': 1 - results['distances'][0][i]
                })
            
            return formatted_results
        except Exception as e:
            print(f"搜索出错: {str(e)}")
            return []

    def interactive_loop(self):
        """交互式查询循环"""
        print("欢迎使用 Godot 4.4 文档交互式查询系统！")
        print("输入 'q' 或 'quit' 退出")
        print("输入 'h' 或 'help' 获取帮助")
        print("-" * 50)
        
        while True:
            try:
                # 获取用户输入
                query = input("\n请输入您的问题: ").strip()
                
                # 检查特殊命令
                if query.lower() in ['q', 'quit', 'exit']:
                    print("感谢使用！再见！")
                    break
                elif query.lower() in ['h', 'help']:
                    self.show_help()
                    continue
                elif not query:
                    continue
                
                # 执行搜索
                print("\n正在搜索相关文档...")
                results = self.search(query)
                
                # 显示结果
                if results:
                    print("\n找到以下相关内容：")
                    print("-" * 50)
                    for i, result in enumerate(results, 1):
                        relevance_percentage = result['relevance'] * 100
                        print(f"\n[{i}] 相关度: {relevance_percentage:.1f}%")
                        print(f"来源: {result['metadata']['source']}")
                        print(f"内容:\n{result['document']}")
                        print("-" * 50)
                else:
                    print("\n未找到相关内容。请尝试使用不同的关键词。")
                
            except KeyboardInterrupt:
                print("\n\n正在退出...")
                break
            except Exception as e:
                print(f"\n发生错误: {str(e)}")

    def show_help(self):
        """显示帮助信息"""
        print("\n帮助信息：")
        print("1. 输入任何关于 Godot 4.4 的问题")
        print("2. 系统会返回最相关的文档片段")
        print("3. 每个结果都会显示相关度和来源")
        print("4. 特殊命令：")
        print("   - q/quit/exit: 退出程序")
        print("   - h/help: 显示此帮助信息")
        print("\n搜索技巧：")
        print("- 使用具体的关键词")
        print("- 可以用中文或英文提问")
        print("- 尽量描述清楚具体的问题")

def main():
    parser = argparse.ArgumentParser(description='交互式 Godot 文档查询系统')
    parser.add_argument('--db-path', '-d', type=str, 
                       default="artifacts/vector_stores/chroma_db",
                       help='向量数据库路径')
    parser.add_argument('--collection', '-c', type=str,
                       default="godotengine_chunks_SZ_400_O_20_all-MiniLM-L6-v2",
                       help='集合名称')
    
    args = parser.parse_args()
    
    # 检查数据库路径
    if not os.path.exists(args.db_path):
        print(f"错误：数据库路径不存在: {args.db_path}")
        return
    
    # 创建查询系统实例并运行
    query_system = InteractiveDocsQuery(args.db_path, args.collection)
    query_system.interactive_loop()

if __name__ == "__main__":
    main() 