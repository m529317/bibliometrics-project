import pandas as pd
import networkx as nx
import matplotlib.pyplot as plt
from collections import defaultdict
from pathlib import Path
import re

DATA = Path("cleaned_papers.pkl")
OUTPUT_IMG = Path("keyword_cooccurrence_network.png")

plt.rcParams['font.sans-serif'] = ['SimHei']
plt.rcParams['axes.unicode_minus'] = False


def extract_keywords(text, top_n=10):
    if pd.isna(text) or not text:
        return []
    
    text = str(text).lower()
    
    stop_words = set([
        'the', 'and', 'of', 'in', 'to', 'a', 'is', 'for', 'that', 'with',
        'on', 'this', 'from', 'be', 'are', 'as', 'by', 'or', 'an', 'which',
        'at', 'was', 'were', 'will', 'has', 'have', 'had', 'been', 'can',
        'could', 'may', 'might', 'should', 'would', 'must', 'about', 'after',
        'all', 'also', 'any', 'because', 'but', 'not', 'some', 'such', 'than',
        'then', 'these', 'they', 'this', 'those', 'through', 'too', 'very',
        'what', 'when', 'where', 'while', 'who', 'whom', 'whose', 'why',
        'how', 'each', 'every', 'both', 'few', 'more', 'most', 'other', 'so',
        'purpose', 'method', 'result', 'conclusion', 'study', 'research',
        'paper', 'article', 'analysis', 'using', 'based', 'system', 'approach',
        'model', 'data', 'information', 'knowledge', 'technology', 'application',
        'ai', 'intelligence', 'artificial'
    ])
    
    words = re.findall(r'[a-zA-Z]+', text)
    
    word_counts = defaultdict(int)
    for word in words:
        word = word.strip().lower()
        if len(word) >= 3 and word not in stop_words:
            word_counts[word] += 1
    
    return [word for word, _ in sorted(word_counts.items(), key=lambda x: x[1], reverse=True)[:top_n]]


def main():
    print("正在生成关键词共现网络...")
    df = pd.read_pickle(DATA)
    
    all_keywords = []
    for abstract in df['abstract'].dropna():
        keywords = extract_keywords(abstract, top_n=8)
        all_keywords.append(keywords)
    
    cooccurrence = defaultdict(int)
    keyword_counts = defaultdict(int)
    
    for keywords in all_keywords:
        for keyword in keywords:
            keyword_counts[keyword] += 1
        for i in range(len(keywords)):
            for j in range(i + 1, len(keywords)):
                k1, k2 = sorted([keywords[i], keywords[j]])
                cooccurrence[(k1, k2)] += 1
    
    min_count = 3
    valid_keywords = {kw for kw, cnt in keyword_counts.items() if cnt >= min_count}
    print(f"有效关键词数量（出现≥{min_count}次）: {len(valid_keywords)}")
    
    filtered_cooccurrence = {
        (k1, k2): cnt for (k1, k2), cnt in cooccurrence.items()
        if k1 in valid_keywords and k2 in valid_keywords and cnt >= 2
    }
    
    G = nx.Graph()
    G.add_weighted_edges_from([(k1, k2, cnt) for (k1, k2), cnt in filtered_cooccurrence.items()])
    
    plt.figure(figsize=(14, 12))
    pos = nx.spring_layout(G, k=0.4, iterations=50, seed=42)
    
    node_sizes = [keyword_counts[kw] * 150 for kw in G.nodes()]
    edge_weights = [G[u][v]['weight'] * 1.5 for u, v in G.edges()]
    
    nx.draw_networkx_nodes(G, pos, node_size=node_sizes, node_color='#2ca02c', alpha=0.7)
    nx.draw_networkx_edges(G, pos, width=edge_weights, alpha=0.4, edge_color='gray')
    nx.draw_networkx_labels(G, pos, font_size=11, font_family='SimHei')
    
    plt.title('人工智能领域关键词共现网络', fontsize=18, pad=20)
    plt.axis('off')
    plt.tight_layout()
    
    plt.savefig(OUTPUT_IMG, dpi=300, bbox_inches='tight')
    print("关键词共现网络图已保存:", OUTPUT_IMG.name)
    
    print("\nTop15高频关键词:")
    top_keywords = sorted(keyword_counts.items(), key=lambda x: x[1], reverse=True)[:15]
    for kw, cnt in top_keywords:
        print(f"{kw}: {cnt}次")


if __name__ == "__main__":
    main()