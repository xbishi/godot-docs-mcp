@echo off
:: 设置代码页为 UTF-8
chcp 65001 > nul
cd /d "%~dp0"

:: 检查 Python 是否已安装
python --version >nul 2>nul
if %errorlevel% neq 0 (
    echo 错误: 未检测到 Python。
    echo 请安装 Python 3.8 或更高版本。
    echo.
    echo 按任意键退出...
    pause > nul
    exit /b 1
)

:: 检查 Graphviz 是否已安装
where dot >nul 2>nul
if %errorlevel% neq 0 (
    echo ============================================
    echo 错误: 未检测到 Graphviz
    echo ============================================
    echo.
    echo 请按照以下步骤安装 Graphviz：
    echo.
    echo ^[1^] 访问 https://graphviz.org/download/
    echo ^[2^] 下载并安装 Windows 版本的 Graphviz
    echo ^[3^] 将 Graphviz 的 bin 目录添加到系统 PATH
    echo     ^(通常在 C:\Program Files\Graphviz\bin^)
    echo ^[4^] 重新启动命令提示符
    echo.
    echo ============================================
    echo 按任意键继续^(如果不需要可视化功能^)
    echo 或关闭窗口去安装 Graphviz...
    echo ============================================
    pause > nul
)

:: 检查虚拟环境是否存在
if not exist ".venv" (
    echo 正在创建虚拟环境...
    python -m venv .venv
    if %errorlevel% neq 0 (
        echo 错误: 创建虚拟环境失败。
        echo 请检查 Python 版本和权限设置。
        echo.
        echo 按任意键退出...
        pause > nul
        exit /b 1
    )
    echo 正在安装依赖...
    call ".venv\Scripts\activate.bat"
    pip install -r requirements.txt
    if %errorlevel% neq 0 (
        echo 错误: 安装依赖失败。
        echo 请检查网络连接和 requirements.txt 文件。
        echo.
        echo 按任意键退出...
        pause > nul
        exit /b 1
    )
) else (
    echo 正在激活虚拟环境...
    call ".venv\Scripts\activate.bat"
)

:: 设置环境变量
set PYTHONPATH=%CD%
set PYTHONIOENCODING=utf-8
set PYTHONUNBUFFERED=1

:: 检查必要的文件是否存在
if not exist "interactive_docs.py" (
    echo 错误: 未找到 interactive_docs.py 文件。
    echo 请确保文件存在于当前目录。
    echo.
    echo 按任意键退出...
    pause > nul
    exit /b 1
)

:: 启动交互式查询脚本
echo ============================================
echo 正在启动 Godot 4.4 文档交互式查询系统...
echo 提示: 输入 'exit' 或 'quit' 可以退出系统
echo ============================================
echo.
python interactive_docs.py

:: 如果脚本退出，等待用户按键
echo.
echo 按任意键退出...
pause > nul 