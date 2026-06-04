# Bibliometrics Project Code Wiki

> 文献计量学小组协作项目 - 完整技术文档

---

## 目录
1. [项目概述](#1-项目概述)
2. [项目架构](#2-项目架构)
3. [核心模块详解](#3-核心模块详解)
4. [关键函数说明](#4-关键函数说明)
5. [依赖关系](#5-依赖关系)
6. [项目运行指南](#6-项目运行指南)
7. [数据流程](#7-数据流程)

---

## 1. 项目概述

### 1.1 项目简介
本项目是一个人工智能领域研究文献计量与知识图谱分析的协作项目，通过Python自动化工具实现文献数据清洗、趋势分析、作者合作网络构建、关键词共现分析等功能。

### 1.2 研究目标
- 人工智能领域文献计量分析
- 知识图谱构建与可视化
- 3图1表产出（年度发文趋势、作者合作网络、关键词共现网络、代表文献表）

### 1.3 人员分工
| 人员 | 职责 |
|------|------|
| 刘伟丰 | GitHub仓库搭建、权限管理、README维护 |
| 李丽 | 制定检索策略、导出原始文献 |
| 王雪婷 | 文献筛选、去重、质量评价 |
| 徐国林 | 编写清洗脚本（Python/R） |
| 杜昊壅 | 数据分析、图表生成、报告撰写 |

---

## 2. 项目架构

### 2.1 目录结构
```
bibliometrics-project-main/
├── .github/workflows/              # GitHub Actions工作流
├── 3图1表/                         # 可视化结果输出目录
│   ├── annual_publication_trend.png
│   ├── author_collaboration_network.png
│   ├── keyword_cooccurrence_network.png
│   └── representative_papers.txt
├── 01_data_cleaning.py             # 数据清洗模块
├── 02_trend_analysis.py            # 趋势分析模块
├── 03_author_analysis.py           # 作者分析模块
├── 04_keyword_network.py           # 关键词网络模块
├── 05_representative_papers.py     # 代表文献模块
├── 人工智能领域.ris                # 原始文献数据
├── cleaned_papers.ris              # 清洗后RIS格式数据
├── cleaned_papers.pkl              # 清洗后Pickle格式数据
├── Literature Search String.docx   # 检索策略文档
└── 文献数据清洗说明.docx           # 数据清洗规范
```

### 2.2 模块职责划分
| 模块 | 文件 | 主要职责 |
|------|------|----------|
| 数据清洗 | [01_data_cleaning.py](file:///d:\文献计量\bibliometrics-project-main\bibliometrics-project-main\01_data_cleaning.py) | 读取RIS数据、去重、过滤、格式清理 |
| 趋势分析 | [02_trend_analysis.py](file:///d:\文献计量\bibliometrics-project-main\bibliometrics-project-main\02_trend_analysis.py) | 年度发文量统计与可视化 |
| 作者分析 | [03_author_analysis.py](file:///d:\文献计量\bibliometrics-project-main\bibliometrics-project-main\03_author_analysis.py) | 作者合作网络构建与分析 |
| 关键词网络 | [04_keyword_network.py](file:///d:\文献计量\bibliometrics-project-main\bibliometrics-project-main\04_keyword_network.py) | 关键词共现网络分析 |
| 代表文献 | [05_representative_papers.py](file:///d:\文献计量\bibliometrics-project-main\bibliometrics-project-main\05_representative_papers.py) | 代表性文献筛选与导出 |

---

## 3. 核心模块详解

### 3.1 数据清洗模块 ([01_data_cleaning.py](file:///d:\文献计量\bibliometrics-project-main\bibliometrics-project-main\01_data_cleaning.py))

#### 功能概述
负责原始RIS文献数据的读取、清洗、去重和格式化，生成可用于后续分析的标准数据格式。

#### 核心处理步骤
1. **数据读取**：使用`rispy`库读取RIS格式文件
2. **字段自动检测**：自动识别RIS标准字段（title、authors、year、abstract）
3. **去重处理**：基于标题+作者+年份组合去重
4. **年份过滤**：保留2023年以后的文献
5. **完整性检查**：确保关键字段不缺失
6. **格式清理**：统一文本格式，去除无效字符
7. **数据保存**：同时输出Pickle和RIS两种格式

#### 清洗规则
| 规则 | 说明 |
|------|------|
| 规则1 | 去重：标题+作者+年份组合唯一 |
| 规则3 | 无关文献剔除（预留接口） |
| 规则4 | 格式统一清理 |
| 规则5 | 关键字段完整性检查 |
| 规则6 | 年份过滤：≥2023年 |

---

### 3.2 趋势分析模块 ([02_trend_analysis.py](file:///d:\文献计量\bibliometrics-project-main\bibliometrics-project-main\02_trend_analysis.py))

#### 功能概述
统计年度发文量并生成可视化趋势图。

#### 核心功能
- 按年份分组统计文献数量
- 使用Seaborn绘制柱状图
- 支持中文显示（使用SimHei字体）
- 输出PNG格式高分辨率图片

#### 输出文件
- `annual_publication_trend.png` - 年度发文趋势图

---

### 3.3 作者分析模块 ([03_author_analysis.py](file:///d:\文献计量\bibliometrics-project-main\bibliometrics-project-main\03_author_analysis.py))

#### 功能概述
构建作者合作网络并进行可视化分析。

#### 核心功能
- 统计作者发文量
- 筛选高产作者（发文≥2篇）
- 构建作者合作网络（NetworkX）
- 可视化展示网络结构
- 输出Top10高产作者列表

#### 网络构建算法
1. 遍历所有文献的作者列表
2. 生成作者两两合作关系
3. 使用NetworkX构建无向加权图
4. Spring布局算法可视化

#### 输出文件
- `author_collaboration_network.png` - 作者合作网络图

---

### 3.4 关键词网络模块 ([04_keyword_network.py](file:///d:\文献计量\bibliometrics-project-main\bibliometrics-project-main\04_keyword_network.py))

#### 功能概述
从摘要中提取关键词，构建关键词共现网络。

#### 核心功能
- 从摘要文本自动提取关键词
- 停用词过滤
- 统计关键词频次
- 构建关键词共现网络
- 输出Top15高频关键词

#### 关键词提取规则
- 长度≥3个字符
- 不在停用词表中
- 每篇文献提取Top8关键词
- 筛选出现≥3次的关键词

#### 输出文件
- `keyword_cooccurrence_network.png` - 关键词共现网络图

---

### 3.5 代表文献模块 ([05_representative_papers.py](file:///d:\文献计量\bibliometrics-project-main\bibliometrics-project-main\05_representative_papers.py))

#### 功能概述
基于关键词匹配和年份评分筛选代表性文献。

#### 评分算法
```
rank_score = keyword_score + year_score
```
- `keyword_score`：标题和摘要中重要关键词的匹配次数
- `year_score`：(年份 - 2022)，越新文献得分越高

#### 重要关键词列表
- artificial intelligence, machine learning, deep learning
- neural network, llm, large language model
- chatgpt, transformer, natural language
- computer vision, reinforcement learning
- data mining, knowledge graph

#### 输出文件
- `representative_papers.txt` - 代表文献表（TXT格式）
- `representative_papers.csv` - 代表文献表（CSV格式）

---

## 4. 关键函数说明

### 4.1 数据清洗模块

#### clean_text(text)
**位置**: [01_data_cleaning.py#L13-L37](file:///d:\文献计量\bibliometrics-project-main\bibliometrics-project-main\01_data_cleaning.py#L13-L37)

**功能**: 通用文本清理函数

**参数**: 
- `text`: 待清理的文本（可为字符串、列表或元组）

**返回值**: 清理后的文本

**处理逻辑**:
1. 处理空值和列表/元组类型
2. 合并列表为分号分隔字符串
3. 去除多余空白
4. 移除URL
5. 保留中英文及常用标点

---

#### dataframe_to_ris_entries(df)
**位置**: [01_data_cleaning.py#L40-L64](file:///d:\文献计量\bibliometrics-project-main\bibliometrics-project-main\01_data_cleaning.py#L40-L64)

**功能**: 将DataFrame转换为rispy标准格式

**参数**:
- `df`: 包含文献数据的DataFrame

**返回值**: rispy格式的条目列表

---

### 4.2 关键词网络模块

#### extract_keywords(text, top_n=10)
**位置**: [04_keyword_network.py#L15-L44](file:///d:\文献计量\bibliometrics-project-main\bibliometrics-project-main\04_keyword_network.py#L15-L44)

**功能**: 从文本中提取高频关键词

**参数**:
- `text`: 输入文本（通常是摘要）
- `top_n`: 返回关键词数量，默认10

**返回值**: 关键词列表

---

## 5. 依赖关系

### 5.1 核心依赖库

| 库名 | 版本 | 用途 |
|------|------|------|
| pandas | - | 数据处理与分析 |
| rispy | - | RIS格式文件读写 |
| matplotlib | - | 数据可视化 |
| seaborn | - | 统计绘图 |
| networkx | - | 网络分析与构建 |

### 5.2 模块依赖关系
```
01_data_cleaning.py 
    ↓ (产出 cleaned_papers.pkl)
    ├→ 02_trend_analysis.py
    ├→ 03_author_analysis.py
    ├→ 04_keyword_network.py
    └→ 05_representative_papers.py
```

### 5.3 系统依赖
- Python 3.x
- SimHei字体（用于中文显示）

---

## 6. 项目运行指南

### 6.1 环境配置

#### 步骤1：克隆仓库
```bash
git clone https://github.com/m529317/bibliometrics-project.git
cd bibliometrics-project
```

#### 步骤2：安装依赖
```bash
pip install pandas rispy matplotlib seaborn networkx
```

#### 步骤3：准备数据
确保原始数据文件 `人工智能领域.ris` 存在于项目根目录。

### 6.2 运行流程

#### 完整执行顺序（推荐）
```bash
# 1. 数据清洗
python 01_data_cleaning.py

# 2. 趋势分析
python 02_trend_analysis.py

# 3. 作者分析
python 03_author_analysis.py

# 4. 关键词网络
python 04_keyword_network.py

# 5. 代表文献
python 05_representative_papers.py
```

### 6.3 输出结果汇总
运行完成后，将生成以下文件：

| 文件 | 说明 |
|------|------|
| cleaned_papers.pkl | 清洗后的Python数据格式 |
| cleaned_papers.ris | 清洗后的RIS格式（可导入CiteSpace） |
| annual_publication_trend.png | 年度发文趋势图 |
| author_collaboration_network.png | 作者合作网络图 |
| keyword_cooccurrence_network.png | 关键词共现网络图 |
| representative_papers.txt | 代表文献表（TXT） |
| representative_papers.csv | 代表文献表（CSV） |

---

## 7. 数据流程

```
┌─────────────────────┐
│ 人工智能领域.ris     │ 原始RIS数据
└──────────┬──────────┘
           │
           ▼
┌─────────────────────────────────┐
│ 01_data_cleaning.py             │
│  - 读取RIS                      │
│  - 去重 (标题+作者+年份)         │
│  - 年份过滤 (≥2023)             │
│  - 完整性检查                   │
│  - 格式清理                     │
└──────────┬──────────────────────┘
           │
           ▼
┌─────────────────────────────────┐
│ cleaned_papers.pkl              │ 中间数据
│ cleaned_papers.ris              │
└──────────┬──────────────────────┘
           │
    ┌──────┴──────┬───────────────┬───────────────┬───────────────┐
    │             │               │               │               │
    ▼             ▼               ▼               ▼               ▼
┌─────────┐ ┌─────────┐    ┌─────────┐   ┌─────────┐    ┌─────────┐
│02_trend │ │03_author│    │04_keyword│  │05_rep   │    │ 3图1表/ │
│_analysis│ │_analysis│    │_network  │  │_papers  │    │ 输出目录 │
└────┬────┘ └────┬────┘    └────┬────┘   └────┬────┘    └─────────┘
     │           │              │             │
     ▼           ▼              ▼             ▼
┌─────────┐ ┌─────────┐    ┌─────────┐   ┌─────────┐
│年度发文 │ │作者合作 │    │关键词共 │   │代表文献 │
│趋势图   │ │网络图   │    │现网络   │   │表       │
└─────────┘ └─────────┘    └─────────┘   └─────────┘
```

---

## 附录

### A. 协作规范
- **分支命名**: `feature/任务名`、`fix/问题描述`
- **Commit消息**: `[模块] 简短描述`
- **合并策略**: 重要成果通过Pull Request合并到main分支

### B. 常见问题
1. **中文显示方框**: 确保系统已安装SimHei字体
2. **RIS读取失败**: 检查RIS文件编码是否为UTF-8
3. **模块导入错误**: 确保所有依赖库已正确安装

### C. 参考文献
- [RIS格式规范](https://en.wikipedia.org/wiki/RIS_(file_format))
- [NetworkX文档](https://networkx.org/documentation/)
