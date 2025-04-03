from mcp.server.fastmcp import FastMCP
import chromadb
from sentence_transformers import SentenceTransformer
import argparse
import os
import logging
import sys
from typing import List, Dict, Any

# 配置日志
logging.basicConfig(
    level=logging.DEBUG,
    format='%(asctime)s - %(name)s - %(levelname)s - %(message)s',
    handlers=[
        logging.StreamHandler(sys.stdout),
        logging.FileHandler('mcp_server.log')
    ]
)
logger = logging.getLogger(__name__)

# 初始化 FastMCP 服务器
try:
    logger.info("Initializing FastMCP server")
    mcp = FastMCP("Vector Database Server")
    logger.info("FastMCP server initialized successfully")
except Exception as e:
    logger.error(f"Failed to initialize FastMCP server: {str(e)}")
    raise

# 全局变量
client: chromadb.PersistentClient = None
collection: chromadb.Collection = None
model = None

@mcp.tool(
    name="search_vectors",
    description="在向量数据库中搜索与查询相关的文档"
)
def search_vectors(query: str, n_results: int = 5) -> List[Dict[str, Any]]:
    """
    在向量数据库中搜索与查询相关的文档
    
    Args:
        query: 搜索查询
        n_results: 返回结果的数量
        
    Returns:
        包含相关文档的列表，每个文档包含 id、内容、元数据和相关度
    """
    try:
        if not collection or not model:
            logger.error("Server not properly initialized: collection or model is None")
            return {"error": "Server not properly initialized"}
            
        logger.debug(f"Processing query: {query}")
        embeddings = model.encode([query]).astype(float).tolist()
        logger.debug("Query encoded successfully")
        
        results = collection.query(
            query_embeddings=embeddings,
            n_results=n_results
        )
        logger.debug(f"Retrieved {len(results['documents'][0])} documents")
        
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
        logger.error(f"Failed to query vector database: {str(e)}", exc_info=True)
        return {"error": f"Failed to query vector database: {str(e)}"}

def initialize_services(db_path: str, collection_name: str):
    """初始化所有必需的服务"""
    global client, collection, model
    
    try:
        # 确保路径存在
        db_path = os.path.abspath(db_path)
        os.makedirs(db_path, exist_ok=True)
        logger.info(f"Database path: {db_path}")
        
        # 初始化 ChromaDB
        logger.info("Initializing ChromaDB client")
        client = chromadb.PersistentClient(path=db_path)
        logger.info("ChromaDB client initialized successfully")
        
        # 获取集合
        logger.info(f"Getting collection: {collection_name}")
        collection = client.get_collection(collection_name)
        logger.info("Collection retrieved successfully")
        
        # 加载模型
        logger.info("Loading sentence transformer model")
        model = SentenceTransformer("sentence-transformers/all-MiniLM-L6-v2")
        logger.info("Model loaded successfully")
        
        return True
    except Exception as e:
        logger.error(f"Failed to initialize services: {str(e)}", exc_info=True)
        return False

if __name__ == "__main__":
    parser = argparse.ArgumentParser(description='Start the Vector Database MCP Server')
    parser.add_argument('--db-path', '-d', type=str, required=True,
                        help='Path to the ChromaDB database')
    parser.add_argument('--collection-name', '-c', type=str, required=True,
                        help='Name of the ChromaDB collection to query')
    
    args = parser.parse_args()
    
    try:
        logger.info("Starting server initialization")
        if not initialize_services(args.db_path, args.collection_name):
            logger.error("Failed to initialize services")
            sys.exit(1)
            
        logger.info("Starting MCP server")
        mcp.run()  # 让 FastMCP 使用默认的 transport 设置
    except Exception as e:
        logger.error(f"Failed to start server: {str(e)}", exc_info=True)
        sys.exit(1) 