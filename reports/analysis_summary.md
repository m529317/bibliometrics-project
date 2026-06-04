# 分析总结报告

## 项目概述
本项目对人工智能领域的研究文献进行了文献计量分析，包括年度发文趋势、作者合作网络、关键词共现网络和代表文献筛选。

## 数据来源
- 数据库：Web of Science / Scopus
- 检索时间：2023年1月-2026年6月
- 文献数：请运行 `src/01_data_cleaning.py` 查看具体数量

## 分析内容

### 1. 数据清洗
- 去重处理：基于标题+作者+年份
- 年份过滤：保留2023年及以后文献
- 完整性检查：确保关键字段完整

### 2. 年度发文趋势
- 统计各年度文献数量
- 生成柱状图可视化
- 输出文件：`outputs/annual_publication_trend.png`

### 3. 作者合作网络
- 筛选高产作者（发文≥2篇）
- 构建合作网络
- 生成网络可视化图
- 输出文件：`outputs/author_collaboration_network.png`

### 4. 关键词共现网络
- 从摘要提取关键词
- 构建共现网络
- 生成网络可视化图
- 输出文件：`outputs/keyword_cooccurrence_network.png`

### 5. 代表文献筛选
- 基于关键词匹配和年份评分
- 筛选Top15代表文献
- 输出文件：`outputs/representative_papers.txt`

## 运行说明
1. 安装依赖：`pip install -r requirements.txt`
2. 运行完整流程：按顺序执行 `src/` 目录下的Python脚本

## 联系方式
如有问题，请联系项目团队成员。
