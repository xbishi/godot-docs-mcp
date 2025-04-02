from mcp_interface import get_godot_context
import json
import sys

def process_query(query: str) -> str:
    """
    处理查询并返回 JSON 格式的响应
    
    Args:
        query: 查询字符串
        
    Returns:
        JSON 格式的响应
    """
    results = get_godot_context(query)
    return json.dumps(results, ensure_ascii=False, indent=2)

def main():
    # 从标准输入读取查询
    query = sys.stdin.read().strip()
    if not query:
        print(json.dumps({"error": "未提供查询"}, ensure_ascii=False))
        return
    
    # 处理查询并输出结果
    print(process_query(query))

if __name__ == "__main__":
    main() 