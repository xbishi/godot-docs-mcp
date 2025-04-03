@echo off
cd /d %~dp0

:: 检查虚拟环境是否存在
if not exist ".venv" (
    echo 正在创建虚拟环境...
    python -m venv .venv
    echo 正在安装依赖...
    call .venv\Scripts\activate
    pip install -r requirements.txt
) else (
    echo 正在激活虚拟环境...
    call .venv\Scripts\activate
)

:: 设置环境变量
set PYTHONPATH=%CD%
set PYTHONIOENCODING=utf-8
set PYTHONUNBUFFERED=1

:: 启动 MCP 服务器
echo 正在启动 Godot 4.4 文档 MCP 服务器...
python mcp_server.py -d artifacts/vector_stores/chroma_db -c godotengine_chunks_SZ_400_O_20_all-MiniLM-L6-v2

:: 如果服务器退出，等待用户按键
echo.
echo 按任意键退出...
pause > nul 