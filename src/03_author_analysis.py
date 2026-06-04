import pandas as pd
import networkx as nx
import matplotlib.pyplot as plt
from collections import defaultdict
from pathlib import Path

# 路径配置
DATA = Path("../data/cleaned_papers.pkl")
OUTPUT_IMG = Path("../outputs/author_collaboration_network.png")

# 设置中文显示
plt.rcParams['font.sans-serif'] = ['SimHei']
plt.rcParams['axes.unicode_minus'] = False


def main():
    print("正在生成作者合作网络图...")
    df = pd.read_pickle(DATA)

    # 统计作者发文量
    author_counts = defaultdict(int)
    for authors in df['authors']:
        for author in authors.split('; '):
            author_counts[author] += 1

    # 筛选发文量≥2的作者（数据量小，降低阈值）
    top_authors = {author for author, count in author_counts.items() if count >= 2}
    print(f"高产作者数量（发文≥2）: {len(top_authors)}")

    # 构建合作网络
    coauthorship = defaultdict(int)
    for authors in df['authors']:
        author_list = authors.split('; ')
        filtered_authors = [a for a in author_list if a in top_authors]
        if len(filtered_authors) < 2:
            continue
        # 生成所有两两组合
        for i in range(len(filtered_authors)):
            for j in range(i + 1, len(filtered_authors)):
                a1, a2 = sorted([filtered_authors[i], filtered_authors[j]])
                coauthorship[(a1, a2)] += 1

    # 构建网络
    G = nx.Graph()
    G.add_weighted_edges_from([(a1, a2, count) for (a1, a2), count in coauthorship.items()])

    # 绘制网络
    plt.figure(figsize=(14, 14))
    pos = nx.spring_layout(G, k=0.3, iterations=50, seed=42)

    # 节点大小与发文量成正比
    node_sizes = [author_counts[author] * 200 for author in G.nodes()]

    # 绘制节点和边
    nx.draw_networkx_nodes(G, pos, node_size=node_sizes, node_color='#ff7f0e', alpha=0.7)
    nx.draw_networkx_edges(G, pos, width=0.8, alpha=0.5, edge_color='gray')
    nx.draw_networkx_labels(G, pos, font_size=10, font_family='SimHei')

    plt.title('人工智能领域作者合作网络（发文≥2篇）', fontsize=18, pad=20)
    plt.axis('off')
    plt.tight_layout()

    plt.savefig(OUTPUT_IMG, dpi=300, bbox_inches='tight')
    print(f"✅ 作者合作网络图已保存: {OUTPUT_IMG.name}")

    # 输出Top10高产作者
    print("\nTop10高产作者:")
    top_authors_sorted = sorted(author_counts.items(), key=lambda x: x[1], reverse=True)[:10]
    for author, count in top_authors_sorted:
        print(f"{author}: {count}篇")


if __name__ == "__main__":
    main()