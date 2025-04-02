extends Node

# 导入必要的模块
const MCP = preload("res://addons/mcp/mcp.gd")

func _ready():
    # 初始化 MCP
    var mcp = MCP.new()
    
    # 查询示例
    var query = "如何在 Godot 中创建一个 2D 游戏？"
    var results = mcp.query(query)
    
    # 处理结果
    for result in results:
        print("相关度: ", result.relevance)
        print("内容: ", result.document.substr(0, 200), "...")
        print("来源: ", result.metadata.source)
        print("---")

# 示例：在编辑器中使用 MCP
static func query_godot_docs(query: String) -> Array:
    var mcp = MCP.new()
    return mcp.query(query) 