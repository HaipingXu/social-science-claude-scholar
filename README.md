# Social Science Claude Scholar

A production Claude Code configuration system for academic research in **Economics** and **Political Science** — covering the complete research lifecycle from ideation to publication.

> Inspired by [pedrohcgs/claude-code-my-workflow](https://github.com/pedrohcgs/claude-code-my-workflow). Extended for social science research with causal inference, paper writing, and replication workflows.

---

## Who This Is For

PhD students and researchers in:
- **Economics**: AER, QJE, JPE, REStud, Econometrica, JPubE
- **Political Science**: APSR, AJPS, JOP, CPS, IO, World Politics
- **Methods**: DID, IV, RDD, Synthetic Control, Text as Data, NLP

---

## What's Included

### 📁 Structure

```
.claude/
├── CLAUDE.md                  # English config (authoritative source)
├── CLAUDE.zh-CN.md            # Chinese translation (synchronized)
├── skills/                    # 42 specialized skills
├── rules/                     # 8 governance rules
├── agents/                    # 14 specialized agents
├── commands/                  # 50+ slash commands
└── hooks/                     # 7 lifecycle hooks
```

### 🔬 Research Skills (10)

| Skill | Purpose |
|-------|---------|
| `research-ideation` | Research startup: 5W1H, gap analysis, Zotero integration |
| `interview-me` | Socratic interview → Research Specification Document |
| `data-analysis` | End-to-end Python/Stata analysis; pyfixest, publication-ready output |
| `causal-inference-analysis` | DID, IV, RDD, Synthetic Control templates |
| `results-analysis` | Regression tables, identification tests, robustness checks |
| `devils-advocate` | 5-7 adversarial attacks on identification/mechanism/literature |
| `review-paper` | Full referee report: 6 dimensions, objections, recommendation |
| `daily-paper-generator` | NBER WP + arXiv + top journal TOC tracker |
| `gpt-researcher` | Autonomous web background research |
| `citation-verification` | Multi-layer citation checking |

### 📝 Paper Writing Skills (11)

| Skill | Purpose |
|-------|---------|
| `social-science-paper-writing` | Dual-track: Economics (AER/QJE/JPE) + Political Science (APSR/JOP) |
| `paper-self-review` | **Scored 0-100**: 8 dimensions, deduction rubric, submission readiness |
| `academic-paper-reviewer` | 5-perspective peer review simulation |
| `review-response` | Systematic rebuttal writing |
| `writing-anti-ai` | Remove AI writing patterns (EN + ZH) |
| `replication-package` | AER/APSR replication package preparation |
| `post-acceptance` | Presentation, poster, promotion |

### ⚙️ Quality Infrastructure

| Component | Description |
|-----------|-------------|
| **Quality Gates** | 0-100 scoring; 80=commit, 85=advisor, 90=journal submission |
| **Adversarial QA** | Critic+Fixer loop (max 5 rounds) on papers and analysis |
| **PreCompact Hook** | Saves session state before context compression |
| **Single-Source-of-Truth** | `.tex` authoritative for papers; Stata `.do` during Python transition |
| **Continuous Learning** | `[LEARN:category]` tags accumulate to MEMORY.md across sessions |
| **Path-Scoped Rules** | Rules load only for relevant file types |

---

## Quick Start

### 1. Install

```bash
# Clone into your Claude config directory
git clone https://github.com/YOUR_USERNAME/social-science-claude-scholar.git ~/.claude-scholar

# Copy to your Claude config (merge with existing ~/.claude/)
cp -r ~/.claude-scholar/skills ~/.claude/
cp -r ~/.claude-scholar/rules ~/.claude/
cp -r ~/.claude-scholar/agents ~/.claude/
cp -r ~/.claude-scholar/commands ~/.claude/
cp -r ~/.claude-scholar/hooks ~/.claude/
```

Or fork and use as your complete `~/.claude/` configuration.

### 2. Register Hooks

Add to `~/.claude/settings.json`:

```json
{
  "hooks": {
    "PreCompact": [{
      "matcher": "*",
      "hooks": [{"type": "command", "command": "python3 ~/.claude/hooks/pre-compact.py", "timeout": 10}]
    }],
    "SessionStart": [{
      "matcher": "compact|resume",
      "hooks": [{"type": "command", "command": "python3 ~/.claude/hooks/post-compact-restore.py", "timeout": 10}]
    }]
  }
}
```

### 3. Research Workflow

```
/research-init     → Start with Zotero-integrated ideation
interview-me       → Formalize idea into Research Spec Doc
data-analysis      → Run regressions, produce tables/figures
devils-advocate    → Stress-test identification before writing
social-science-paper-writing → Draft paper (Econ or PolSci track)
paper-self-review  → Score 0-100, find blocking issues
/rebuttal          → Respond to reviewer comments
```

---

## Key Design Principles

1. **Contractor Mode**: Plan → Approve → Autonomous execute → Verify → Score → Present
2. **Single Source of Truth**: One authoritative file per artifact; derived files generated, never edited
3. **Adversarial QA**: Every paper runs through a hostile AER/APSR referee before submission
4. **Numeric Quality Gates**: No subjective "looks good" — scores block commits and submissions
5. **Context Survival**: Session state persists across Claude's context compression boundaries

---

## Python Stack

Primary: **pyfixest** (panel regressions, Sun & Abraham DID), **plotnine** (ggplot2-style figures)

```python
from pyfixest.estimation import feols
from pyfixest.report import etable

# Two-way FE with clustered SE
m1 = feols("log_wage ~ educ | ind_id + year", data=df, vcov={"CRV1": "state"})

# Sun & Abraham (2021) heterogeneity-robust DID
sa = feols("y ~ sunab(cohort, rel_time) | unit + year", data=df, vcov={"CRV1": "unit"})

etable([m1, sa], file="output/tables/table1.tex")
```

---

## Acknowledgments

Built on top of Claude Code's agent/skill/hook infrastructure.
Architecture inspired by [Pedro Sant'Anna's workflow](https://github.com/pedrohcgs/claude-code-my-workflow).

---

## License

MIT
