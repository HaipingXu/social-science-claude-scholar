# Claude Scholar 配置

## 项目概述

**Claude Scholar** - 面向学术研究和软件开发的个人 Claude Code 配置系统

**Mission**: 覆盖完整的学术研究生命周期（从构思到发表）和软件开发工作流，同时提供插件开发和项目管理能力。

---

## 用户背景

### 学术背景
- **学历**: 社会科学 PhD（政治学 / 经济学）
- **研究领域**: 比较政治学、政治经济学、政治制度、公共经济学、经济史
- **研究方法**: 因果推断计量（DID、IV、RDD、合成控制）、文本即数据/NLP、应用机器学习、应用博弈论、历史比较定性方法
- **投稿目标**:
  - 政治学：APSR, AJPS, JOP, Comparative Political Studies (CPS), International Organization (IO), World Politics
  - 经济学：AER, QJE, JPE, REStud, Econometrica, Journal of Public Economics (JPubE)
  - 跨学科：PNAS, Journal of Conflict Resolution, Political Analysis
- **关注点**: 可信因果识别、严谨实证分析、清晰理论动机、精确学术写作

### 技术栈偏好

**主要工具**:
- **写作**: LaTeX（主力）、Overleaf 用于协作
- **统计分析**: Stata（当前主力）→ Python（过渡中）
- **包管理**: `uv` - 现代化 Python 包管理器

**Python 生态（从 Stata 过渡）**:
- **因果推断**: `pyfixest`（主力面板回归）、`statsmodels`, `linearmodels`, `econml`
- **数据处理**: `pandas`, `numpy`, `pyarrow`
- **NLP / 文本数据**: `transformers`, `gensim`, `spacy`, `bertopic`
- **可视化**: `plotnine`（ggplot2 等价）、`matplotlib`, `seaborn`
- **Stata 桥接**: `pystata`, `stata_setup`

**Git 规范**:
- **提交规范**: Conventional Commits
  ```
  Type: feat, fix, docs, style, refactor, perf, test, chore
  Scope: data, analysis, paper, config, utils, workflow
  ```
- **分支策略**: master/develop/feature/bugfix/hotfix/release
- **合并策略**: 功能分支用 rebase 同步，用 merge --no-ff 合并

---

## 全局配置

### 语言设置
- **用中文回答用户**
- 专业术语保持英文（如 NeurIPS, RLHF, TDD, Git, DID, IV, RDD）
- 不翻译特定名词或名称

### 工作目录规范
- 计划文档：`/plan` 文件夹
- 临时文件：`/temp` 文件夹
- 文件夹不存在时自动创建

### 任务执行原则
- 复杂任务先交流方案，再拆解实施
- 实施后进行验证测试
- 做好备份，不影响现有功能
- 完成后及时清理临时文件
- **操作日志**：涉及 3 次以上工具调用或文件修改的会话，维护运行中的操作日志

### 操作日志格式

日志位置：`~/.claude/session-logs/YYYY-MM-DD.md`，不存在时自动创建目录和文件，会话中持续追加。

```markdown
## 会话：YYYY-MM-DD HH:MM

### [HH:MM] <操作摘要>
- **工具**: Write / Edit / Bash / WebFetch 等
- **目标**: `文件路径` 或 `执行的命令`
- **结果**: 成功 / 失败 / 部分完成
- **备注**: 重要上下文或决策依据

### [HH:MM] <下一步操作>
...
```

记录：文件创建、文件编辑、有副作用的 bash 命令、关键决策。跳过：只读文件读取、纯信息性网页抓取。

### 工作风格
- **任务管理**: 使用 TodoWrite 跟踪进度，复杂任务先规划再执行，优先使用已有 skills
- **沟通方式**: 不确定时主动询问，重要操作前先确认，遵循 hook 强制流程
- **代码风格**: Python 遵循 PEP 8，注释使用中文，标识符使用英文

---

## 核心工作流

### 研究生命周期（7 阶段）

```
构思 → 文献综述 → 数据与实证 → 论文写作 → 自审 → 投稿/Rebuttal → 录用后处理
```

| 阶段 | 核心工具 | 命令 |
|------|---------|------|
| 1. 研究构思 | `research-ideation` skill + `interview-me` skill + `gpt-researcher` skill + Zotero MCP | `/research-init`, `/zotero-review`, `/zotero-notes` |
| 2. 文献综述 | `daily-paper-generator` skill + `gpt-researcher` skill + Zotero MCP | `/zotero-notes`, `/zotero-review` |
| 3. 数据与实证分析 | `data-analysis` skill + `results-analysis` skill + `data-analyst` agent | `/analyze-results` |
| 4. 论文写作 | `social-science-paper-writing` skill + `paper-miner` agent | - |
| 5. 论文自审 | `paper-self-review` skill + `devils-advocate` skill + `review-paper` skill | - |
| 6. 投稿与 Rebuttal | `review-response` skill + `rebuttal-writer` agent | `/rebuttal` |
| 7. 录用后处理 | `post-acceptance` skill | `/presentation`, `/poster`, `/promote` |

### 支撑工作流

- **自动化执行**: 7 个 Hook 在会话各阶段自动触发（技能评估、环境初始化、工作总结、安全检查、上下文压缩保存/恢复）
- **上下文持续性**: `pre-compact.py` 在压缩前保存会话状态；`post-compact-restore.py` 在恢复后重建上下文——计划和决策跨压缩边界存活
- **质量门控**: 所有论文/分析工作 0-100 评分；commit 需 ≥80，投稿需 ≥90（`quality-gates.md` 规则）
- **对抗式 QA**: Critic+Fixer 循环（最多 5 轮）用于论文和分析——`orchestrator-protocol.md` 规则
- **承包商模式**: 计划 → 审批 → 自主执行循环；复杂任务用 MUST/SHOULD/MAY 需求规格
- **单一权威源**: `.tex` 是论文权威源，Stata `.do` 是 Python 过渡期的权威源（`single-source-of-truth.md` 规则）
- **持续学习**: `[LEARN:category]` 标签记录跨会话经验到 MEMORY.md（`learn.md` 规则）
- **Zotero 集成**: 论文自动导入、集合管理、全文阅读和引用导出
- **每日论文追踪**: `daily-paper-generator` 监控 NBER WP + arXiv econ + 顶刊 TOC
- **研究版本控制**: Git + DVC 管理数据/分析脚本/论文
- **可复现包准备**: `replication-package` skill 按 AER/APSR 标准准备
- **操作日志**: 重要会话记录至 `~/.claude/session-logs/YYYY-MM-DD.md`
- **技能进化**: `skill-development` → `skill-quality-reviewer` → `skill-improver` 三步改进循环

---

## 技能目录（42 skills）

### 🔬 研究与分析 (10 skills)

- **research-ideation**: 研究构思启动（5W1H、Gap 分析、研究问题制定、Zotero 集成）
- **interview-me**: Socratic 访谈式研究想法形式化——对话式提问，产出完整 Research Specification Document（含假说与识别策略）
- **results-analysis**: 实证结果分析（识别假设检验、回归表格、DID/IV/RDD 可视化、稳健性检验）
- **data-analysis**: 端到端数据分析流水线——EDA → 回归 → 出版级表格/图形，Python（pyfixest）或 Stata；内含 Stata→Python 对照翻译参考
- **causal-inference-analysis**: DID、IV、RDD、合成控制的 Python/Stata 实现（代码模板、假设检验、表格与图形生成）
- **citation-verification**: 引文验证（多层：格式→API→信息→内容）
- **daily-paper-generator**: 每日论文追踪（NBER WP + arXiv + 经济学/政治学顶刊 TOC，双语摘要）
- **gpt-researcher**: 自主网络背景调研——灰色文献、政策文件、制度背景、案例历史；本地 PDF RAG
- **devils-advocate**: 对抗式挑战——5-7 个针对识别策略/机制/测量/文献的具体攻击；按严重度排序，附预防建议
- **review-paper**: 完整审稿报告模拟——6 维度 1-5 分评分 + 致命反对意见 + 录用/拒稿建议；像 AER/APSR 审稿人一样思考

### 📝 论文写作与发表 (11 skills)

- **social-science-paper-writing**: 双轨制论文写作——经济学轨（AER/QJE/JPE：引言→数据→实证策略→结果→稳健性）+ 政治学轨（APSR/JOP：引言→理论/假说→研究设计→实证分析→讨论）；各节模板、期刊规范、内置去 AI 写作痕迹
- **ml-paper-writing**: NLP/应用 ML 论文写作（保留用于 NeurIPS/ICML/ACL 等）
- **writing-anti-ai**: 去除 AI 写作痕迹，支持中英文双语
- **paper-self-review**: **0-100 量化评分**的论文质量审计——8 个维度含扣分量表；区分阻塞问题（blocking）与警告；附 Referee Objections；给出投稿准备度判定
- **academic-paper-reviewer**: 多视角同行评审模拟——5 位独立审稿人（主编 + 方法论 + 领域专家 + 视角审查 + 魔鬼代言人）；0-100 质量评分；5 种模式
- **review-response**: 系统化 rebuttal 写作
- **post-acceptance**: 录用后处理（演讲、海报、推广）
- **doc-coauthoring**: 文档协作工作流
- **latex-conference-template-organizer**: LaTeX 期刊/会议模板整理

### 💻 开发工作流 (7 skills)

- **daily-coding**: 日常编码检查清单（自动触发）
- **git-workflow**: 研究项目版本控制——Git + DVC；研究专用提交规范（data/analysis/results/paper）；DVC 配置；研究 .gitignore
- **replication-package**: AER/APSR/AJPS 可复现包准备——README 模板、主脚本、数据 README、代码质量清单、openICPSR/Dataverse 上传
- **code-review-excellence**: 代码审查最佳实践（数据处理、计量分析脚本）
- **bug-detective**: 调试和错误排查（Python, Stata, Bash/Zsh）
- **architecture-design**: 数据分析项目代码框架和设计模式
- **verification-loop**: 验证循环和测试（回归结果核验、可复现性检查）

### 🔌 插件开发 (8 skills)

- **skill-development**: Skill 开发指南
- **skill-improver**: Skill 改进工具
- **skill-quality-reviewer**: Skill 质量审查
- **command-development**: Slash 命令开发
- **command-name**: 插件结构指南
- **agent-identifier**: Agent 开发配置
- **hook-development**: Hook 开发和事件处理
- **mcp-integration**: MCP 服务器集成

### 🧪 工具与实用 (4 skills)

- **planning-with-files**: 使用 Markdown 文件进行规划和进度跟踪
- **uv-package-manager**: uv 包管理器使用
- **webapp-testing**: 本地 Web 应用测试
- **kaggle-learner**: Kaggle 竞赛学习

### 🎨 网页设计 (3 skills)

- **frontend-design**: 创建独特、生产级的前端界面
- **ui-ux-pro-max**: UI/UX 设计智能（50+ 风格、97 色板、57 字体配对、9 技术栈）
- **web-design-reviewer**: 网站设计视觉检查，识别并修复响应式、可访问性、布局问题

---

## 命令（50+ Commands）

### 研究工作流命令

| 命令 | 功能 |
|------|------|
| `/research-init` | 启动 Zotero 集成研究构思工作流 |
| `/zotero-review` | 从 Zotero 集合读取论文，生成结构化文献综述 |
| `/zotero-notes` | 批量阅读 Zotero 论文，生成结构化阅读笔记 |
| `/analyze-results` | 分析实证结果（因果推断检验、DID/IV/RDD 可视化） |
| `/rebuttal` | 生成系统化 rebuttal 文档 |
| `/presentation` | 创建会议演讲大纲 |
| `/poster` | 生成学术海报设计方案 |
| `/promote` | 生成推广内容（Twitter、LinkedIn、博客） |

### 开发工作流命令

| 命令 | 功能 |
|------|------|
| `/plan` | 创建实施计划 |
| `/commit` | 提交代码（遵循 Conventional Commits） |
| `/update-github` | 提交并推送到 GitHub |
| `/update-readme` | 更新 README 文档 |
| `/code-review` | 代码审查 |
| `/tdd` | 测试驱动开发工作流 |
| `/build-fix` | 修复构建错误 |
| `/verify` | 验证更改 |
| `/checkpoint` | 创建检查点 |
| `/refactor-clean` | 重构和清理 |
| `/learn` | 从代码中提取可重用模式 |
| `/create_project` | 创建新项目 |
| `/update-memory` | 检查并更新 CLAUDE.md 记忆 |

### SuperClaude 命令集 (`/sc`)

- `/sc agent` - Agent 调度
- `/sc analyze` - 代码分析
- `/sc brainstorm` - 交互式头脑风暴
- `/sc build` - 构建项目
- `/sc business-panel` - 业务面板
- `/sc cleanup` - 代码清理
- `/sc design` - 系统设计
- `/sc document` - 生成文档
- `/sc estimate` - 工作量估算
- `/sc explain` - 代码解释
- `/sc git` - Git 操作
- `/sc help` - 帮助信息
- `/sc implement` - 功能实现
- `/sc improve` - 代码改进
- `/sc index` - 项目索引
- `/sc index-repo` - 仓库索引
- `/sc load` - 加载上下文
- `/sc pm` - 包管理器操作
- `/sc recommend` - 推荐方案
- `/sc reflect` - 反思总结
- `/sc research` - 技术调研
- `/sc save` - 保存上下文
- `/sc select-tool` - 工具选择
- `/sc spawn` - 生成子任务
- `/sc spec-panel` - 规格面板
- `/sc task` - 任务管理
- `/sc test` - 测试执行
- `/sc troubleshoot` - 问题排查
- `/sc workflow` - 工作流管理

---

## 代理（14 Agents）

### 研究工作流代理

- **literature-reviewer** - 文献搜索、分类和趋势分析（Zotero MCP 集成）
- **data-analyst** - 自动化数据分析和可视化
- **rebuttal-writer** - 系统化 rebuttal 写作，语气优化
- **paper-miner** - 从成功论文中提取写作知识

### 开发工作流代理

- **architect** - 系统架构设计
- **build-error-resolver** - 构建错误修复
- **bug-analyzer** - 深度代码执行流分析和根因调查
- **code-reviewer** - 代码审查
- **dev-planner** - 开发任务规划和拆解
- **refactor-cleaner** - 代码重构和清理
- **tdd-guide** - TDD 工作流指导
- **kaggle-miner** - Kaggle 工程实践提取

### 设计与内容代理

- **ui-sketcher** - UI 蓝图设计和交互规范
- **story-generator** - 用户故事和需求生成

---

## Hooks（7 个）

| 钩子 | 触发时机 | 功能 |
|------|----------|------|
| `session-start.js` | 会话开始 | 显示 Git 状态、待办事项、可用命令 |
| `skill-forced-eval.js` | 每次用户输入 | 强制评估所有可用技能 |
| `session-summary.js` | 会话结束 | 生成工作日志，检测 CLAUDE.md 更新 |
| `stop-summary.js` | 会话停止 | 快速状态检查，临时文件检测 |
| `security-guard.js` | 文件操作 | 安全验证（密钥检测、危险命令拦截） |
| `pre-compact.py` | 上下文压缩前 | 保存会话状态（决策记录、日志路径）到持久化文件 |
| `post-compact-restore.py` | 会话恢复（compact/resume） | 压缩后重建上下文：决策 + 日志路径 + 恢复操作指引 |

---

## 规则（8 Rules）

| 规则文件 | 作用范围 | 作用 |
|---------|---------|------|
| `agents.md` | 全局 | 代理编排：自动调用时机、并行执行、多视角分析 |
| `security.md` | 全局 | 安全规范：密钥管理、敏感文件保护、提交前安全检查 |
| `orchestrator-protocol.md` | 全局 | 承包商模式：计划→验证→对抗 QA→评分循环（最多 5 轮） |
| `learn.md` | 全局 | 持续学习：`[LEARN:category]` 标签记录经验到 MEMORY.md |
| `single-source-of-truth.md` | 全局 | 单一权威源：`.tex` 是论文权威源；Stata 是过渡期分析权威源 |
| `quality-gates.md` | 路径隔离（`.tex/.do/.py/.R/papers/**`） | 0-100 评分量表；80=commit，85=advisor，90=投稿 |
| `coding-style.md` | 路径隔离（`**/*.py`, `src/**`） | Python 代码规范：文件 200-400 行、类型提示、Factory/Registry |
| `experiment-reproducibility.md` | 路径隔离（`**/*.py`, `**/*.R`, `**/*.do`） | 随机种子、配置记录、检查点管理 |

---

## 持续学习机制

**MEMORY.md** 跨会话积累经验，位于 `~/.claude/projects/-Users-xuhaiping-Desktop/memory/MEMORY.md`。

格式：
```
[LEARN:category] <发现/纠正的内容> → <正确做法或应用时机>
```

类别：`workflow`、`writing`、`python`、`stata`、`data`、`rules`、`skills`、`identity`

触发写入：用户纠正假设、非显而易见的依赖关系被发现、同一模式被 2+ 次交互确认、用户明确要求记住某件事。

---

## 命名规范

### Skill 命名
- 格式：kebab-case（小写+连字符）
- 形式：优先使用 gerund form（动词+ing）
- 示例：`git-workflow`, `bug-detective`, `data-analysis`

### Tags 命名
- 格式：Title Case
- 缩写全大写：TDD, DID, IV, RDD, NLP, APSR, AER
- 示例：`[Writing, Research, CausalInference]`

### 描述规范
- 人称：第三人称
- 内容：包含用途和使用场景

---

## 任务完成总结

每次任务完成时，主动提供简要总结：

```
📋 本次操作回顾
1. [主要操作]
2. [修改的文件]

📊 当前状态
• [Git/文件系统/运行状态]

💡 下一步建议
1. [针对性建议]
```
