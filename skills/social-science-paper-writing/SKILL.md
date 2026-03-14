---
name: social-science-paper-writing
description: "Use when the user asks to 'write a political science paper', 'draft an economics paper', 'write intro/theory/empirics/conclusion section', 'write for APSR', 'write for AER', 'write for JOP', 'draft identification strategy section', 'write robustness section', 'write theory section with hypotheses', 'write data section', 'write results section', 'write paper for top journal', 'polish academic writing', 'improve paper structure', 'APSR submission', 'AER submission', 'draft literature review', or 'write abstract'. Supports two tracks: Economics (AER/QJE/JPE style) and Political Science (APSR/AJPS/JOP style)."
tags: [Writing, Academic, Economics, PoliticalScience, APSR, AER, Empirical, CausalInference]
version: "1.0"
---

# Social Science Paper Writing — Econ & PolSci Tracks

Dual-track writing assistant for top-journal academic papers in economics and political science. Covers the full paper lifecycle: conceptual outline → section drafts → journal-specific polish.

---

## Track Selection

| Your Target | Use |
|-------------|-----|
| AER, QJE, JPE, REStud, Econometrica, JPubE | **Econ Track** |
| APSR, AJPS, JOP, CPS, IO, World Politics, Political Analysis | **PolSci Track** |
| Cross-disciplinary (PNAS, JCR) | Start with PolSci Track; adjust tone |

**If unsure**: State your primary audience (economists vs. political scientists). The core empirical sections are similar; the differences are in framing, theory sections, and writing style.

---

## Paper Structure Comparison

### Economics Track (AER/QJE/JPE)

```
1. Introduction          ← 1200-1800 words; front-load contribution + results
2. Related Literature    ← Usually integrated into Introduction (500-800w) OR standalone section
3. Theoretical Framework ← Optional; formal model OR economic intuition
4. Data & Institutional Background
5. Empirical Strategy    ← Most scrutinized section
6. Results               ← Main tables + coefficient interpretation
7. Robustness & Extensions
8. Conclusion
```

**Econ writing norms:**
- Introduction must include: (a) motivating empirical fact, (b) research question, (c) identification strategy, (d) main findings with magnitudes, (e) contribution to literature, (f) paper roadmap
- Results stated numerically with coefficients: "A one-standard-deviation increase in X is associated with a Y-unit increase in Z (p<0.01)"
- Avoid normative language; let data speak
- Short sentences, direct prose. AER style is terse.

### Political Science Track (APSR/AJPS/JOP)

```
1. Introduction          ← 800-1200 words; puzzle → argument → contribution
2. Theory & Hypotheses   ← Dedicated section; formal or informal theory; explicit H1, H2...
3. Research Design       ← Case selection + identification strategy
4. Data & Measurement    ← Variable operationalization + descriptive stats
5. Empirical Analysis    ← Main results + heterogeneity
6. Robustness Checks     ← Alternative measures, samples, specs
7. Discussion            ← Scope conditions + mechanisms + alternative explanations
8. Conclusion
```

**PolSci writing norms:**
- Theory section must derive *testable hypotheses* from logical argument
- Literature review integrated into theory — establish "what we know" before "what this paper adds"
- Research design section: justify case selection, explain identification, acknowledge threats
- More prose-heavy than economics; less equation-forward
- APSR: ~12,000 words + references; JOP: ~10,000 words

---

## Section-by-Section Writing Guide

### 1. Introduction

**Economics Introduction Template (5-paragraph NBER style):**

```
¶1: Hook — motivating empirical fact or puzzle (1-3 sentences + figure/table reference)
    "Does X cause Y? [Motivating statistic.] Despite [size/importance], we know remarkably little about [mechanism/heterogeneity/context]."

¶2: This paper — what we do and how
    "This paper provides [causal/descriptive] evidence on [question]. We exploit [identification strategy] to isolate [variation]. Our setting is [context] because [institutional detail that makes identification credible]."

¶3: Main findings — numerically specific
    "We find that [main result with coefficient and significance]. This effect is [large/small] relative to [benchmark]. We also find [secondary finding]. [Mechanism evidence if available]."

¶4: Contribution to literature — 3 literatures, 2-3 sentences each
    "Our paper contributes to three strands of literature. First, [Literature A]: [Our contribution]. Second, [Literature B]: [Our contribution]. Third, [Literature C]: [Our contribution]."

¶5: Roadmap — 1 sentence per section
    "Section 2 describes the institutional context. Section 3 presents our empirical strategy..."
```

**Political Science Introduction Template:**

```
¶1: Open with the empirical puzzle or policy stakes
    "[Striking fact about the phenomenon]. This is puzzling because [existing theory predicts X but we observe Y]."

¶2: Existing explanations and their limits
    "Scholars have argued [Explanation A] and [Explanation B]. However, [limitation of existing work — empirical gap, theoretical underspecification, scope condition ignored]."

¶3: This paper's argument (the "I argue that...")
    "I argue that [Core Argument]. The mechanism is [causal chain]. This argument has implications for [broader stakes]."

¶4: Evidence — data, design, main findings
    "I test this argument using [Data]. The identification strategy exploits [variation]. I find [main result], consistent with [theoretical prediction]."

¶5: Contribution — theory + empirics + policy
    "This paper contributes to [Literature A] by [Contribution]. For [Literature B], the findings suggest [Implication]. The analysis also speaks to [Policy Domain]."

¶6: Roadmap
```

---

### 2. Theory Section (PolSci Track)

**Structure:**
```
2.1  Prior literature — what we know and the gap
2.2  Theoretical framework — assumptions, actors, mechanism
2.3  Hypotheses — derived from the theory, numbered, testable

Format for hypotheses:
H1: [Direction] + [Mechanism trigger] → [Outcome direction]
Example: "Hypothesis 1 (Compliance Mechanism): Provincial party secretaries with more extensive central government experience will be more likely to implement central directives, even at the cost of local economic performance."
```

**PolSci theory section norms:**
- One hypothesis per distinct theoretical prediction; don't bundle
- Hypotheses should be falsifiable — what would we observe if H1 is *wrong*?
- For game theoretic models: present intuition in prose first, formal model in appendix
- For mechanism papers: distinguish *necessary* vs. *sufficient* conditions

---

### 3. Empirical Strategy / Identification Section

**This is the most important section in any causal empirical paper.**

#### Economics Style (Empirical Strategy)

```markdown
## 3. Empirical Strategy

### 3.1 Baseline Specification

Our baseline specification is:

Y_{it} = α + β·X_{it} + γ·Z_{it} + δ_i + λ_t + ε_{it}

where Y_{it} is [outcome] for unit i in year t, X_{it} is [treatment variable],
Z_{it} is a vector of controls including [list], δ_i are unit fixed effects,
and λ_t are time fixed effects. Standard errors are clustered at the [level].

### 3.2 Identification

The key identifying assumption is that, conditional on fixed effects and controls,
variation in X_{it} is uncorrelated with unobserved determinants of Y_{it}.

**Threats to identification:**
1. [Threat 1] — Addressed by [approach]
2. [Threat 2] — Addressed by [approach]

**Supporting evidence for identification:**
- Pre-trend test: [Result — Table X / Figure X]
- Placebo: [Result — Appendix Table X]
- [Additional test if applicable]
```

#### PolSci Style (Research Design)

```markdown
## 3. Research Design

### 3.1 Case Selection
I focus on [context] for [N] reasons. First, [substantive reason — why this case is theoretically relevant].
Second, [data/measurement reason — why measurement is possible here].
Third, [identification reason — why causal inference is more credible here than elsewhere].

### 3.2 Identification Strategy
To identify the effect of [X] on [Y], I exploit [source of variation].
The key assumption is [parallel trends / exclusion restriction / unconfoundedness].

**Validity of this assumption:**
- [Test 1]: [Evidence]
- [Test 2]: [Evidence]

### 3.3 Estimation
I estimate [equation or description of estimator]. I cluster standard errors at the [unit]
level because [justification].
```

---

### 4. Results Section

**Norms for both tracks:**
- Lead with the headline result ("Table 2, Column 3 — our preferred specification")
- Report coefficient, standard error, significance, AND magnitude in words
- Never say "X is significant" alone — always report sign, magnitude, and interpretation
- For interaction terms: present marginal effects plot (Brambor-Clark-Golder 2006)

**Economics results prose template:**
```
Table 2 reports our baseline estimates. Column (1) includes only province and year
fixed effects; Column (3) adds the full set of controls and is our preferred specification.
The coefficient on [X] is [β] ([SE], p [<0.05/0.01]), indicating that a one-[unit]
increase in [X] is associated with a [β × unit]-[outcome unit] increase in [Y].
This represents [X%] of the sample mean / [X] standard deviations.
```

**PolSci results prose template:**
```
Model 3 — our preferred specification with the full set of controls and two-way
fixed effects — yields a positive and statistically significant coefficient on [X]
(β = [value], SE = [value], p < [threshold]). Consistent with Hypothesis 1,
provinces/countries/units with higher levels of [X] experience [Y-direction] [Y] outcomes.
A one-standard-deviation increase in [X] is associated with a [magnitude] change in [Y],
equivalent to [X% / comparison].
```

---

### 5. Robustness Section

**Standard robustness battery (both tracks):**

```markdown
## Robustness Checks

### 5.1 Alternative Outcome Measures
[Baseline DV] → [Alternative 1] (Appendix Table X): [Result — "holds / attenuates to β=X"]
[Baseline DV] → [Alternative 2] (Appendix Table Y): [Result]

### 5.2 Alternative Treatment Measures
[Baseline IV] → [Alternative measure 1]: [Result]
[Baseline IV] → [Time-invariant version]: [Result]

### 5.3 Sample Restrictions
Excluding [subgroup] (Appendix Table Z): [Result]
Excluding [outlier provinces/countries]: [Result]
Winsorized at [1%/5%]: [Result]

### 5.4 Placebo Tests
[Temporal placebo — pre-treatment period]: [Result, null as expected]
[Spatial/unit placebo]: [Result, null as expected]

### 5.5 Alternative Estimators / Specifications
[DID → Staggered DID with Callaway-Sant'Anna 2021]: [Result]
[OLS → Poisson / Log-log / IV]: [Result]
[No clustering → Wild cluster bootstrap (Cameron et al. 2008)]: [Result]
```

---

### 6. Discussion / Conclusion

**Discussion Section (PolSci):**
```
Address in order:
1. Scope conditions — where does the argument apply / not apply?
2. Alternative mechanisms — rule out or acknowledge remaining threats
3. Implications for theory — what does this change in our understanding?
4. Policy implications — practical takeaways (1 paragraph, not over-sold)
```

**Conclusion (both tracks) — 3-5 paragraphs:**
```
¶1: Restate the question and core finding (not a copy of the abstract)
¶2: Mechanism / theoretical contribution
¶3: What we still don't know — honest limitations
¶4: Broader implications for [literature] / [policy] / [future research]
```

---

## Activation Commands

When user asks to write a specific section, respond with:

1. **Draft** — produce a complete first draft of the section
2. **Outline** — produce a structured outline with key arguments for each paragraph
3. **Polish** — improve an existing draft for style, clarity, and journal norms
4. **Review** — evaluate the section against journal standards and suggest revisions

**Default mode**: Draft (unless user specifies otherwise)

---

## Journal-Specific Requirements

### AER / QJE / JPE (Economics)

| Element | Requirement |
|---------|-------------|
| Length | ~15,000 words (main text); appendix unlimited |
| Introduction | ~1,500 words; must include quantified findings |
| Abstract | 150 words; include magnitudes |
| Tables | Not in main text for QJE (supplementary); AER prefers tables in text |
| Equations | Numbered; defined in text |
| Literature | No standalone section — integrate into introduction |
| Identification | Dedicated subsection; explicit parallel trends or exclusion restriction |
| Replication | AER requires data + code deposit (openICPSR) |

### APSR (Political Science)

| Element | Requirement |
|---------|-------------|
| Length | 12,000 words including references |
| Abstract | 150 words; no quantified findings required but encouraged |
| Theory | Dedicated section with numbered hypotheses |
| Tables/Figures | In text; must be self-contained with notes |
| Literature | Integrated into theory; ~40-60 references |
| Identification | In "Research Design" section; parallel trends or design justification |
| Replication | Harvard Dataverse deposit required |

### JOP (Journal of Politics)

| Element | Requirement |
|---------|-------------|
| Length | 10,000 words |
| Style | Similar to APSR; slightly more methodologically flexible |
| Format | Anonymous submission; remove identifying information |

---

## Anti-AI Writing Patterns (Built-in)

This skill produces writing that avoids:
- ❌ "This paper explores / investigates / sheds light on..."
- ❌ "Crucially, importantly, notably, interestingly" as sentence starters
- ❌ Passive voice where active is more direct
- ❌ Hedging every sentence ("may suggest," "could potentially indicate")
- ❌ Over-long sentences with multiple nested clauses
- ❌ "In conclusion, in summary, to summarize" at the start of conclusion sections

Preferred:
- ✅ Direct, declarative sentences: "We find X. Y because Z."
- ✅ Precise quantification: "a [0.66 percentage point / 12%] increase"
- ✅ Active voice: "The analysis shows" not "It is shown that"
- ✅ Varied sentence length: mix short punchy with longer explanatory

---

## References

- **`references/econ-writing-guide.md`** — AER/QJE/JPE submission tips, common referee complaints
- **`references/polisci-writing-guide.md`** — APSR/JOP submission tips, theory section templates

## Related Skills

| Skill | When to Use |
|-------|-------------|
| `writing-anti-ai` | After draft is complete — de-AI the prose |
| `paper-self-review` | Before submission — 6-item quality check |
| `academic-paper-reviewer` | Simulate peer review on the complete draft |
| `results-analysis` | Generate regression tables and figures |
| `causal-inference-analysis` | Write identification strategy code |
| `replication-package` | Prepare code/data for journal submission |
