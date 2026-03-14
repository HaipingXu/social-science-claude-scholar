---
name: daily-paper-generator
description: Use when the user asks to "generate daily paper", "find recent papers", "search NBER working papers", "find new econ papers", "find new polisci papers", "search arXiv economics", "check journal updates", "what's new in political economy", "find papers on causal inference", "find papers on text as data", or wants paper summaries in comparative politics, political economy, political institutions, public economics, or economic history.
version: 1.0.0
---

# Daily Paper Generator (Econ / PolSci Edition)

## Overview

Automate discovery, review, and summarization of recent research papers across economics and political science. Each run produces TOP 3 paper summaries with bilingual (Chinese + English) reviews, saved as Markdown files.

**Core workflow:**
1. Search across multiple sources (arXiv econ, NBER WP, journal TOCs)
2. Retrieve paper metadata and abstracts
3. Evaluate quality using social-science criteria (see `references/quality-criteria.md`)
4. Select top 3 papers
5. Generate structured bilingual summaries
6. Save to `daily paper/` directory

---

## Sources to Search

Search in priority order. Use Chrome MCP browser for all navigation.

### Source 1: arXiv Economics & Political Science

**Category browsing (recommended for breadth):**
```
https://arxiv.org/list/econ.GN/recent       # General Economics
https://arxiv.org/list/econ.PE/recent       # Political Economy
https://arxiv.org/list/econ.GE/recent       # General Equilibrium
https://arxiv.org/list/cs.CL/recent         # NLP / Text as Data
```

**Keyword search (for focused topics):**
```
https://arxiv.org/search/?searchtype=all&query=KEYWORDS&abstracts=show&order=-announced_date_first
```

See `references/keywords.md` for the full keyword list organized by research area.

### Source 2: NBER Working Papers

Browse latest working papers (most important source for economics):
```
https://www.nber.org/papers?page=1&perPage=50&sortBy=public_date
```

Filter by relevant programs:
- PE – Public Economics
- POL – Political Economy
- DEV – Development of the American Economy (Economic History)
- IFM – International Finance and Macroeconomics
- LS – Labor Studies (if relevant)

### Source 3: Journal New Issues (Top Journals)

Check for newly published articles. Navigate to current issue pages:

**Economics Top 5:**
| Journal | Current Issue URL |
|---------|------------------|
| AER | https://www.aeaweb.org/journals/aer/current |
| QJE | https://academic.oup.com/qje/issue |
| JPE | https://www.journals.uchicago.edu/toc/jpe/current |
| REStud | https://academic.oup.com/restud/issue |
| Econometrica | https://onlinelibrary.wiley.com/toc/14680262/current |

**Political Science:**
| Journal | Current Issue URL |
|---------|------------------|
| APSR | https://www.cambridge.org/core/journals/american-political-science-review/latest-issue |
| AJPS | https://onlinelibrary.wiley.com/toc/15405907/current |
| JOP | https://www.journals.uchicago.edu/toc/jop/current |
| CPS | https://journals.sagepub.com/toc/cpsa/current |
| JPubE | https://www.sciencedirect.com/journal/journal-of-public-economics/issues |

---

## Evaluation Criteria

Score each paper on 5 dimensions (see `references/quality-criteria.md` for detailed rubrics):

| Dimension | Weight | Key Questions |
|-----------|--------|---------------|
| Contribution & Novelty | 30% | New finding, mechanism, or method? |
| Identification Strategy | 25% | Is causal claim credible? (for empirical) |
| Relevance to Research Areas | 20% | Fits comparative politics / poleco / public econ / econ history / text-as-data? |
| Data & Method Quality | 15% | Sample size, measurement validity, robustness |
| Writing & Clarity | 10% | Clear argument, well-structured |

Score 1–5 per dimension → weighted sum → rank → pick top 3.

---

## Output Format

Each paper summary must contain **8 sections**:

```markdown
# [Paper Title]

## Authors & Affiliation
[Author list]
[Lead institution]

## Source & Link
**Source**: [arXiv / NBER WP / Journal Name]
**Link**: [URL]
**Date**: YYYY-MM-DD
**ID**: [arXiv ID / NBER WP number / DOI]
**JEL / Keywords**: [if available]

## 中文评述 (~300字)
**研究背景**：[1-2句，问题重要性]
**研究缺口**：[2-3句，现有文献不足]
**核心贡献**：[1-2句，本文贡献]
**识别策略/方法**：[2-3句，因果识别或方法创新]
**主要发现**：[2-3句，关键结果]
**意义与局限**：[1-2句]

## English Review
[Fluent academic prose, same structure as Chinese review, ~200 words]
[Avoid AI-like phrasing. Natural, direct, varied sentence structure.]

## Main Figure / Table
[Reserve space: insert key figure or Table 1 if available]

## Paper Metadata
| Field | Content |
|-------|---------|
| **Title** | |
| **First Author** | |
| **All Authors** | |
| **Affiliation** | |
| **Date** | |
| **Source** | |
| **Link** | |
| **JEL Codes** | |
| **Methods** | [e.g., DID, IV, RDD, Text Analysis, Survey Experiment] |

## Integrated Format (for sharing)
Daily Paper MMDD

[Title]
[URL]

[Chinese review]

[English review]

## Appendix
**Replication/Data**: [Available / Not stated / Link if provided]
**Related Papers**: [1-2 closely related works if known]
**Notes**: [Any additional observations]
**Sources**: [All URLs consulted]
```

---

## File Output

Save to fixed directory `/Users/xuhaiping/research/daily-papers/`:

```
/Users/xuhaiping/research/daily-papers/
├── 2026-03-13-paper-1.md
├── 2026-03-13-paper-2.md
└── 2026-03-13-paper-3.md
```

**Filename format:** `YYYY-MM-DD-paper-N.md`

---

## Quick Reference

| Task | Method |
|------|--------|
| Browse arXiv econ | Navigate category pages with Chrome MCP |
| Browse NBER WPs | Navigate nber.org/papers with Chrome MCP |
| Check journal TOCs | Navigate journal current-issue pages above |
| Search by keyword | Use arXiv search URL with econ keywords |
| Evaluate paper | Apply 5-dimension rubric in `references/quality-criteria.md` |
| Write Chinese review | Follow structure in `references/writing-style.md` |
| Write English review | Apply anti-AI principles: direct, varied, natural |

## Additional Resources

### Reference Files
- **`references/keywords.md`** — Full keyword list organized by research area (causal inference, text-as-data, comparative politics, etc.)
- **`references/quality-criteria.md`** — Detailed 5-dimension evaluation rubrics for social science papers
- **`references/writing-style.md`** — Chinese review templates and English writing principles

### Notes
- Prioritize papers with clear identification strategy for empirical work
- For theory papers, assess formal model quality and applied relevance
- For NLP/text-as-data papers, assess both methodological rigor and substantive contribution
- Chrome MCP browser required for all source navigation
