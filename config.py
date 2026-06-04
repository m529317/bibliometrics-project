"""
项目参数配置文件
"""

# ==================== 数据清洗参数 ====================
CLEANING_CONFIG = {
    # 年份过滤
    'min_year': 2023,
    
    # 去重字段
    'deduplicate_fields': ['title', 'authors', 'year'],
    
    # 必需字段检查
    'required_fields': ['title', 'authors', 'year', 'abstract'],
}

# ==================== 趋势分析参数 ====================
TREND_CONFIG = {
    # 图表尺寸
    'figure_size': (12, 6),
    
    # DPI
    'dpi': 300,
    
    # 颜色
    'bar_color': '#1f77b4',
}

# ==================== 作者分析参数 ====================
AUTHOR_CONFIG = {
    # 高产作者阈值（发文数）
    'min_publications': 2,
    
    # 网络可视化参数
    'node_size_multiplier': 200,
    'spring_layout_k': 0.3,
    'spring_layout_seed': 42,
    
    # 输出Top N高产作者
    'top_n_authors': 10,
}

# ==================== 关键词网络参数 ====================
KEYWORD_CONFIG = {
    # 每篇文献提取Top N关键词
    'keywords_per_paper': 8,
    
    # 关键词最小出现次数
    'min_keyword_freq': 3,
    
    # 共现最小次数
    'min_cooccurrence': 2,
    
    # 停用词列表
    'stop_words': [
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
    ],
    
    # 网络可视化参数
    'node_size_multiplier': 150,
    'spring_layout_k': 0.4,
    'spring_layout_seed': 42,
    
    # 输出Top N关键词
    'top_n_keywords': 15,
}

# ==================== 代表文献参数 ====================
REPRESENTATIVE_CONFIG = {
    # 重要关键词列表
    'important_keywords': [
        'artificial intelligence', 'machine learning', 'deep learning',
        'neural network', 'llm', 'large language model', 'chatgpt',
        'transformer', 'natural language', 'computer vision',
        'reinforcement learning', 'data mining', 'knowledge graph'
    ],
    
    # 关键词匹配权重
    'keyword_score_weight': 1.0,
    
    # 年份评分：(年份 - year_baseline)
    'year_baseline': 2022,
    'year_score_weight': 1.0,
    
    # 输出Top N代表文献
    'top_n_papers': 15,
}

# ==================== 路径配置 ====================
PATH_CONFIG = {
    # 原始数据
    'raw_data': 'data/人工智能领域.ris',
    
    # 清洗后数据
    'cleaned_data_pickle': 'data/cleaned_papers.pkl',
    'cleaned_data_ris': 'data/cleaned_papers.ris',
    
    # 输出目录
    'output_dir': 'outputs/',
    
    # 图表文件
    'trend_figure': 'outputs/annual_publication_trend.png',
    'author_network': 'outputs/author_collaboration_network.png',
    'keyword_network': 'outputs/keyword_cooccurrence_network.png',
    
    # 代表文献
    'representative_txt': 'outputs/representative_papers.txt',
    'representative_csv': 'outputs/representative_papers.csv',
}

# ==================== 项目元信息 ====================
PROJECT_INFO = {
    'title': '人工智能领域研究文献计量分析',
    'version': '1.0',
    'authors': ['刘伟丰', '李丽', '王雪婷', '徐国林', '杜昊壅'],
    'date': '2026-06',
}
