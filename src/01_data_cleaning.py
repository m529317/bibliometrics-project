import pandas as pd
import rispy
import re
from pathlib import Path
from rispy import dump

# 路径配置
RAW_DATA = Path("../data/人工智能领域.ris")
OUTPUT_PKL = Path("../data/cleaned_papers.pkl")
OUTPUT_RIS = Path("../data/cleaned_papers.ris")


def clean_text(text):
    """通用文本清理函数（极简版，无版本依赖）"""
    if pd.isna(text):
        return None

    # 只处理最常见的列表和元组类型（rispy只会生成这两种）
    if isinstance(text, (list, tuple)):
        if len(text) == 0:
            return None
        # 过滤空值并转换为字符串
        parts = [str(t).strip() for t in text if pd.notna(t) and str(t).strip()]
        if not parts:
            return None
        return '; '.join(parts)

    # 处理普通字符串
    text = str(text).strip()
    if not text:
        return None

    # 格式清理
    text = re.sub(r'\s+', ' ', text)
    text = re.sub(r'https?://\S+|www\.\S+', '', text)
    text = re.sub(r'[^\u4e00-\u9fa5a-zA-Z0-9\s.,;:!?()[]{}"\'-]', '', text)
    return text


def dataframe_to_ris_entries(df):
    """将DataFrame转换为rispy标准格式"""
    entries = []
    for _, row in df.iterrows():
        entry = {}
        for k, v in row.items():
            # 跳过辅助字段
            if k in ['authors_std', 'keywords_std']:
                continue
            # 跳过空值
            if pd.isna(v):
                continue
            # 处理列表类型
            if isinstance(v, (list, tuple)):
                if len(v) == 0:
                    continue
                # 作者字段必须保留列表格式
                if k == 'authors' or k == 'AU':
                    entry[k] = [str(a).strip() for a in v if pd.notna(a) and str(a).strip()]
                else:
                    entry[k] = '; '.join([str(t).strip() for t in v if pd.notna(t) and str(t).strip()])
            else:
                entry[k] = v
        entries.append(entry)
    return entries


def main():
    print("=" * 50)
    print("文献数据清洗脚本（仅输出RIS格式）")
    print("严格匹配《文献数据清洗说明.docx》")
    print("=" * 50)

    # 1. 读取原始RIS数据
    print("\n1. 读取原始数据...")
    with open(RAW_DATA, 'r', encoding='utf-8') as f:
        entries = rispy.load(f)
    df = pd.DataFrame(entries)
    original_count = len(df)
    print(f"原始文献数量: {original_count} 篇")

    # 自动检测RIS标准字段
    print("\n正在自动检测字段名...")
    field_mapping = {
        'title': ['title', 'TI'],
        'authors': ['authors', 'AU'],
        'year': ['year', 'PY'],
        'abstract': ['abstract', 'AB']
    }

    actual_fields = {}
    for standard_name, possible_names in field_mapping.items():
        for name in possible_names:
            if name in df.columns:
                actual_fields[standard_name] = name
                print(f"✓ 找到 {standard_name}: {name}")
                break

    # 转换列表字段为字符串用于去重
    for col in df.columns:
        if df[col].apply(lambda x: isinstance(x, (list, tuple))).any():
            df[col] = df[col].apply(lambda x: '; '.join([str(i) for i in x]) if isinstance(x, (list, tuple)) else x)

    # 2. 去重处理（规则1：标题+作者+年份）
    print("\n2. 执行去重处理...")
    deduplicate_cols = [actual_fields['title'], actual_fields['authors'], actual_fields['year']]
    df = df.drop_duplicates(subset=deduplicate_cols, keep='first')
    deduplicated_count = len(df)
    print(f"剔除重复: {original_count - deduplicated_count} 篇")

    # 3. 年份过滤（规则6：仅保留2023年以后）
    print("\n3. 执行年份过滤...")
    df[actual_fields['year']] = pd.to_numeric(df[actual_fields['year']], errors='coerce')
    df = df[df[actual_fields['year']] >= 2023]
    year_filtered_count = len(df)
    print(f"剔除2023年前: {deduplicated_count - year_filtered_count} 篇")

    # 4. 完整性检查（规则5：关键字段完整）
    print("\n4. 执行完整性检查...")
    required_fields = [actual_fields['title'], actual_fields['authors'], actual_fields['year']]
    df = df.dropna(subset=required_fields)
    df = df[~df[actual_fields['abstract']].isna()]
    complete_count = len(df)
    print(f"剔除缺失字段: {year_filtered_count - complete_count} 篇")

    # 5. 格式清理（规则4：统一格式）
    print("\n5. 执行格式清理...")
    for col in df.columns:
        df[col] = df[col].apply(clean_text)

    # 6. 无关文献剔除（规则3，预留接口）
    # 如需添加，取消注释并修改关键词：
    # irrelevant = ['综述', '书评', '会议摘要']
    # df = df[~df[actual_fields['title']].str.contains('|'.join(irrelevant), case=False, na=False)]
    final_count = len(df)
    print(f"\n剔除无关文献: {complete_count - final_count} 篇")

    # 最终统计
    print("\n" + "=" * 50)
    print("✅ 清洗完成！最终结果：")
    print("=" * 50)
    print(f"原始文献: {original_count} 篇")
    print(f"最终有效文献: {final_count} 篇")
    print("=" * 50)

    # 保存结果
    print("\n正在保存文件...")

    # 保存Python专用格式
    df.to_pickle(OUTPUT_PKL)
    print(f"✓ PKL格式: {OUTPUT_PKL.name}")

    # 保存标准RIS格式
    ris_entries = dataframe_to_ris_entries(df)
    with open(OUTPUT_RIS, 'w', encoding='utf-8') as f:
        dump(ris_entries, f)
    print(f"✓ RIS格式: {OUTPUT_RIS.name}（可直接导入CiteSpace）")
    print("\n🎉 所有文件保存成功！")


if __name__ == "__main__":
    main()