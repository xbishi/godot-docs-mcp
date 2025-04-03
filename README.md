# Godot 4.4 文档向量化查询系统

这是一个基于向量数据库的 Godot 4.4 文档处理和查询系统，支持文档下载、处理、向量化和语义搜索功能。系统包含完整的文档处理流程和交互式查询界面。

## 功能特点

### 文档处理
- 自动下载和处理 Godot 文档
- HTML 到 Markdown 的转换
- 文本分块和向量化
- 基于 ChromaDB 的向量存储

### 查询功能
- 基于语义的文档搜索
- 交互式命令行界面
- 支持中英文查询
- 显示相关度百分比
- 显示文档来源
- 格式化输出结果

### 可视化
- 文档向量的 2D/3D 可视化
- 聚类分析和展示
- 交互式数据探索

## 系统要求

- Python 3.9+
- CUDA（可选，用于加速向量化）

## 安装

1. 克隆仓库：
```bash
git clone https://github.com/[your-username]/godot-docs-search.git
cd godot-docs-search
```

2. 创建虚拟环境（推荐）：
```bash
python -m venv venv
# Windows
venv\Scripts\activate
# Linux/Mac
source venv/bin/activate
```

3. 安装依赖：
```bash
pip install -r requirements.txt
```

## 使用方法

### 1. 文档处理流程

a. 下载文档：
```bash
python downloader.py --delay 1.0
```

b. 处理文档：
```bash
python curator.py --input artifacts/downloaded_sites/godotengine
```

c. 创建文本块：
```bash
python chunker.py --input artifacts/curated/godotengine --chunk-size 400 --chunk-overlap 20
```

d. 向量化处理：
```bash
python vectorizer.py --input artifacts/chunks/godotengine_chunks_SZ_400_O_20.jsonl
```

e. 可视化（可选）：
```bash
python visualizer.py --collection godotengine_chunks_SZ_400_O_20_all-MiniLM-L6-v2
```

### 2. 交互式查询

```bash
python interactive_docs.py
```

可选参数：
- `--db-path`, `-d`: 向量数据库路径
- `--collection`, `-c`: 集合名称

### 3. MCP 服务器

```bash
python mcp_server.py -d artifacts/vector_stores/chroma_db -c godotengine_chunks_SZ_400_O_20_all-MiniLM-L6-v2
```

## 项目结构

```
.
├── README.md              # 项目文档
├── requirements.txt       # 依赖列表
├── downloader.py         # 文档下载器
├── curator.py           # 文档处理器
├── chunker.py           # 文本分块器
├── vectorizer.py        # 向量化处理器
├── visualizer.py        # 向量可视化工具
├── interactive_docs.py  # 交互式查询界面
├── mcp_server.py        # MCP 服务器
└── artifacts/           # 资源文件夹
    ├── downloaded_sites/ # 下载的原始文档
    ├── curated/         # 处理后的文档
    ├── chunks/          # 文本块
    ├── vector_stores/   # 向量数据库
    └── visualizations/  # 可视化结果
```

## 依赖说明

项目依赖分为以下几类：
- 核心依赖：ChromaDB、Sentence-Transformers
- MCP 相关：MCP CLI、HTTPX
- 文档处理：BeautifulSoup4、Langchain
- 数据处理：NumPy、Scikit-learn
- 可视化：Plotly、UMAP
- 开发工具：pytest、black、flake8

详细依赖列表见 requirements.txt

## 开发指南

1. 代码风格
   - 使用 black 进行格式化
   - 使用 isort 排序导入
   - 遵循 flake8 规范

2. 测试
   - 使用 pytest 运行测试
   - 添加新功能时包含测试用例

## 注意事项

1. 确保数据库路径正确且存在
2. 首次运行时需要下载模型
3. 查询时尽量使用具体的关键词
4. 支持中英文混合查询
5. 大规模处理时建议使用 GPU 加速

## 贡献

1. Fork 项目
2. 创建特性分支
3. 提交更改
4. 推送到分支
5. 创建 Pull Request

## 许可证

MIT License

Copyright (c) 2024 [Your Name]

Permission is hereby granted, free of charge, to any person obtaining a copy
of this software and associated documentation files (the "Software"), to deal
in the Software without restriction, including without limitation the rights
to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
copies of the Software, and to permit persons to whom the Software is
furnished to do so, subject to the following conditions:

The above copyright notice and this permission notice shall be included in all
copies or substantial portions of the Software.

THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE
SOFTWARE.
