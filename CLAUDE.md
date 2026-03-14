# Claude Scholar Configuration

## Project Overview

**Claude Scholar** - Personal Claude Code configuration system for academic research and software development

**Mission**: Cover the complete academic research lifecycle (from ideation to publication) and software development workflows, with plugin development and project management capabilities.

---

## User Background

### Academic Background
- **Degree**: PhD in Social Science (Political Science / Economics)
- **Fields**: Comparative Politics, Political Economy, Political Institutions, Public Economics, Economic History
- **Methods**: Causal inference econometrics (DID, IV, RDD, Synthetic Control), Text as Data / NLP, Applied Machine Learning, Applied Game Theory, Qualitative Historical Comparative Methods
- **Target Venues**:
  - Political Science: APSR, AJPS, JOP, Comparative Political Studies (CPS), International Organization (IO), World Politics
  - Economics: AER, QJE, JPE, REStud, Econometrica, Journal of Public Economics (JPubE)
  - Cross-disciplinary: PNAS, Journal of Conflict Resolution, Political Analysis
- **Focus**: Credible causal identification, rigorous empirical analysis, clear theoretical motivation, precise academic writing

### Tech Stack Preferences

**Primary Tools**:
- **Writing**: LaTeX (primary), Overleaf for collaboration
- **Statistical analysis**: Stata (current primary) → Python (transitioning)
- **Package manager**: `uv` - modern Python package manager

**Python Ecosystem (transitioning from Stata)**:
- **Causal inference**: `statsmodels`, `linearmodels`, `econml`, `doubleml`, `causalml`
- **Data**: `pandas`, `numpy`, `pyarrow`
- **NLP / Text as Data**: `transformers`, `gensim`, `spacy`, `bertopic`
- **Visualization**: `matplotlib`, `seaborn`, `plotnine` (ggplot2 equivalent)
- **Stata bridge**: `pystata`, `stata_setup`

**Git Standards**:
- **Commit convention**: Conventional Commits
  ```
  Type: feat, fix, docs, style, refactor, perf, test, chore
  Scope: data, analysis, paper, config, utils, workflow
  ```
- **Branch strategy**: master/develop/feature/bugfix/hotfix/release
- **Merge strategy**: rebase for feature branch sync, merge --no-ff for integration

---

## Global Configuration

### Language Settings
- **Respond in English to the user**
- Keep technical terms in English (e.g. NeurIPS, RLHF, TDD, Git)
- Do not translate proper nouns or names

### Working Directory Standards
- Plan documents: `/plan` folder
- Temporary files: `/temp` folder
- Auto-create folders if they don't exist

### Task Execution Principles
- Discuss approach before breaking down complex tasks
- Run example tests after implementation
- Make backups, avoid breaking existing functionality
- Clean up temporary files after completion
- **Operation Logging**: For any session involving 3+ tool calls or file modifications, maintain a running session log

### Operation Log Format

Log file location: `~/.claude/session-logs/YYYY-MM-DD.md`
Auto-create the file and directory if they don't exist. Append entries throughout the session.

```markdown
## Session: YYYY-MM-DD HH:MM

### [HH:MM] <Action summary>
- **Tool**: Write / Edit / Bash / WebFetch / etc.
- **Target**: `path/to/file` or `command run`
- **Outcome**: Success / Failed / Partial
- **Notes**: Any important context or decision rationale

### [HH:MM] <Next action>
...
```

Log every: file creation, file edit, bash command with side effects, key decisions. Skip: read-only file reads, web fetches that are purely informational.

### Work Style
- **Task management**: Use TodoWrite to track progress, plan before executing complex tasks, prefer existing skills
- **Communication**: Ask proactively when uncertain, confirm before important operations, follow hook-enforced workflows
- **Code style**: Python follows PEP 8, comments in English, identifiers in English

---

## Core Workflows

### Research Lifecycle (7 Stages)

```
Ideation → Literature Review → Data & Empirics → Paper Writing → Self-Review → Submission/Rebuttal → Post-Acceptance
```

| Stage | Core Tools | Commands |
|-------|-----------|----------|
| 1. Research Ideation | `research-ideation` skill + `gpt-researcher` skill + `literature-reviewer` agent + Zotero MCP | `/research-init`, `/zotero-review`, `/zotero-notes` |
| 2. Literature Review | `daily-paper-generator` skill + `gpt-researcher` skill + Zotero MCP | `/zotero-notes`, `/zotero-review` |
| 3. Data & Empirical Analysis | `results-analysis` skill + `data-analyst` agent | `/analyze-results` |
| 4. Paper Writing | `social-science-paper-writing` skill + `paper-miner` agent | - |
| 5. Self-Review | `paper-self-review` skill + `academic-paper-reviewer` skill | - |
| 6. Submission & Rebuttal | `review-response` skill + `rebuttal-writer` agent | `/rebuttal` |
| 7. Post-Acceptance | `post-acceptance` skill | `/presentation`, `/poster`, `/promote` |

### Supporting Workflows

- **Automation**: 7 Hooks auto-trigger at session lifecycle stages (skill evaluation, env init, work summary, security check, pre-compact save, post-compact restore)
- **Context Survival**: `pre-compact.py` saves state before context compression; `post-compact-restore.py` restores context on resume — plans and decisions survive session boundaries
- **Quality Gates**: All paper/analysis work scored 0-100; commit requires ≥80, journal submission requires ≥90 (`quality-gates.md` rule)
- **Adversarial QA**: Critic+Fixer loop on papers and analysis (max 5 rounds) before committing — `orchestrator-protocol.md` rule
- **Contractor Mode**: Plan → Approve → Autonomous execution loop; requirements spec (MUST/SHOULD/MAY) for complex tasks
- **Single-Source-of-Truth**: `.tex` is authoritative for papers; Stata `.do` is authoritative during Python transition; `data/raw/` is read-only (`single-source-of-truth.md` rule)
- **Continuous Learning**: `[LEARN:category]` tags written to MEMORY.md whenever corrected or a non-obvious pattern is confirmed; read at session start for complex tasks (`learn.md` rule)
- **Zotero Integration**: Automated paper import, collection management, full-text reading, and citation export via Zotero MCP
- **Daily Paper Tracking**: `daily-paper-generator` monitors NBER WP + arXiv econ + top journal TOCs (AER/QJE/JPE/APSR/AJPS/JOP/CPS/JPubE)
- **Web Background Research**: `gpt-researcher` skill for grey literature, policy documents, institutional context, and case backgrounds (complements Zotero for non-paywalled sources)
- **Research Version Control**: Git + DVC for data/analysis/paper versioning; `git-workflow` skill covers research-specific commit scopes (`data`, `analysis`, `results`, `paper`) and branch strategy
- **Replication Package**: `replication-package` skill prepares AER/APSR-compliant replication materials for journal submission
- **Operation Logging**: All sessions with significant actions logged to `~/.claude/session-logs/YYYY-MM-DD.md` — each file edit, bash command, and key decision recorded with timestamp and outcome
- **Skill Evolution**: `skill-development` → `skill-quality-reviewer` → `skill-improver` three-step improvement loop

---

## Skills Directory (42 skills)

### 🔬 Research & Analysis (10 skills)

- **research-ideation**: Research startup (5W1H, literature review, gap analysis, research question formulation, Zotero integration)
- **interview-me**: Socratic research interview — formalize ideas into specification doc with hypotheses and identification strategy (conversational, no AskUserQuestion)
- **results-analysis**: Empirical results analysis (regression tables, identification tests, DID/IV/RDD visualization, robustness checks)
- **data-analysis**: End-to-end data analysis workflow — EDA → regression → publication-ready tables/figures in Python (pyfixest/linearmodels) or Stata; Stata-to-Python translation reference
- **causal-inference-analysis**: DID, IV, RDD, Synthetic Control implementation in Python & Stata (code templates, assumption tests, table & figure generation)
- **citation-verification**: Citation verification (multi-layer: format→API→info→content)
- **daily-paper-generator**: Daily paper tracker — NBER WP + arXiv econ + top journal TOCs (AER/QJE/JPE/APSR/AJPS/JOP/CPS/JPubE)
- **gpt-researcher**: Autonomous web background research — grey literature, policy documents, institutional context, case backgrounds; local PDF corpus RAG
- **devils-advocate**: Adversarial challenge — 5-7 specific attacks on identification, mechanism, measurement, literature; severity-ranked with pre-emption strategies
- **review-paper**: Full referee report simulation — 6 dimensions scored 1-5, referee objections, recommendation; think like AER/APSR referee

### 📝 Paper Writing & Publication (11 skills)

- **ml-paper-writing**: General academic paper writing (kept for NLP/applied ML papers)
- **social-science-paper-writing**: Dual-track econ/polisci paper writing — Economics (AER/QJE/JPE: Intro→Data→Empirical Strategy→Results→Robustness) + PolSci (APSR/JOP: Intro→Theory/Hypotheses→Research Design→Analysis→Discussion); section templates, journal-specific norms, anti-AI writing patterns
- **writing-anti-ai**: Remove AI writing patterns, bilingual (Chinese/English)
- **paper-self-review**: **Scored 0-100** paper quality audit — 8 dimensions with deduction rubric; blocking issues vs warnings; referee objections; submission readiness verdict
- **academic-paper-reviewer**: Multi-perspective peer review simulation — 5 independent reviewers (EIC + Methodology + Domain + Perspective + Devil's Advocate); 0-100 quality rubrics; 5 modes (full, re-review, quick, methodology-focus, guided)
- **review-response**: Systematic rebuttal writing
- **post-acceptance**: Post-acceptance processing (presentation, poster, promotion)
- **doc-coauthoring**: Document co-authoring workflow
- **latex-conference-template-organizer**: LaTeX conference template organization

### 💻 Development Workflows (7 skills)

- **daily-coding**: Daily coding checklist (minimal mode, auto-triggered)
- **git-workflow**: Research project version control — Git + DVC for data/analysis/paper; commit scopes (`data`, `analysis`, `results`, `paper`); DVC setup; research .gitignore
- **replication-package**: Prepare AER/APSR/AJPS replication packages — README template, master script, data README, code quality checklist, openICPSR/Dataverse upload
- **code-review-excellence**: Code review best practices (data processing, econometric analysis scripts)
- **bug-detective**: Debugging and error investigation (Python, Stata, Bash/Zsh)
- **architecture-design**: Data analysis project code architecture and design patterns
- **verification-loop**: Verification loops and testing (regression result validation, reproducibility checks)

### 🔌 Plugin Development (8 skills)

- **skill-development**: Skill development guide
- **skill-improver**: Skill improvement tool
- **skill-quality-reviewer**: Skill quality review
- **command-development**: Slash command development
- **command-name**: Plugin structure guide
- **agent-identifier**: Agent development configuration
- **hook-development**: Hook development and event handling
- **mcp-integration**: MCP server integration

### 🧪 Tools & Utilities (4 skills)

- **planning-with-files**: Planning and progress tracking with Markdown files
- **uv-package-manager**: uv package manager usage
- **webapp-testing**: Local web application testing
- **kaggle-learner**: Kaggle competition learning

### 🎨 Web Design (3 skills)

- **frontend-design**: Create distinctive, production-grade frontend interfaces
- **ui-ux-pro-max**: UI/UX design intelligence (50+ styles, 97 palettes, 57 font pairings, 9 stacks)
- **web-design-reviewer**: Visual website inspection for responsive, accessibility, and layout issues

---

## Commands (50+ Commands)

### Research Workflow Commands

| Command | Function |
|---------|----------|
| `/research-init` | Start Zotero-integrated research ideation workflow (auto-create collections, import papers, full-text analysis) |
| `/zotero-review` | Read papers from Zotero collection, generate structured literature review |
| `/zotero-notes` | Batch read Zotero papers, generate structured reading notes |
| `/analyze-results` | Analyze experiment results (statistical tests, visualization, ablation) |
| `/rebuttal` | Generate systematic rebuttal document |
| `/presentation` | Create conference presentation outline |
| `/poster` | Generate academic poster design |
| `/promote` | Generate promotion content (Twitter, LinkedIn, blog) |

### Development Workflow Commands

| Command | Function |
|---------|----------|
| `/plan` | Create implementation plan |
| `/commit` | Commit code (following Conventional Commits) |
| `/update-github` | Commit and push to GitHub |
| `/update-readme` | Update README documentation |
| `/code-review` | Code review |
| `/tdd` | Test-driven development workflow |
| `/build-fix` | Fix build errors |
| `/verify` | Verify changes |
| `/checkpoint` | Create checkpoint |
| `/refactor-clean` | Refactor and clean up |
| `/learn` | Extract reusable patterns from code |
| `/create_project` | Create new project |
| `/setup-pm` | Configure package manager (uv/pnpm) |
| `/update-memory` | Check and update CLAUDE.md memory |

### SuperClaude Command Suite (`/sc`)

- `/sc agent` - Agent dispatch
- `/sc analyze` - Code analysis
- `/sc brainstorm` - Interactive brainstorming
- `/sc build` - Build project
- `/sc business-panel` - Business panel
- `/sc cleanup` - Code cleanup
- `/sc design` - System design
- `/sc document` - Generate documentation
- `/sc estimate` - Effort estimation
- `/sc explain` - Code explanation
- `/sc git` - Git operations
- `/sc help` - Help info
- `/sc implement` - Feature implementation
- `/sc improve` - Code improvement
- `/sc index` - Project index
- `/sc index-repo` - Repository index
- `/sc load` - Load context
- `/sc pm` - Package manager operations
- `/sc recommend` - Recommend solutions
- `/sc reflect` - Reflection summary
- `/sc research` - Technical research
- `/sc save` - Save context
- `/sc select-tool` - Tool selection
- `/sc spawn` - Spawn subtasks
- `/sc spec-panel` - Spec panel
- `/sc task` - Task management
- `/sc test` - Test execution
- `/sc troubleshoot` - Issue troubleshooting
- `/sc workflow` - Workflow management

---

## Agents (14 Agents)

### Research Workflow Agents

- **literature-reviewer** - Literature search, classification, and trend analysis (Zotero MCP integration: auto-import, full-text reading)
- **data-analyst** - Automated data analysis and visualization
- **rebuttal-writer** - Systematic rebuttal writing with tone optimization
- **paper-miner** - Extract writing knowledge from successful papers

### Development Workflow Agents

- **architect** - System architecture design
- **build-error-resolver** - Build error fixing
- **bug-analyzer** - Deep code execution flow analysis and root cause investigation
- **code-reviewer** - Code review
- **dev-planner** - Development task planning and breakdown
- **refactor-cleaner** - Code refactoring and cleanup
- **tdd-guide** - TDD workflow guidance
- **kaggle-miner** - Extract engineering practices from Kaggle solutions

### Design & Content Agents

- **ui-sketcher** - UI blueprint design and interaction specifications
- **story-generator** - User story and requirement generation

---

## Hooks (7 Hooks)

| Hook | Trigger | Function |
|------|---------|----------|
| `session-start.js` | Session start | Show Git status, todos, available commands |
| `skill-forced-eval.js` | Every user input | Force evaluate all available skills |
| `session-summary.js` | Session end | Generate work log, detect CLAUDE.md updates |
| `stop-summary.js` | Session stop | Quick status check, temp file detection |
| `security-guard.js` | File operations | Security validation (key detection, dangerous command interception) |
| `pre-compact.py` | Pre-compaction | Save session state (decisions, session log path) before context compression |
| `post-compact-restore.py` | SessionStart (compact/resume) | Restore context after compression: decisions + session log + recovery actions |

---

## Rules (8 Rules)

| Rule File | Scope | Purpose |
|-----------|-------|---------|
| `agents.md` | Always-on | Agent orchestration: auto-invocation, parallel execution |
| `security.md` | Always-on | Key management, sensitive file protection, pre-commit checks |
| `orchestrator-protocol.md` | Always-on | Contractor mode: plan→verify→adversarial QA→score loop (max 5 rounds) |
| `learn.md` | Always-on | Continuous learning: `[LEARN:category]` tags → MEMORY.md; triggers for writing entries |
| `single-source-of-truth.md` | Always-on | One authoritative source per artifact: `.tex` for papers, Stata `.do` during Python transition, `data/raw/` is read-only |
| `quality-gates.md` | Path-scoped (`.tex`, `.do`, `.py`, `.R`, papers/) | 0-100 scoring rubrics; thresholds: 80=commit, 85=advisor, 90=journal |
| `coding-style.md` | Path-scoped (`**/*.py`, `src/**`) | Python code standards: 200-400 line files, type hints, Factory/Registry |
| `experiment-reproducibility.md` | Path-scoped (`**/*.py`, `**/*.R`, `**/*.do`) | Random seeds, config recording, checkpoint management |

---

## Continuous Learning

**MEMORY.md** accumulates patterns across sessions at `~/.claude/projects/-Users-xuhaiping-Desktop/memory/MEMORY.md`.

Format:
```
[LEARN:category] <what was discovered or corrected> → <correct behavior or when to apply>
```

Categories: `workflow`, `writing`, `python`, `stata`, `data`, `rules`, `skills`, `identity`

Write an entry when: the user corrects an assumption, a pattern is confirmed across 2+ interactions, a non-obvious dependency is discovered, or the user explicitly asks to remember something.

At session end: scan for corrections → write `[LEARN]` entries → check `CLAUDE.zh-CN.md` is in sync.

---

## Naming Conventions

### Skill Naming
- Format: kebab-case (lowercase + hyphens)
- Form: prefer gerund form (verb+ing)
- Example: `scientific-writing`, `git-workflow`, `bug-detective`

### Tags Naming
- Format: Title Case
- Abbreviations all caps: TDD, RLHF, NeurIPS, ICLR
- Example: `[Writing, Research, Academic]`

### Description Standards
- Person: third person
- Content: include purpose and use cases
- Example: "Provides guidance for academic paper writing, covering top-venue submission requirements"

---

## Task Completion Summary

After each task, proactively provide a brief summary:

```
📋 Operation Review
1. [Main operation]
2. [Modified files]

📊 Current Status
• [Git/filesystem/runtime status]

💡 Next Steps
1. [Targeted suggestions]
```
