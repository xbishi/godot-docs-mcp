#!/usr/bin/env python3

import os
import re
import argparse
from bs4 import BeautifulSoup

class PageCurator:
    def __init__(self, input_dir):
        """
        初始化页面清理器
        Args:
            input_dir: 输入目录路径，包含要处理的HTML文件
        """
        self.input_dir = input_dir
        self.output_dir = os.path.join("artifacts", "curated")
        
        # 提取域名以保持文件夹结构
        if os.path.basename(os.path.dirname(input_dir)) == "downloaded_sites":
            # 如果输入是downloaded_sites下的直接域名文件夹
            self.domain = os.path.basename(input_dir)
        else:
            # 如果输入路径更深（例如downloaded_sites/domain/en/stable）
            # 提取downloaded_sites后的第一个文件夹
            parts = input_dir.split(os.sep)
            if "downloaded_sites" in parts:
                idx = parts.index("downloaded_sites")
                if idx + 1 < len(parts):
                    self.domain = parts[idx + 1]
                else:
                    self.domain = None
            else:
                self.domain = None
        
    def clean_html(self, html_content):
        """
        清理HTML内容，移除脚本、样式和不必要的导航元素
        Args:
            html_content: 要清理的HTML内容
        Returns:
            清理后的HTML内容
        """
        # 首先清理非UTF8和特殊字符
        html_content = re.sub(r'[^\x00-\x7F]+', '', html_content) 
        
        soup = BeautifulSoup(html_content, 'html.parser')

        # 移除脚本和样式标签
        for tag in soup(['script', 'style', 'iframe', 'noscript']):
            tag.decompose()
        
        # 移除导航元素、搜索框等
        selectors_to_remove = [
            'nav',                     # 导航菜单
            '.nav',                    # 导航类
            '.navigation',
            '.navbar',
            '.sidebar',
            '.menu',
            '.header',                 # 页眉通常包含导航
            '.footer',                 # 页脚通常包含无关链接
            '.search',                 # 搜索表单
            '.pagination',             # 下一页/上一页链接
            '[role="search"]',         # 搜索角色元素
            '[role="navigation"]',     # 导航角色元素
            '.wy-nav-side',           # ReadTheDocs特定
            '.wy-side-scroll',
            '.wy-side-nav-search',
            '.wy-menu',
            '.rst-versions',
            '.wy-nav-top',
            '.toc',                    # 目录（通常在侧边栏）
            '.breadcrumb',            # 面包屑导航
            '.toctree',               # 文档目录
            '.toctree-l1',           # 文档目录级别
            '.toctree-l2',
            '.toctree-l3',
            '.toctree-l4',
            '.contents',              # 目录的替代名称
            '#table-of-contents',     # 常见目录ID
            '[role="contentinfo"]'    # 通常包含目录或导航
        ]
        
        for selector in selectors_to_remove:
            for element in soup.select(selector):
                element.decompose()
        
        # 移除可能是导航或外部的链接
        for a_tag in soup.find_all('a'):
            href = a_tag.get('href', '')
            
            # 检查链接是否可能是导航或外部链接
            is_nav_link = False
            nav_patterns = ['search', 'next', 'prev', 'previous', 'index', 'home', 'contact', 'about']
            
            # 检查链接的文本内容
            if a_tag.text and any(pattern in a_tag.text.lower() for pattern in nav_patterns):
                is_nav_link = True
            
            # 检查href属性
            if href and (href.startswith('http') or any(pattern in href.lower() for pattern in nav_patterns)):
                is_nav_link = True
            
            # 用文本内容替换导航链接
            if is_nav_link:
                a_tag.replace_with(a_tag.text)
        
        # 移除空容器
        for tag in soup.find_all():
            if tag.name != 'br' and tag.name != 'img' and not tag.text.strip() and not tag.contents:
                tag.decompose()
                
        # 获取主要内容 - 优先使用main、article或content部分
        main_content = None
        for selector in ['main', 'article', '#content', '.content', '.main-content', '.document', '.section']:
            content_section = soup.select_one(selector)
            if content_section:
                main_content = content_section
                break
        
        # 如果找到主要内容区域，使用它；否则使用整个body
        if main_content:
            cleaned_html = str(main_content)
        else:
            # 如果没有明确的主要内容，使用body或整个内容（如果找不到body）
            body = soup.body or soup
            cleaned_html = str(body)
            
        return cleaned_html
    
    def html_to_markdown(self, html_content):
        """
        将清理后的HTML内容转换为Markdown格式
        Args:
            html_content: 要转换的HTML内容
        Returns:
            转换后的Markdown内容
        """
        # 使用html2text将HTML转换为Markdown
        try:
            import html2text
            h = html2text.HTML2Text()
            h.ignore_links = True
            h.ignore_images = True
            h.ignore_tables = False
            h.ignore_emphasis = True
            markdown_content = h.handle(html_content)
            return markdown_content
        except ImportError:
            # 如果无法导入html2text，使用BeautifulSoup进行基本文本提取
            soup = BeautifulSoup(html_content, 'html.parser')
            
            # 提取文本并保留一些结构
            markdown_lines = []
            
            # 处理标题
            for i in range(1, 7):
                for heading in soup.find_all(f'h{i}'):
                    markdown_lines.append(f"{'#' * i} {heading.text.strip()}\n")
            
            # 处理段落
            for p in soup.find_all('p'):
                markdown_lines.append(f"{p.text.strip()}\n\n")
            
            # 处理列表
            for ul in soup.find_all('ul'):
                for li in ul.find_all('li'):
                    markdown_lines.append(f"* {li.text.strip()}\n")
                markdown_lines.append("\n")
            
            for ol in soup.find_all('ol'):
                for i, li in enumerate(ol.find_all('li')):
                    markdown_lines.append(f"{i+1}. {li.text.strip()}\n")
                markdown_lines.append("\n")
            
            return ''.join(markdown_lines)
    
    def process_file(self, filepath):
        """
        处理单个HTML文件
        Args:
            filepath: 要处理的文件路径
        Returns:
            处理是否成功
        """
        try:
            # 读取文件
            with open(filepath, 'r', encoding='utf-8', errors='ignore') as f:
                html_content = f.read()
            
            # 清理HTML
            cleaned_html = self.clean_html(html_content)
            
            # 转换为Markdown
            markdown_content = self.html_to_markdown(cleaned_html)
            
            # 确定输出路径
            rel_path = os.path.relpath(filepath, self.input_dir)
            
            # 如果有域名，将其包含在输出路径中
            if self.domain:
                output_path = os.path.join(self.output_dir, self.domain, rel_path)
            else:
                output_path = os.path.join(self.output_dir, rel_path)
            
            # 将文件扩展名改为.md
            output_path = os.path.splitext(output_path)[0] + '.md'
            
            # 创建目录（如果不存在）
            os.makedirs(os.path.dirname(output_path), exist_ok=True)
            
            # 写入Markdown内容
            with open(output_path, 'w', encoding='utf-8') as f:
                f.write(markdown_content)
            
            print(f"已处理: {filepath} -> {output_path}")
            return True
        except Exception as e:
            print(f"处理出错 {filepath}: {e}")
            return False

    def process_directory(self):
        """处理输入目录中的所有HTML文件"""
        # 创建输出目录（如果不存在）
        os.makedirs(self.output_dir, exist_ok=True)
        
        # 统计计数
        processed_files = 0
        failed_files = 0
        
        # 遍历输入目录
        for root, dirs, files in os.walk(self.input_dir):
            for file in files:
                if file.endswith('.html'):
                    filepath = os.path.join(root, file)
                    success = self.process_file(filepath)
                    if success:
                        processed_files += 1
                    else:
                        failed_files += 1
        
        print(f"\n清理完成。已处理 {processed_files} 个文件。失败: {failed_files}。")


if __name__ == "__main__":
    # 创建命令行参数解析器
    parser = argparse.ArgumentParser(description="清理下载的网页以进行嵌入。")
    parser.add_argument("--input", "-i", 
                        help="包含下载网站的输入目录")
   
    args = parser.parse_args()
    
    # 创建清理器实例并处理目录
    curator = PageCurator(input_dir=args.input)
    curator.process_directory()
