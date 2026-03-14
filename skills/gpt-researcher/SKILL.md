---
name: gpt-researcher
description: Use this skill when the user asks to "research background on", "find background information about", "search web for context on", "look up policy history of", "find grey literature on", "research institutional context", "find government reports on", "background research for introduction section", "research country context", "web research on", "autonomous web search", "deep research on", "find sources about", or needs web-sourced background context for academic writing (political economy, comparative politics, economic history, public policy). Complements Zotero/arXiv for web-accessible grey literature and policy documents.
tags: [Research, WebSearch, Background, GreyLiterature, Policy]
version: 1.0.0
---

# GPT Researcher — Academic Research Background Tool

Autonomous deep web research agent for gathering background context, policy documents, grey literature, and institutional history. **Complements** (does not replace) academic literature search via Zotero/arXiv.

## When to Use vs. Other Tools

| Task | Best Tool |
|------|-----------|
| Find recent academic papers | `daily-paper-generator` + Zotero |
| Read and annotate specific papers | `literature-reviewer` agent |
| Institutional/country background | **GPT Researcher** ← this skill |
| Policy documents & reports | **GPT Researcher** ← this skill |
| Local PDF corpus research | **GPT Researcher** ← this skill |
| Historical event context | **GPT Researcher** ← this skill |
| Quantitative data retrieval | Manual (FRED, World Bank API) |

---

## Setup Status (2026-03-14)

| Component | Status | Notes |
|-----------|--------|-------|
| venv | ✅ `/tmp/gptr-env/` (Python 3.11) | Recreate if /tmp cleared: `cd /tmp && ~/.local/bin/uv venv gptr-env --python 3.11 && ~/.local/bin/uv pip install gpt-researcher langchain-anthropic langchain-huggingface sentence-transformers tavily-python --python /tmp/gptr-env/bin/python` |
| TAVILY_API_KEY | ✅ Set in `~/.zshenv` | 1000 searches/month free |
| ANTHROPIC_API_KEY | ⚠️ Not set | Needed for full gpt-researcher autonomous mode; get from console.anthropic.com |

## Two Usage Modes

### Mode A: Tavily Search + Claude Synthesis (Recommended — works now)

```bash
# Run Tavily search
export TAVILY_API_KEY="$(grep TAVILY ~/.zshenv | cut -d'"' -f2)"
/tmp/gptr-env/bin/python ~/.claude/scripts/tavily_search.py "your research query"

# Results are printed + saved to /tmp/tavily_results_TIMESTAMP.md
# Then tell Claude: "Read /tmp/tavily_results_*.md and synthesize a background section"
```

**This is the practical daily workflow** — Tavily finds sources, Claude synthesizes.

### Mode B: Full GPT Researcher (requires ANTHROPIC_API_KEY)

```bash
# First: get API key from console.anthropic.com → API Keys → Create
echo 'export ANTHROPIC_API_KEY="sk-ant-YOUR_KEY"' >> ~/.zshenv
source ~/.zshenv

# Then run with all config:
export SMART_LLM="anthropic:claude-haiku-4-5"
export FAST_LLM="anthropic:claude-haiku-4-5"
export STRATEGIC_LLM="anthropic:claude-haiku-4-5"
export EMBEDDING="huggingface:sentence-transformers/all-MiniLM-L6-v2"
/tmp/gptr-env/bin/python -c "
import asyncio, os
from gpt_researcher import GPTResearcher
async def run():
    r = GPTResearcher(query='YOUR QUERY', report_type='research_report', verbose=False)
    await r.conduct_research()
    print(await r.write_report())
asyncio.run(run())
"
```

Get Tavily key: https://app.tavily.com | Get Anthropic key: https://console.anthropic.com

---

## Core Usage Patterns for Academic Research

### 1. Institutional / Country Background Research

Use for writing Introduction or Case Selection sections:

```python
import asyncio
from gpt_researcher import GPTResearcher

async def research_background(topic: str, output_file: str = "background.md"):
    researcher = GPTResearcher(
        query=topic,
        report_type="research_report",   # 2000+ word detailed report
        report_source="web",
    )
    await researcher.conduct_research()
    report = await researcher.write_report()

    with open(output_file, "w") as f:
        f.write(report)
    print(f"Report saved to {output_file}")
    return report

# Example: Comparative politics case background
asyncio.run(research_background(
    "Political economy of state-business relations in Taiwan 1949-1980: "
    "KMT party structure, land reform, export-led industrialization policy",
    output_file="background/taiwan_political_economy.md"
))
```

### 2. Policy History Research

For policy analysis papers — trace legislative/regulatory history:

```python
asyncio.run(research_background(
    "History of minimum wage legislation in US states 1990-2020: "
    "key policy changes, timing, state-level variation, political context",
    output_file="background/min_wage_policy_history.md"
))
```

### 3. Deep Research (Multi-Level, ~5 min)

For comprehensive literature sweeps — recursively explores subtopics:

```python
async def deep_research(query: str):
    researcher = GPTResearcher(
        query=query,
        report_type="deep",   # recursive tree exploration
    )
    await researcher.conduct_research()
    return await researcher.write_report()

# Good for: economic history, qualitative comparative, mechanism tracing
asyncio.run(deep_research(
    "Causes and consequences of property rights reforms in post-communist Eastern Europe"
))
```

### 4. Local Document Research (PDF Corpus RAG)

Research across your existing PDFs — works with papers, reports, archives:

```python
import os
os.environ["DOC_PATH"] = "./my-papers"  # directory with your PDFs

researcher = GPTResearcher(
    query="How do these papers explain variation in democratic backsliding?",
    report_type="research_report",
    report_source="local",   # searches local docs only
)
await researcher.conduct_research()
report = await researcher.write_report()
```

### 5. Hybrid Search (Web + Local Documents)

```python
researcher = GPTResearcher(
    query="Electoral system reform and party fragmentation: key arguments",
    report_type="research_report",
    report_source="hybrid",   # web + local PDFs combined
)
```

---

## Output Quality & Limitations

**Strengths for academic use:**
- Grey literature (government reports, think tank papers, NGO documents)
- Policy timelines and event chronologies
- Institutional descriptions and organizational histories
- News archives for event documentation
- Finding publicly available datasets and data sources

**Important limitations — always verify:**
- ❌ Cannot access paywalled journals (JSTOR, Elsevier, etc.)
- ❌ Citations may not be in correct academic format → paste into Zotero for cleaning
- ❌ May hallucinate specific statistics or dates → fact-check key claims
- ❌ Not a substitute for systematic literature review
- ✅ Use output as **first draft context**, not final citations

**Recommended workflow:**
1. Run GPT Researcher for background sweep
2. Copy promising sources into Zotero for proper citation
3. Verify key factual claims before including in paper

---

## Integration with Research Workflow

### In Research Ideation Stage
```
research-ideation skill
    └── GPT Researcher: "What is the policy/institutional context of [topic]?"
    └── Output → background.md → feeds Introduction writing
```

### In Paper Writing Stage
```
ml-paper-writing skill (Introduction section)
    └── GPT Researcher: search for grey literature and policy context
    └── Zotero: formal academic citations
    └── Combined → complete Introduction with proper sourcing
```

### Quick One-liner (for simple queries)
```bash
python -c "
import asyncio
from gpt_researcher import GPTResearcher
async def r(q):
    res = GPTResearcher(q, 'research_report')
    await res.conduct_research()
    print(await res.write_report())
asyncio.run(r('$QUERY'))
"
```

---

## Academic Research Query Templates

Copy and adapt these for common research scenarios:

```python
QUERY_TEMPLATES = {
    "case_background": "{country/region} political economy {period}: "
                       "key institutions, major actors, policy trajectory",

    "policy_history":  "History of {policy_area} in {country} {years}: "
                       "legislation timeline, implementation, political context",

    "dataset_discovery": "Available datasets and data sources for {topic}: "
                         "government statistics, panel data, survey data",

    "mechanism_context": "Evidence for {mechanism} in {context}: "
                         "case studies, qualitative evidence, historical examples",

    "lit_gap_scan":    "Recent scholarly debate on {topic}: "
                       "competing arguments, unresolved questions, empirical gaps",
}
```

---

## Reference Resources

- **`references/config-reference.md`** — All configuration options (LLM provider, search depth, output format)
- **`references/deep-research.md`** — Deep research mode settings and cost estimates
- Official docs: https://docs.gptr.dev
