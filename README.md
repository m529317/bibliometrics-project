# bibliometrics-project
# 文献计量学小组协作项目

## 研究主题
本项目旨在对**人工智能领域**的研究文献进行计量分析与知识图谱构建，通过文献计量学方法揭示该领域的研究趋势、核心作者、热点主题及知识结构。

## 整体流程
1. 检索文献 → 2. 筛选去重 → 3. 数据清洗 → 4. 数据分析 → 5. 可视化与论文撰写

## 人员分工
| 角色 | 姓名 | 职责 |
|------|------|------|
| 仓库管理员 | 刘伟丰 | GitHub仓库搭建、权限管理、README维护 |
| 检索专家 | 李丽 | 制定检索策略、导出原始文献 |
| 数据筛选员 | 王雪婷 | 文献筛选、去重、质量评价 |
| 数据工程师 | 徐国林 | 编写清洗脚本（Python） |
| 分析师 | 杜昊壅 | 数据分析、图表生成、报告撰写 |

## 数据来源
- **数据库**: Web of Science / Scopus
- **检索策略**: 见 `data/Literature Search String.docx`
- **原始数据**: `data/人工智能领域.ris`（RIS格式文献数据）
- **清洗后数据**: `data/cleaned_papers.ris`（可导入CiteSpace/VOSviewer）

## 项目结构
```
bibliometrics-project/
├── .github/workflows/     # GitHub Actions工作流
├── data/                  # 原始数据与清洗数据
│   ├── 人工智能领域.ris       # 原始RIS数据
│   ├── cleaned_papers.ris    # 清洗后RIS数据
│   ├── Literature Search String.docx  # 检索策略
│   └── 文献数据清洗说明.docx           # 清洗规范
├── outputs/               # 图表输出目录
│   ├── annual_publication_trend.png      # 年度发文趋势图
│   ├── author_collaboration_network.png  # 作者合作网络图
│   ├── keyword_cooccurrence_network.png  # 关键词共现网络图
│   └── representative_papers.txt         # 代表文献表
├── src/                   # 源代码
│   ├── 01_data_cleaning.py      # 数据清洗模块
│   ├── 02_trend_analysis.py     # 趋势分析模块
│   ├── 03_author_analysis.py    # 作者分析模块
│   ├── 04_keyword_network.py    # 关键词网络模块
│   └── 05_representative_papers.py  # 代表文献模块
├── paper/                 # 课程论文
│   └── mini_review_template.md  # IMRaD格式论文模板
├── presentation/          # 答辩材料
├── reports/               # 报告文档
│   └── analysis_summary.md     # 分析总结报告
├── docs/                  # 文档说明
│   └── ai_usage.md        # AI使用说明
├── reflection/            # 个人反思记录
│   └── team_reflection.md     # 团队分工与反思
├── config.py             # 项目参数配置
├── requirements.txt      # Python依赖声明
├── CODE_WIKI.md          # 技术文档
├── .gitignore            # Git忽略文件
├── LICENSE               # 许可证
└── README.md             # 项目说明
```

## 运行命令

### 环境配置
```bash
# 方式1：使用requirements.txt安装（推荐）
pip install -r requirements.txt

# 方式2：手动安装依赖
pip install pandas rispy matplotlib seaborn networkx
```

### 完整执行流程
```bash
# 1. 数据清洗
python src/01_data_cleaning.py

# 2. 趋势分析（生成年度发文趋势图）
python src/02_trend_analysis.py

# 3. 作者分析（生成作者合作网络图）
python src/03_author_analysis.py

# 4. 关键词网络（生成关键词共现网络图）
python src/04_keyword_network.py

# 5. 代表文献（生成代表文献表）
python src/05_representative_papers.py
```

## 输出目录说明

| 目录/文件 | 内容 | 说明 |
|-----------|------|------|
| `data/` | RIS文件、清洗说明、检索策略 | 原始数据与处理后数据 |
| `outputs/` | PNG图表、TXT表格 | 可视化结果输出 |
| `src/` | Python脚本 | 数据分析源代码 |
| `paper/` | 课程论文终稿 | mini review格式（IMRaD） |
| `presentation/` | 答辩PPT/PDF | 演示材料 |
| `reports/` | 报告文档 | 分析总结报告 |
| `docs/` | 文档说明 | AI使用说明等 |
| `reflection/` | 个人反思 | 分工说明或反思记录 |
| `config.py` | 参数配置文件 | 所有分析参数集中管理 |
| `requirements.txt` | Python依赖声明 | 用于环境复现 |

## 协作规范
- 分支命名：`feature/任务名`、`fix/问题描述`
- Commit消息格式：`[模块] 简短描述`
- 重要成果请通过Pull Request合并到main分支

## 许可证
MIT License