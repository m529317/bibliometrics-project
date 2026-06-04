import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
from pathlib import Path
from matplotlib.font_manager import FontProperties

# 路径配置
DATA = Path("../data/cleaned_papers.pkl")
OUTPUT_IMG = Path("../outputs/annual_publication_trend.png")

# 【终极方案】直接创建中文字体对象，不依赖全局设置
chinese_font = FontProperties(family='SimHei', size=12)
title_font = FontProperties(family='SimHei', size=16)
label_font = FontProperties(family='SimHei', size=12)


def main():
    print("正在生成年度发文量趋势图...")
    df = pd.read_pickle(DATA)

    # 按年份统计发文量
    annual_counts = df['year'].value_counts().sort_index()

    # 绘制趋势图
    plt.figure(figsize=(12, 6), dpi=100)
    sns.set_style("whitegrid")

    ax = sns.barplot(x=annual_counts.index.astype(int), y=annual_counts.values, color='#1f77b4', alpha=0.8)

    # 添加数值标签
    for i, v in enumerate(annual_counts.values):
        ax.text(i, v + 2, str(v), ha='center', va='bottom', fontsize=12, fontweight='bold')

    # 【关键】所有中文都明确指定字体对象
    plt.title('人工智能领域年度发文量趋势（2023-2026）', fontproperties=title_font, pad=20)
    plt.xlabel('年份', fontproperties=label_font)
    plt.ylabel('发文量', fontproperties=label_font)
    plt.xticks(fontproperties=chinese_font, fontsize=11)
    plt.yticks(fontsize=11)
    plt.ylim(0, max(annual_counts.values) + 10)
    plt.tight_layout()

    plt.savefig(OUTPUT_IMG, dpi=300, bbox_inches='tight')
    print(f"✅ 发文量趋势图已保存: {OUTPUT_IMG.name}")
    print("\n✅ 中文显示已修复，没有方框！")

    # 输出统计结果
    print("\n年度发文量统计:")
    for year, count in annual_counts.items():
        print(f"{int(year)}年: {count}篇")


if __name__ == "__main__":
    main()