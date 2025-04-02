#!/usr/bin/env python3

import os
import requests
from bs4 import BeautifulSoup
from urllib.parse import urljoin, urlparse
import argparse
import time

class WebsiteDownloader:
    def __init__(self, delay=1):
        """
        初始化网站下载器
        Args:
            delay: 请求之间的延迟时间（秒），用于避免对服务器造成过大压力
        """
        self.delay = delay  # 请求之间的延迟时间
        self.visited_urls = set()  # 已访问的URL集合，用于避免重复下载
        self.page_count = 0  # 页面计数器
        self.skipped_count = 0  # 跳过的页面计数器
        
    def download_page(self, url):
        """
        下载单个页面并保存到输出目录
        Args:
            url: 要下载的网页URL
        Returns:
            下载的HTML内容，如果下载失败则返回None
        """
        try:
            # 解析URL并创建保存路径
            parsed_url = urlparse(url)
            path = parsed_url.path
            
            # 处理根路径
            if path == "" or path == "/":
                filepath = os.path.join(self.output_dir, "index.html")
            else:
                # 移除开头的斜杠并创建目录结构
                if path.startswith("/"):
                    path = path[1:]
                
                # 处理结尾斜杠（目录索引）
                if path.endswith("/"):
                    path = os.path.join(path, "index.html")
                elif "." not in os.path.basename(path):
                    path = os.path.join(path, "index.html")
                
                filepath = os.path.join(self.output_dir, path)
            
            # 检查文件是否已存在，如果存在则跳过
            if os.path.exists(filepath):
                print(f"跳过（已存在）: {url} -> {filepath}")
                self.skipped_count += 1
                
                # 仍然需要返回内容以提取链接
                try:
                    with open(filepath, 'r', encoding='utf-8', errors='ignore') as f:
                        return f.read()
                except:
                    # 如果无法读取现有文件，则重新下载
                    pass
            
            # 如果文件不存在，则下载
            response = requests.get(url, timeout=10)
            if response.status_code == 200:
                # 创建目录（如果不存在）
                os.makedirs(os.path.dirname(filepath), exist_ok=True)
                
                # 保存内容
                with open(filepath, 'wb') as f:
                    f.write(response.content)
                
                print(f"已下载: {url} -> {filepath}")
                return response.text
            else:
                print(f"下载失败 {url}: HTTP {response.status_code}")
                return None
        except Exception as e:
            print(f"下载出错 {url}: {e}")
            return None

    def extract_links(self, html, base_url, scope_path):
        """
        从HTML内容中提取符合范围的链接
        Args:
            html: HTML内容
            base_url: 基础URL
            scope_path: 要爬取的范围路径
        Returns:
            提取的链接列表
        """
        soup = BeautifulSoup(html, 'html.parser')
        links = []
        
        parsed_base = urlparse(base_url)
        base_domain = parsed_base.netloc
        
        for a_tag in soup.find_all('a', href=True):
            href = a_tag['href']
            
            # 跳过锚点链接（指向同一页面内的部分）
            if '#' in href:
                continue
                
            full_url = urljoin(base_url, href)
            
            parsed_url = urlparse(full_url)
            
            # 只包含相同域名和范围内的链接
            if parsed_url.netloc == base_domain and parsed_url.path.startswith(scope_path):
                links.append(full_url)
                
        return links

    def process_url_list(self, url_list_file):
        """
        处理URL列表并下载每个URL范围内的页面
        Args:
            url_list_file: 包含URL列表的文件路径
        """
        # 从文件读取URL
        with open(url_list_file, 'r') as f:
            urls = [line.strip() for line in f if line.strip()]
        
        total_downloaded = 0
        
        for start_url in urls:
            print(f"\n处理URL: {start_url}")
            
            # 解析URL以确定范围
            parsed_url = urlparse(start_url)
            path = parsed_url.path
            
            # 用连字符替换域名中的点
            domain_folder = parsed_url.netloc.replace('.', '-')
            
            # 当前URL的输出目录
            self.output_dir = "artifacts/downloaded_sites/" + domain_folder
            # 创建输出目录（如果不存在）
            os.makedirs(self.output_dir, exist_ok=True)
            
            # 确定范围路径（包含index.html的目录）
            if path.endswith('index.html'):
                scope_path = path[:-10]  # 移除'index.html'
            elif path.endswith('/'):
                scope_path = path
            else:
                scope_path = path + '/'
            
            # 为每个新范围重置已访问的URL
            self.visited_urls = set()
            
            # 待访问的URL队列
            queue = [start_url]
            
            # 处理队列
            while queue:
                url = queue.pop(0)
                
                # 如果已访问则跳过
                if url in self.visited_urls:
                    continue
                
                # 标记为已访问
                self.visited_urls.add(url)
                
                # 下载页面
                html_content = self.download_page(url)
                
                if html_content:
                    total_downloaded += 1
                    # 提取链接并添加到队列（如果在范围内）
                    new_links = self.extract_links(html_content, url, scope_path)
                    for link in new_links:
                        if link not in self.visited_urls and link not in queue:
                            queue.append(link)
                
                # 对服务器友好
                time.sleep(self.delay)
        
        print(f"\n下载完成。总页面数: {total_downloaded}")
        print(f"已下载: {total_downloaded - self.skipped_count}, 已跳过: {self.skipped_count}")


if __name__ == "__main__":
    # 创建命令行参数解析器
    parser = argparse.ArgumentParser(description="从指定URL及其子目录下载页面。")
    parser.add_argument("--delay", "-d", type=float, default=1.0,
                        help="请求之间的延迟时间（秒）（默认：1.0）")
    
    args = parser.parse_args()
    
    # 创建下载器实例并处理URL列表
    downloader = WebsiteDownloader(
        delay=args.delay
    )
    
    downloader.process_url_list("websites_to_download.txt")
