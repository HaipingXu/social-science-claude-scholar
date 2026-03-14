# Single-Source-of-Truth Protocol

Every artifact has exactly one authoritative source. Derived versions are generated from it, never edited directly.

---

## Paper Writing

**Authoritative source: `.tex` file**

- LaTeX `.tex` is the master document
- Never edit `.docx` exports or Overleaf PDFs directly — they are derived outputs
- If a collaborator edits a `.docx`, merge changes back into `.tex` as the primary step
- Figures: the script that generates the figure is authoritative, not the `.pdf` or `.png` output

---

## Analysis (Stata → Python Transition)

**Authoritative source during transition: Stata `.do` file**
**Authoritative source after replication verified: Python `.py` script**

### Transition Protocol

1. **Stata is authoritative** until Python replication is verified
2. Python script must replicate Stata results within tolerance before Python becomes authoritative
3. Verify replication:

| Quantity | Tolerance |
|----------|-----------|
| Point estimates | < 0.01 |
| Standard errors | < 0.05 |
| Sample size N | Exact match |
| Significance levels | Same |

4. After replication verified: commit Stata as frozen reference, mark Python as new authoritative source
5. **Never modify both simultaneously** — pick one, update the other to match

### Replication Failure Protocol

- Do NOT proceed to extensions or new specifications
- Isolate which step diverges (sample, variable definition, SE computation, package defaults)
- Document investigation in session log even if unresolved
- Common Stata→Python traps (see `data-analysis` skill)

---

## Data

**Authoritative source: `data/raw/` files**

- `data/raw/` is read-only after initial download — never overwrite
- `data/processed/` is derived from `raw/` via reproducible scripts
- If raw data changes, create a new versioned subfolder: `data/raw/v2/`
- Git-track scripts that produce processed data; DVC-track the data files themselves

---

## Configuration

**Authoritative source: config files / CLAUDE.md / CLAUDE.zh-CN.md**

- `CLAUDE.md` (English) is the primary authoritative config
- `CLAUDE.zh-CN.md` is a synchronized translation — must be updated whenever `CLAUDE.md` changes
- Never let the two diverge by more than one session

---

## Derived Output Rule

For any derived file (PDF, `.docx`, `.html`, `.png`, `.csv`):
- Add a comment or header: `# Auto-generated from [source file] — do not edit directly`
- If the derived file must be edited manually, immediately update the source

---

## Conflict Resolution

When source and derived copy diverge:
1. Identify which is more recent and more authoritative
2. Update the derived copy from the source (never the reverse)
3. Log the conflict resolution in the session log
