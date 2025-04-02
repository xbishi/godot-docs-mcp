# Godot 文档 MCP 服务

这是一个基于 ChromaDB 的 Godot 文档检索系统，可以作为 MCP (Multi-Context Provider) 服务集成到各种支持 MCP 的软件中。

## 功能特点

- 支持语义搜索 Godot 官方文档
- 提供 RESTful API 接口
- 支持多种集成方式
- 可配置的查询参数
- 中文支持

## 安装说明

### 1. 环境要求

- Python 3.9+
- Conda 环境管理工具
- Git

### 2. 安装步骤

```bash
# 克隆仓库
git clone https://github.com/yourusername/godot-docs-mcp.git
cd godot-docs-mcp

# 创建并激活 Conda 环境
conda create -n web2embeddings python=3.9
conda activate web2embeddings

# 安装依赖
pip install -r requirements.txt
```

## 使用方法

### 1. 作为独立服务运行

```bash
# 启动服务
python mcp_interface.py

# 测试查询
curl -X POST http://localhost:8000/query -H "Content-Type: application/json" -d '{"query": "如何在 Godot 中创建一个 2D 游戏？"}'
```

### 2. 集成到 Cursor

1. 复制配置文件：
```bash
mkdir -p ~/.cursor
cp .cursor/mcp_config.json ~/.cursor/
```

2. 在 Cursor 设置中添加 MCP 配置：
```json
{
    "mcp_name": "godot_docs",
    "description": "Godot 文档检索系统",
    "command": "python",
    "args": ["/path/to/godot-docs-mcp/cursor_mcp.py"],
    "working_directory": "/path/to/godot-docs-mcp",
    "env": {
        "PYTHONPATH": "/path/to/godot-docs-mcp",
        "CONDA_ENV": "web2embeddings"
    }
}
```

### 3. 集成到其他支持 MCP 的软件

#### 3.1 通过命令行接口

```bash
# 直接查询
echo "您的查询" | python cursor_mcp.py

# 或者
python mcp_interface.py -q "您的查询"
```

#### 3.2 通过 Python API

```python
from mcp_interface import get_godot_context

# 执行查询
results = get_godot_context("您的查询")
for result in results:
    print(f"相关度: {result['relevance']:.2f}")
    print(f"内容: {result['document'][:200]}...")
```

## 配置说明

### 1. 数据库配置

默认数据库路径：`artifacts/vector_stores/chroma_db`

如需修改，请编辑 `mcp_interface.py` 中的 `db_path` 参数。

### 2. 查询参数

- `n_results`: 返回结果数量（默认：20）
- `collection_name`: ChromaDB 集合名称

## 项目结构

```
godot-docs-mcp/
├── .cursor/                    # Cursor 配置文件
│   ├── mcp_config.json        # MCP 配置
│   └── activate_mcp.bat       # 环境激活脚本
├── artifacts/                  # 数据文件
│   ├── curated/               # 清理后的文档
│   └── vector_stores/         # 向量数据库
├── mcp_interface.py           # 主程序
├── cursor_mcp.py              # Cursor 集成
├── requirements.txt           # 依赖列表
└── README.md                  # 说明文档
```

## 常见问题

### 1. 环境问题

如果遇到环境激活失败：
```bash
# 检查 Conda 环境
conda env list

# 重新创建环境
conda create -n web2embeddings python=3.9
conda activate web2embeddings
pip install -r requirements.txt
```

### 2. 查询问题

如果查询无结果：
- 检查数据库路径是否正确
- 确认集合名称是否正确
- 验证文档是否已正确导入

### 3. 性能优化

- 减少返回结果数量
- 优化查询语句
- 使用更高效的模型

## 贡献指南

1. Fork 项目
2. 创建特性分支
3. 提交更改
4. 推送到分支
5. 创建 Pull Request

## 许可证

MIT License

## 联系方式

- 项目主页：https://github.com/yourusername/godot-docs-mcp
- 问题反馈：https://github.com/yourusername/godot-docs-mcp/issues
