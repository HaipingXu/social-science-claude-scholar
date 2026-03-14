---
name: replication-package
description: Use when the user asks to "prepare replication package", "create replication files", "AER replication standards", "APSR replication requirements", "organize code for submission", "data availability statement", "make research reproducible", "package data and code", "openICPSR submission", "dataverse upload", "write data README", "code README for replication", "clean up code for publication", or "submit replication materials".
tags: [Replication, OpenScience, AER, APSR, DataManagement, Reproducibility]
version: 1.0.0
---

# Replication Package Preparation

Guide for preparing publication-ready replication packages for top economics and political science journals. Covers AER (American Economic Association) and APSR/AJPS (political science) standards.

## Journal Requirements Overview

| Journal | Policy | Data Archive | Code Required | Standard |
|---------|--------|-------------|---------------|----------|
| AER / AEJ | Mandatory | openICPSR | Yes | AEA Data & Code Availability Policy |
| QJE | Mandatory | Harvard Dataverse | Yes | Harvard Dataverse |
| JPE | Mandatory | openICPSR | Yes | AEA-compatible |
| APSR | Mandatory | Harvard Dataverse | Yes | APSA Guidelines |
| AJPS | Mandatory | Harvard Dataverse | Yes | AJPS Replication Policy |
| JOP | Mandatory | Harvard Dataverse | Yes | JOP Policy |

---

## Replication Package Structure

```
replication-package/
├── README.pdf               ← required by AEA; describes everything
├── README.md                ← same content, markdown version
│
├── data/
│   ├── raw/                 ← original data (if shareable)
│   │   ├── census_2020.dta
│   │   └── README_data.txt  ← source, access, citation for each dataset
│   └── processed/           ← cleaned data used in analysis
│
├── code/
│   ├── 00_master.do/.py     ← single entry point: runs everything
│   ├── 01_clean.do/.py
│   ├── 02_main_analysis.do/.py
│   ├── 03_robustness.do/.py
│   ├── 04_figures.do/.py
│   └── 05_tables.do/.py
│
├── output/
│   ├── figures/             ← all figures in paper
│   └── tables/              ← all tables (LaTeX + CSV)
│
└── requirements/
    ├── stata_packages.txt   ← ado packages + versions
    └── requirements.txt     ← Python packages + versions
```

---

## Step 1: README.md / README.pdf

The README is the most important file. AEA requires PDF format. Structure:

```markdown
# Replication Package for "[Paper Title]"

**Authors**: [Names]
**Journal**: [Journal Name]
**DOI**: [final DOI if available]
**Date**: YYYY-MM-DD

---

## Overview

This package replicates all tables and figures in [Paper Title].
Running `code/00_master.do` (or `00_master.py`) reproduces all results.

---

## Data Availability and Sources

| Dataset | Source | Access | Notes |
|---------|--------|--------|-------|
| Census 2020 | US Census Bureau | Public | Downloaded YYYY-MM-DD |
| Proprietary XYZ | [Provider] | Restricted | See data/raw/README_data.txt |

**Restricted-access data**: [Explain how to obtain; typical wait time; contact]

---

## Software Requirements

**Stata**: Version 17+
Required packages (auto-installed by `00_master.do`):
- reghdfe (Correia 2016) — version X.X
- rdrobust (Calonico et al. 2014) — version X.X
- estout (Jann 2007) — version X.X

**Python**: 3.10+
See `requirements/requirements.txt` for full package list.
Key packages: linearmodels 6.x, pyfixest 0.x, stargazer 0.x

---

## Instructions to Replicators

1. Set the global path in `code/00_master.do`: `global root "/path/to/replication-package"`
2. Run: `do code/00_master.do`
3. All figures saved to `output/figures/`; all tables to `output/tables/`
4. Expected run time: ~XX minutes on standard hardware

---

## Package Contents

| File/Directory | Description |
|----------------|-------------|
| `README.pdf` | This file |
| `data/raw/` | Original input datasets |
| `data/processed/` | Intermediate cleaned data |
| `code/00_master.do` | Master script (run this) |
| `code/01_clean.do` | Data cleaning |
| `code/02_main_analysis.do` | Main results (Tables 1–4) |
| `code/03_robustness.do` | Robustness checks (Appendix Tables) |
| `code/04_figures.do` | All figures |
| `output/figures/` | Figures 1–N (PDF format) |
| `output/tables/` | Tables 1–N (.tex + .csv) |

---

## Correspondence

Questions: [author email]
```

---

## Step 2: Master Script (00_master.do / 00_master.py)

**Stata master script:**

```stata
* ============================================================
* MASTER REPLICATION SCRIPT
* Paper: "[Title]"
* ============================================================

clear all
set more off
set scheme s2color

* ── 1. Set root path (CHANGE THIS) ──────────────────────────
global root "/Users/yourname/replication-package"

* ── 2. Define sub-paths ─────────────────────────────────────
global data    "$root/data"
global raw     "$data/raw"
global proc    "$data/processed"
global code    "$root/code"
global figures "$root/output/figures"
global tables  "$root/output/tables"

* ── 3. Install required packages ────────────────────────────
* Uncomment on first run:
* ssc install reghdfe, replace
* ssc install ftools, replace
* ssc install rdrobust, replace
* ssc install estout, replace

* ── 4. Run analysis scripts in order ────────────────────────
do "$code/01_clean.do"
do "$code/02_main_analysis.do"
do "$code/03_robustness.do"
do "$code/04_figures.do"
do "$code/05_tables.do"

display "✓ Replication complete. Check output/ directory."
```

**Python master script:**

```python
"""
Master replication script.
Run: python code/00_master.py
"""
from pathlib import Path
import subprocess
import sys

ROOT = Path(__file__).parent.parent  # adjust as needed

scripts = [
    "01_clean.py",
    "02_main_analysis.py",
    "03_robustness.py",
    "04_figures.py",
    "05_tables.py",
]

for script in scripts:
    print(f"\n{'='*50}\nRunning {script}...\n{'='*50}")
    result = subprocess.run(
        [sys.executable, ROOT / "code" / script],
        check=True
    )

print("\n✓ Replication complete. Check output/ directory.")
```

---

## Step 3: Code Quality Checklist

Before packaging, verify each script:

**Stata scripts:**
- [ ] All paths use global macros (`$root`, `$data`, etc.) — no hardcoded paths
- [ ] `set seed XXXXX` at the top if any random processes
- [ ] `set more off` and `clear all` at top
- [ ] Comments explain what each section does
- [ ] `log using` to capture output (helps debugging)
- [ ] All user-written packages listed in README

**Python scripts:**
- [ ] All paths relative to `ROOT` using `pathlib.Path`
- [ ] `random.seed()`, `np.random.seed()` set at top
- [ ] `requirements.txt` captures exact package versions
- [ ] No hardcoded absolute paths
- [ ] Comments in English

**Both:**
- [ ] Script runs top-to-bottom without manual intervention
- [ ] Output files don't overwrite themselves if script run twice
- [ ] Numbered in logical order matching paper sections

---

## Step 4: Data README

Create `data/raw/README_data.txt`:

```
DATA SOURCES AND AVAILABILITY
===============================

1. [Dataset Name] (file: census_2020.dta)
   Source: [Full citation]
   URL: [download link]
   Access: Public / Restricted
   Downloaded: YYYY-MM-DD
   Version: [version or as-of date]
   Notes: [any relevant details, subsetting, etc.]

2. [Proprietary Dataset] (file: firm_panel.dta)
   Source: [Provider name]
   Access: Restricted — requires signed data use agreement
   Contact: [contact info]
   Typical wait: [X weeks]
   Notes: We obtained access under agreement #XXX. Variables used: [list]
```

---

## Step 5: Software Version Capture

**Stata:**
```stata
* At end of 00_master.do, log environment:
display "Stata version: `c(stata_version)'"
display "OS: `c(os)'"
display "Date: `c(current_date)'"
ado describe  // lists installed packages with versions
```

**Python:**
```bash
# Generate requirements.txt with pinned versions
uv pip freeze > requirements/requirements.txt

# Or: only direct dependencies
uv pip list --format=json | python -c "
import json, sys
pkgs = json.load(sys.stdin)
for p in pkgs: print(f\"{p['name']}=={p['version']}\")
" > requirements/requirements.txt
```

---

## Step 6: Self-Test Before Submission

```bash
# Create a clean test environment
mkdir /tmp/replication-test
cp -r replication-package/ /tmp/replication-test/

# Python: test in fresh venv
cd /tmp/replication-test
python -m venv .venv
source .venv/bin/activate
pip install -r requirements/requirements.txt
python code/00_master.py

# Stata: open fresh Stata, run 00_master.do
# Verify all outputs in output/ match paper figures/tables
```

---

## Step 7: Upload to openICPSR / Harvard Dataverse

**openICPSR (AEA journals):**
1. Go to [openicpsr.org](https://www.openicpsr.org)
2. Create new deposit → select "ICPSR" or "AEA"
3. Upload zip of replication package
4. Fill metadata: title, authors, keywords, geographic coverage
5. Submit for AEA review; receive deposit number (e.g., `openICPSR-XXXXXX`)
6. Add deposit DOI to paper before final submission

**Harvard Dataverse (APSR/AJPS/QJE):**
1. Go to [dataverse.harvard.edu](https://dataverse.harvard.edu)
2. Create dataset under your account or journal's dataverse
3. Upload files, fill metadata
4. Publish to get DOI

---

## Common Issues

| Problem | Solution |
|---------|----------|
| Hardcoded paths | Use `$root` globals (Stata) or `pathlib.Path` (Python) |
| Package not installed | Add to master script install section |
| Results don't match | Check seed, Stata version, package versions |
| Data too large to upload | Use restricted access + describe access procedure |
| Proprietary data | Provide synthetic data or describe access |

---

## Reference Resources

- **`references/aea-policy.md`** — Full AEA Data & Code Availability Policy summary
- **`references/journal-specific.md`** — APSR/AJPS/QJE/JPE specific requirements

## External Standards

- [AEA Data Editor Guidance](https://aeadataeditor.github.io/aea-de-guidance/)
- [Social Science Data Editors Template README](https://social-science-data-editors.github.io/template_README/)
- [APSA Replication Guidelines](https://www.apsanet.org/replication)
