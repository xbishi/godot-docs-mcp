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

:: 设置 PYTHONPATH
set PYTHONPATH=%CD%

:: 启动交互式查询脚本
echo 正在启动 Godot 4.4 文档交互式查询系统...
python interactive_docs.py

:: 如果脚本退出，等待用户按键
echo.
echo 按任意键退出...
pause > nul 