import pandas as pd
from pathlib import Path

DATA = Path("cleaned_papers.pkl")
OUTPUT_TXT = Path("representative_papers.txt")
OUTPUT_CSV = Path("representative_papers.csv")


def main():
    print("正在生成代表文献表...")
    df = pd.read_pickle(DATA)
    
    df['year'] = pd.to_numeric(df['year'], errors='coerce')
    
    df['authors_short'] = df['authors'].apply(lambda x: ', '.join(str(x).split('; ')[:3]) + ' et al.' if len(str(x).split('; ')) > 3 else x)
    
    important_keywords = ['artificial intelligence', 'machine learning', 'deep learning', 'neural network', 
                         'llm', 'large language model', 'chatgpt', 'transformer', 'natural language',
                         'computer vision', 'reinforcement learning', 'data mining', 'knowledge graph']
    
    df['keyword_score'] = df['title'].str.lower().apply(lambda x: sum(1 for kw in important_keywords if kw in str(x))) + \
                         df['abstract'].str.lower().apply(lambda x: sum(1 for kw in important_keywords if kw in str(x)))
    
    df['year_score'] = df['year'].apply(lambda x: x - 2022 if pd.notna(x) else 0)
    
    df['rank_score'] = df['keyword_score'] + df['year_score']
    
    top_papers = df.sort_values('rank_score', ascending=False).head(15)
    
    top_papers = top_papers.sort_values('year', ascending=False)
    
    result_df = top_papers[['title', 'authors_short', 'year', 'secondary_title', 'doi']].copy()
    result_df.columns = ['标题', '作者', '年份', '期刊', 'DOI']
    
    result_df['标题'] = result_df['标题'].apply(lambda x: str(x)[:80] + '...' if len(str(x)) > 80 else x)
    
    print("\n代表文献表（Top 15）:")
    print("-" * 120)
    header = f"{'序号':<4} {'年份':<6} {'作者':<35} {'期刊':<20} {'标题':<50}"
    print(header)
    print("-" * 120)
    
    papers_list = []
    for i, (_, row) in enumerate(result_df.iterrows(), 1):
        line = f"{i:<4} {int(row['年份']):<6} {str(row['作者'])[:32]:<35} {str(row['期刊'])[:18]:<20} {str(row['标题'])[:48]:<50}"
        print(line)
        papers_list.append({
            '序号': i,
            '标题': row['标题'],
            '作者': row['作者'],
            '年份': int(row['年份']),
            '期刊': row['期刊'],
            'DOI': row['DOI']
        })
    
    print("-" * 120)
    
    result_df.to_csv(OUTPUT_CSV, index=False, encoding='utf-8-sig')
    print("\n代表文献表已保存为CSV:", OUTPUT_CSV.name)
    
    with open(OUTPUT_TXT, 'w', encoding='utf-8') as f:
        f.write("=" * 80 + "\n")
        f.write("          人工智能领域代表文献表\n")
        f.write("=" * 80 + "\n\n")
        f.write(f"生成时间: 2026年\n")
        f.write(f"文献来源: 数据清洗后文献库\n")
        f.write(f"入选数量: {len(result_df)}篇\n")
        f.write("\n" + "-" * 80 + "\n")
        f.write(f"{'序号':<4} {'年份':<6} {'作者':<35} {'期刊':<20} {'标题'}\n")
        f.write("-" * 80 + "\n")
        for i, (_, row) in enumerate(result_df.iterrows(), 1):
            f.write(f"{i:<4} {int(row['年份']):<6} {str(row['作者'])[:32]:<35} {str(row['期刊'])[:18]:<20} {str(row['标题'])}\n")
        f.write("\n" + "=" * 80 + "\n")
    
    print("代表文献表已保存为TXT:", OUTPUT_TXT.name)
    
    print("\n文献年份分布:")
    year_dist = top_papers['year'].value_counts().sort_index()
    for year, count in year_dist.items():
        print(f"{int(year)}年: {count}篇")


if __name__ == "__main__":
    main()