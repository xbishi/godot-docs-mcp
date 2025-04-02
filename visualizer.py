#!/usr/bin/env python3

import os
import argparse
import numpy as np
import plotly.graph_objects as go
import chromadb
from umap import UMAP
import webbrowser
import random
from sklearn.cluster import KMeans


class EmbeddingVisualizer:
    """使用降维技术在3D空间中可视化ChromaDB中的嵌入向量。"""
    
    def __init__(
        self,
        db_directory: str,
        collection_name: str,
        max_points: int = 2000,
        random_seed: int = 42,
        n_clusters: int = 10,
        outlier_threshold: float = 3.0
    ):
        """
        初始化可视化器
        Args:
            db_directory: ChromaDB数据库目录路径
            collection_name: ChromaDB中的集合名称
            max_points: 要可视化的最大点数（用于性能优化）
            random_seed: 用于重现性的随机种子
            n_clusters: 用于点着色的聚类数量
            outlier_threshold: 离群值移除的Z分数阈值（值越高保留的离群值越多）
        """
        self.db_directory = db_directory
        self.collection_name = collection_name
        # 更新输出目录到artifacts/visualizations
        visualization_dir = "artifacts/visualizations"
        self.output_file = f"{visualization_dir}/visualization_{collection_name}_{random_seed}_{max_points}_{n_clusters}_{outlier_threshold}.html"
        self.max_points = max_points
        self.random_seed = random_seed
        self.n_clusters = n_clusters
        self.outlier_threshold = outlier_threshold
        
        # 设置随机种子以确保重现性
        random.seed(self.random_seed)
        np.random.seed(self.random_seed)
        
        # 初始化ChromaDB客户端
        print(f"连接到 {db_directory} 的ChromaDB")
        self.client = chromadb.PersistentClient(path=db_directory)
        
        # 获取集合
        try:
            self.collection = self.client.get_collection(name=collection_name)
            print(f"找到集合: {collection_name}，包含 {self.collection.count()} 个文档")
        except Exception as e:
            print(f"访问集合时出错: {e}")
            raise
        
    def get_embeddings(self):
        """
        从ChromaDB检索嵌入向量和元数据
        Returns:
            嵌入向量、文档、元数据和ID的元组
        """
        print("从ChromaDB检索嵌入向量...")
        
        # 获取所有嵌入向量
        result = self.collection.get(
            include=['embeddings', 'documents', 'metadatas']
        )
        
        embeddings = np.array(result['embeddings'])
        documents = result['documents']
        metadatas = result['metadatas']
        ids = result['ids']
        
        print(f"检索到 {len(embeddings)} 个嵌入向量，维度为 {embeddings.shape[1]}")
        
        # 如果嵌入向量太多，采样一个子集
        if len(embeddings) > self.max_points:
            print(f"从 {len(embeddings)} 个点中采样 {self.max_points} 个点进行可视化")
            indices = np.random.choice(len(embeddings), self.max_points, replace=False)
            embeddings = embeddings[indices]
            documents = [documents[i] for i in indices]
            metadatas = [metadatas[i] for i in indices]
            ids = [ids[i] for i in indices]
            
        return embeddings, documents, metadatas, ids
    
    def reduce_dimensions(self, embeddings):
        """
        使用UMAP将嵌入向量降维到2D和3D
        Args:
            embeddings: 要降维的嵌入向量
        Returns:
            2D和3D降维后的嵌入向量
        """
        print("使用UMAP降维...")
        
        # 降维到3D
        reducer_3d = UMAP(n_components=3, random_state=self.random_seed, n_neighbors=15, min_dist=0.1)
        embeddings_3d = reducer_3d.fit_transform(embeddings)
        print(f"维度从 {embeddings.shape[1]} 降至 3")
        
        # 降维到2D
        reducer_2d = UMAP(n_components=2, random_state=self.random_seed, n_neighbors=15, min_dist=0.1)
        embeddings_2d = reducer_2d.fit_transform(embeddings)
        print(f"维度从 {embeddings.shape[1]} 降至 2")
        
        return embeddings_2d, embeddings_3d
    
    def cluster_embeddings(self, embeddings):
        """
        对嵌入向量进行聚类以进行可视化着色
        Args:
            embeddings: 要聚类的嵌入向量
        Returns:
            聚类标签
        """
        print(f"将嵌入向量聚类为 {self.n_clusters} 组...")
        kmeans = KMeans(n_clusters=self.n_clusters, random_state=self.random_seed)
        clusters = kmeans.fit_predict(embeddings)
        return clusters
    
    def filter_outliers(self, embeddings_2d, embeddings_3d, documents, metadatas, ids, clusters):
        """
        过滤掉距离主聚类太远的离群点
        
        使用Z分数来识别在2D和3D空间中距离中心太远的点。
        返回所有输入的过滤版本。
        """
        print(f"使用阈值 {self.outlier_threshold} 过滤离群值...")
        
        # 计算3D嵌入向量每个轴的Z分数
        z_scores_3d = np.zeros_like(embeddings_3d)
        for dim in range(3):
            mean = np.mean(embeddings_3d[:, dim])
            std = np.std(embeddings_3d[:, dim])
            if std > 0:  # 避免除以零
                z_scores_3d[:, dim] = np.abs((embeddings_3d[:, dim] - mean) / std)
        
        # 如果任何维度的Z分数超过阈值，则该点为离群值
        max_z_scores_3d = np.max(z_scores_3d, axis=1)
        outliers_3d = max_z_scores_3d > self.outlier_threshold
        
        # 计算2D嵌入向量每个轴的Z分数
        z_scores_2d = np.zeros_like(embeddings_2d)
        for dim in range(2):
            mean = np.mean(embeddings_2d[:, dim])
            std = np.std(embeddings_2d[:, dim])
            if std > 0:  # 避免除以零
                z_scores_2d[:, dim] = np.abs((embeddings_2d[:, dim] - mean) / std)
        
        # 如果任何维度的Z分数超过阈值，则该点为离群值
        max_z_scores_2d = np.max(z_scores_2d, axis=1)
        outliers_2d = max_z_scores_2d > self.outlier_threshold
        
        # 组合两种离群值检测方法（一个点只有在2D和3D中都不是离群值时才会保留）
        outliers = outliers_2d | outliers_3d
        
        # 统计离群值数量
        num_outliers = np.sum(outliers)
        print(f"过滤掉 {num_outliers} 个离群值（占点的 {num_outliers/len(outliers)*100:.1f}%）")
        
        # 只保留非离群值点
        keep_indices = ~outliers
        embeddings_2d_filtered = embeddings_2d[keep_indices]
        embeddings_3d_filtered = embeddings_3d[keep_indices]
        documents_filtered = [doc for i, doc in enumerate(documents) if keep_indices[i]]
        metadatas_filtered = [meta for i, meta in enumerate(metadatas) if keep_indices[i]]
        ids_filtered = [id for i, id in enumerate(ids) if keep_indices[i]]
        clusters_filtered = clusters[keep_indices]
        
        return embeddings_2d_filtered, embeddings_3d_filtered, documents_filtered, metadatas_filtered, ids_filtered, clusters_filtered
    
    def create_visualization(self, embeddings_2d, embeddings_3d, documents, metadatas, ids, clusters, original_dims):
        """
        使用Plotly创建具有2D/3D切换功能的交互式可视化
        Args:
            embeddings_2d: 2D嵌入向量
            embeddings_3d: 3D嵌入向量
            documents: 文档内容
            metadatas: 元数据
            ids: 文档ID
            clusters: 聚类标签
            original_dims: 原始维度数
        """
        print("创建具有2D/3D切换功能的可视化...")
        
        # 创建颜色调色板
        colors = [
            '#1f77b4', '#ff7f0e', '#2ca02c', '#d62728', '#9467bd',
            '#8c564b', '#e377c2', '#7f7f7f', '#bcbd22', '#17becf',
            '#aec7e8', '#ffbb78', '#98df8a', '#ff9896', '#c5b0d5'
        ]
        
        # 创建悬停文本
        hover_texts = []
        for i in range(len(documents)):
            # 从源路径提取文件名
            source_path = metadatas[i]['source']
            filename = os.path.basename(source_path)
            
            # 截断文档文本用于悬停显示
            doc_preview = documents[i][:200] + "..." if len(documents[i]) > 200 else documents[i]
            doc_preview = doc_preview.replace("\n", "<br>")
            
            hover_text = f"<b>ID:</b> {ids[i]}<br><b>文件:</b> {filename}<br><b>预览:</b><br>{doc_preview}"
            hover_texts.append(hover_text)
        
        # 创建带有子图的图形
        fig = go.Figure()
        
        # 添加3D轨迹（初始可见）
        for cluster_id in range(self.n_clusters):
            cluster_indices = np.where(clusters == cluster_id)[0]
            
            fig.add_trace(go.Scatter3d(
                x=embeddings_3d[cluster_indices, 0],
                y=embeddings_3d[cluster_indices, 1],
                z=embeddings_3d[cluster_indices, 2],
                mode='markers',
                marker=dict(
                    size=5,
                    color=colors[cluster_id % len(colors)],
                    opacity=0.7,
                ),
                text=[hover_texts[i] for i in cluster_indices],
                hoverinfo='text',
                name=f'聚类 {cluster_id}',
                scene='scene',
                visible=True
            ))
        
        # 添加2D轨迹（初始隐藏）
        for cluster_id in range(self.n_clusters):
            cluster_indices = np.where(clusters == cluster_id)[0]
            
            fig.add_trace(go.Scatter(
                x=embeddings_2d[cluster_indices, 0],
                y=embeddings_2d[cluster_indices, 1],
                mode='markers',
                marker=dict(
                    size=8,
                    color=colors[cluster_id % len(colors)],
                    opacity=0.7,
                ),
                text=[hover_texts[i] for i in cluster_indices],
                hoverinfo='text',
                name=f'聚类 {cluster_id}',
                visible=False
            ))
        
        # 创建2D/3D切换按钮
        button_3d = dict(
            label="3D视图",
            method="update",
            args=[
                {"visible": [True] * self.n_clusters + [False] * self.n_clusters},
                {"scene": {"xaxis": {"title": "UMAP维度1"},
                           "yaxis": {"title": "UMAP维度2"},
                           "zaxis": {"title": "UMAP维度3"}},
                 "xaxis": {"title": ""},
                 "yaxis": {"title": ""},
                 "title": {"text": f"{self.collection_name} 嵌入向量的3D可视化（原始维度：{original_dims}）",
                           "y": 0.95,
                           "x": 0.5,
                           "xanchor": "center",
                           "yanchor": "top",
                           "font": {"size": 24}}}
            ]
        )
        
        # 创建2D视图按钮
        button_2d = dict(
            label="2D视图",
            method="update",
            args=[
                {"visible": [False] * self.n_clusters + [True] * self.n_clusters},
                {"scene": {"xaxis": {"title": ""},
                           "yaxis": {"title": ""},
                           "zaxis": {"title": ""}},
                 "xaxis": {"title": "UMAP维度1"},
                 "yaxis": {"title": "UMAP维度2"},
                 "title": {"text": f"{self.collection_name} 嵌入向量的2D可视化（原始维度：{original_dims}）",
                           "y": 0.95,
                           "x": 0.5,
                           "xanchor": "center",
                           "yanchor": "top",
                           "font": {"size": 24}}}
            ]
        )
        
        # 更新布局
        fig.update_layout(
            updatemenus=[
                dict(
                    type="buttons",
                    direction="right",
                    active=0,
                    x=0.57,
                    y=1.2,
                    buttons=[button_3d, button_2d],
                )
            ],
            showlegend=True,
            legend=dict(
                yanchor="top",
                y=0.99,
                xanchor="left",
                x=0.01
            )
        )
        
        return fig
    
    def save_and_open_visualization(self, fig):
        """
        保存可视化结果并在浏览器中打开
        Args:
            fig: 要保存的图形对象
        """
        # 创建输出目录（如果不存在）
        os.makedirs(os.path.dirname(self.output_file), exist_ok=True)
        
        # 保存HTML文件
        fig.write_html(self.output_file)
        print(f"可视化已保存到: {self.output_file}")
        
        # 在浏览器中打开
        webbrowser.open('file://' + os.path.abspath(self.output_file))
    
    def run(self):
        """运行完整的可视化流程"""
        # 获取嵌入向量
        embeddings, documents, metadatas, ids = self.get_embeddings()
        original_dims = embeddings.shape[1]
        
        # 降维
        embeddings_2d, embeddings_3d = self.reduce_dimensions(embeddings)
        
        # 聚类
        clusters = self.cluster_embeddings(embeddings)
        
        # 过滤离群值
        embeddings_2d, embeddings_3d, documents, metadatas, ids, clusters = self.filter_outliers(
            embeddings_2d, embeddings_3d, documents, metadatas, ids, clusters
        )
        
        # 创建可视化
        fig = self.create_visualization(
            embeddings_2d, embeddings_3d, documents, metadatas, ids, clusters, original_dims
        )
        
        # 保存并打开可视化
        self.save_and_open_visualization(fig)


if __name__ == "__main__":
    # 创建命令行参数解析器
    parser = argparse.ArgumentParser(description="使用降维技术在3D空间中可视化ChromaDB中的嵌入向量。")
    parser.add_argument("--collection", "-c", required=True,
                        help="要可视化的ChromaDB集合名称")
    parser.add_argument("--db", "-d", default="artifacts/vector_stores/chroma_db",
                        help="ChromaDB数据库目录（默认：artifacts/vector_stores/chroma_db）")
    parser.add_argument("--max-points", "-m", type=int, default=2000,
                        help="要可视化的最大点数（默认：2000）")
    parser.add_argument("--seed", "-s", type=int, default=42,
                        help="随机种子（默认：42）")
    parser.add_argument("--clusters", "-k", type=int, default=10,
                        help="聚类数量（默认：10）")
    parser.add_argument("--outlier-threshold", "-t", type=float, default=3.0,
                        help="离群值阈值（默认：3.0）")
    
    args = parser.parse_args()
    
    # 创建可视化器实例并运行
    visualizer = EmbeddingVisualizer(
        db_directory=args.db,
        collection_name=args.collection,
        max_points=args.max_points,
        random_seed=args.seed,
        n_clusters=args.clusters,
        outlier_threshold=args.outlier_threshold
    )
    visualizer.run()