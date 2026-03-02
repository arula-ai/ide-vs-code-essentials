# VS Code Essentials for Analysts — Participant Guide

**4 Labs · 15 minutes each · 60 minutes total**

---

## Pre-Lab Setup

Complete **before** the session starts.

### Required Software

| Software | Download |
|---|---|
| VS Code | code.visualstudio.com |
| Python 3.10+ | python.org/downloads |
| Git | git-scm.com |

---

### Installation

**Mac** — Open Terminal (Cmd+Space → type "Terminal"):

```bash
pip3 install pandas openpyxl matplotlib numpy
```

**Windows** — Open Command Prompt (Start → type "cmd"):

```bash
pip install pandas openpyxl matplotlib numpy
```

**Both OS** — Clone the repo and generate data:

```bash
git clone [your-repo-url]
cd vscode-analyst-ai-lab
```

| | Mac | Windows |
|---|---|---|
| Generate data | `python3 generate_sample_data.py` | `python generate_sample_data.py` |

---

### OS Keyboard & Command Reference

| Action | Mac | Windows |
|---|---|---|
| Open terminal in VS Code | Ctrl+` | Ctrl+` |
| Open Copilot Chat | Cmd+Shift+I | Ctrl+Shift+I |
| Command Palette | Cmd+Shift+P | Ctrl+Shift+P |
| Save file | Cmd+S | Ctrl+S |
| Preview Markdown | Cmd+Shift+V | Ctrl+Shift+V |
| Split editor panes | Cmd+\ | Ctrl+\ |
| Create virtual env | `python3 -m venv venv` | `python -m venv venv` |
| Activate virtual env | `source venv/bin/activate` | `venv\Scripts\activate` |
| Run Python script | `python3 script.py` | `python script.py` |

---

---

## Lab 1 — Workspace, Data Preview & Documentation

**15 min · Goal:** Open VS Code, read the project brief, inspect raw data, and document your observations using Markdown and Copilot.

---

**1.** Open VS Code → **File → Open Folder** → select `vscode-analyst-ai-lab` → **Open**

**2.** Click **Yes, I trust the authors** if prompted

**3.** Click **Install** on the extension popup (bottom-right)
> No popup? → Cmd+Shift+P / Ctrl+Shift+P → `Extensions: Show Recommended Extensions` → install all

**4.** Open `docs/business_context.md` → press Cmd+Shift+V / Ctrl+Shift+V to preview
→ Read it completely. This is your project brief.

**5.** Open `data/raw/sales_transactions.csv` → scroll through and note:
- Column names and their data types
- Any blank cells (look in `discount_pct`)
- Inconsistencies in `product_category` (different cases, spelling)
- Any negative values in `revenue`

**6.** Open Copilot Chat → Cmd+Shift+I / Ctrl+Shift+I → paste this prompt:

```
I have a CSV file with retail sales data for NovaTrend Retail.
Columns: transaction_id, date, region, product_id, product_category,
units_sold, unit_price, discount_pct, revenue, customer_id.

What are the 5 most important business questions I should investigate?
Focus on questions that would matter to a Chief Revenue Officer.
```

**7.** In the Explorer (left sidebar), right-click the root folder → **New File** → name it `notes.md`

**8.** Paste this into `notes.md`:

```markdown
# Analyst Notes — NovaTrend Retail Q1

**Analyst:** [Your Name]
**Date:** [Today's Date]

---

## Project Overview

NovaTrend Retail needs a Q1 analysis brief before the executive strategy meeting.
This document captures my analysis approach, data observations, and key findings.

---

## Business Questions

1. [Copy your top question from Copilot's response]
2. Which product categories drive the most revenue?
3. Do discounts actually increase revenue?

---

## Data Dictionary — sales_transactions.csv

| Column | Type | Description | Example |
|---|---|---|---|
| transaction_id | Text | Unique ID per sale | T001 |
| date | Date | Transaction date (mixed formats) | 2024-01-15 |
| region | Text | Sales region | North |
| product_category | Text | Product type | Electronics |
| units_sold | Number | Units per transaction | 3 |
| discount_pct | Number | Discount applied (null = 0%) | 0.15 |
| revenue | Number | Revenue (negative = return) | 249.99 |

---

## Data Quality Issues

- [ ] Date column — 3 mixed formats (ISO, US, English)
- [ ] product_category — inconsistent casing + typo "Electronis"
- [ ] ~15% of discount_pct values are null
- [ ] Negative revenue rows = product returns (need to be separated)

---

## Business Insights Found

### Finding 1: [Headline — e.g., "North Region Leads Revenue by 34%"]
- **Data:** [Numbers from your query results]
- **So what:** [Business implication]

### Finding 2: [Headline]
- **Data:**
- **So what:**
```

**9.** Save → Cmd+S / Ctrl+S → preview → Cmd+Shift+V / Ctrl+Shift+V

**10.** Open Copilot Chat → paste this prompt → replace the Project Overview text in `notes.md` with Copilot's version:

```
Rewrite this project overview in 2 professional sentences for a business analyst.
Keep it concise and specific to a Q1 retail sales analysis:

"NovaTrend Retail needs a Q1 analysis brief before the executive strategy meeting.
This document captures my analysis approach, data observations, and key findings."
```

---

✅ **Done when:** `notes.md` has a data dictionary, 3 business questions, 4 quality issues checked off, and a Copilot-improved project overview.

---

---

## Lab 2 — Git: Branch, Commit & Push

**15 min · Goal:** Create a personal branch, update documentation, commit your changes, and push to the repo.

---

**1.** Open terminal → Ctrl+`

**2.** Check current branch:

```bash
git status
```

**3.** Create your personal branch — replace `yourname` with your first name (lowercase):

```bash
git checkout -b analysis-yourname
```

**4.** Confirm you are on your new branch:

```bash
git status
```

**5.** Open `notes.md` → add analyst observations at the bottom:

```markdown
---

## Analyst Observations

**Reviewed by:** [Your Name] | **Date:** [Today]

Initial scan identified 4 data quality issues that must be fixed before analysis:
1. Mixed date formats (ISO / US / English) — inconsistent grouping risk
2. Inconsistent product_category casing + typo "Electronis"
3. ~15% null discount_pct — business rule: treat as 0% discount
4. Negative revenue rows = product returns — must be separated before aggregation
```

**6.** Save → Cmd+S / Ctrl+S

**7.** Open Copilot Chat → paste this prompt to generate your commit message:

```
Write a one-line Git commit message under 72 characters, imperative tense,
for an analyst who added data quality observations and analyst notes
to a documentation file called notes.md.
```

**8.** Stage all changes:

```bash
git add .
```

**9.** Commit using Copilot's message (or your own):

```bash
git commit -m "Add analyst observations and data quality notes — YourName"
```

**10.** Verify the commit:

```bash
git log --oneline
```

**11.** Push your branch:

```bash
git push origin analysis-yourname
```

> First push on a new branch? Run:
> ```bash
> git push --set-upstream origin analysis-yourname
> ```

---

✅ **Done when:** `git log --oneline` shows your commit at the top.

| Problem | Fix |
|---|---|
| `nothing to commit` | Save the file first (Cmd+S) → then `git add .` |
| `branch already exists` | Use `analysis-yourname-2` |
| `no upstream branch` | `git push --set-upstream origin analysis-yourname` |

---

---

## Lab 3 — Data Cleaning, SQL Analysis & Findings

**15 min · Goal:** Clean all 4 data quality issues with Copilot, run the script, query clean data in the notebook, and document 2 business findings.

---

### Part A — Clean the Data (scripts/data_cleaning.py)

**1.** Open `scripts/data_cleaning.py` → find `# ── TODO 1`

**2.** Open Copilot Chat → paste each prompt below → copy the result → paste it under the matching TODO comment → save after each:

**TODO 1** — Fix mixed date formats:

```
Write Python pandas code to parse a column named 'date' in a DataFrame 'df'
with mixed formats: '2024-01-15', '01/15/2024', 'Jan 15 2024'.
Convert all to YYYY-MM-DD string format. Store back in df['date'].
```

**TODO 2** — Standardize product categories:

```
Write Python pandas code to:
1. Strip whitespace from 'product_category' in DataFrame 'df'
2. Convert all values to Title Case
3. Replace the typo 'Electronis' with 'Electronics'
Store back in df['product_category'].
```

**TODO 3** — Fill missing discount values:

```
Write one line of Python pandas code to fill all NaN values
in the 'discount_pct' column of DataFrame 'df' with 0.
Store the result back in the column.
```

**TODO 4** — Separate product returns:

```
Write Python pandas code to:
1. Create a new DataFrame 'returns_df' containing all rows
   where 'revenue' is negative in DataFrame 'df'
2. Remove those rows from 'df' (keep only positive revenue)
3. Print how many return rows were found
```

---

### Part B — Run the Script

**3.** Open terminal → run:

| Mac | Windows |
|---|---|
| `python3 scripts/data_cleaning.py` | `python scripts\data_cleaning.py` |

**4.** Confirm the output shows:
```
✅ Cleaning complete!
   Clean data saved: 192 rows
   Output: data/processed/clean_sales.csv
```

**5.** In Explorer, expand `data/processed/` → click `clean_sales.csv` → verify dates are uniform and categories are consistent

| Error | Fix |
|---|---|
| `ModuleNotFoundError: pandas` | `pip3 install pandas` (Mac) or `pip install pandas` (Windows) |
| `FileNotFoundError` | Run from the project root, not from inside `scripts/` |
| `NameError: returns_df` | TODO 4 code is incomplete — go back and complete it |

---

### Part C — SQL Analysis in Notebook

**6.** Open `notebooks/exploration.ipynb`

**7.** Run these setup cells in order — press **Shift+Enter** on each:
- **Cell 3** — loads `clean_sales.csv` into a DataFrame
- **Cell 5** — sets up the SQL engine (`✅ SQL engine ready`)
- **Cell 7** — defines the `run_query()` helper function

**8.** Open `sql/analysis_queries.sql` → find `-- TODO: Write Query 1 here`
→ Open Copilot Chat → paste this prompt → copy SQL → paste under the TODO:

```
Write SQL to calculate total revenue grouped by 'region'
from a table called 'sales_transactions'.
Order by total_revenue descending. Label the sum 'total_revenue'.
```

**9.** Find `-- TODO: Write Query 2 here` → paste this prompt → copy SQL → paste under the TODO:

```
Write SQL to find the top 5 product_category values by total revenue
from 'sales_transactions'.
Include SUM(revenue) as total_revenue and SUM(units_sold) as total_units.
Order by total_revenue descending.
```

**10.** In the notebook, paste and run each query (Shift+Enter after each cell):

```python
query_1 = """
-- paste your Query 1 SQL here
"""
run_query(query_1)
```

```python
query_2 = """
-- paste your Query 2 SQL here
"""
run_query(query_2)
```

---

### Part D — Document Your Findings

**11.** Back in `notes.md`, fill in the **Business Insights Found** section with real numbers from your query results:

```
Example: "North Region: $47,200 in Q1 — 34% more than South ($35,100)"
```

**12.** Save → Cmd+S / Ctrl+S → commit your work:

```bash
git add .
git commit -m "Add data cleaning and SQL analysis results — YourName"
```

---

✅ **Done when:** `clean_sales.csv` exists, 2 query results show in the notebook, and 2 findings with numbers are in `notes.md`.

---

---

## Lab 4 — Spreadsheet Analysis & Insight Report

**15 min · Goal:** Build a reusable analysis script with Copilot, produce a chart, and write an executive-ready insight report.

---

### Part A — Virtual Environment Setup

**1.** Open terminal → confirm you are in the project root:

```bash
pwd
```

> Should end with `vscode-analyst-ai-lab`. If not: `cd path/to/vscode-analyst-ai-lab`

**2.** Create and activate a virtual environment:

| Step | Mac | Windows |
|---|---|---|
| Create | `python3 -m venv venv` | `python -m venv venv` |
| Activate | `source venv/bin/activate` | `venv\Scripts\activate` |

> Confirm: `(venv)` appears at the start of your terminal prompt

**3.** Install packages:

| Mac | Windows |
|---|---|
| `pip3 install pandas openpyxl matplotlib` | `pip install pandas openpyxl matplotlib` |

---

### Part B — Build the Analysis Script (scripts/spreadsheet_analysis.py)

**4.** Open `scripts/spreadsheet_analysis.py` → find the 4 `# ── TODO` sections

**5.** Open Copilot Chat → paste each prompt → copy result → paste under the matching TODO → save:

**TODO 1** — Load the spreadsheet:

```
Write Python pandas code to load an Excel file named 'sales_data.xlsx'
from folder 'data/raw/' into a DataFrame called 'df'.
Specify sheet_name='Sales Transactions'.
Print the shape and first 5 rows.
```

**TODO 2** — Clean column names:

```
Write Python pandas code to clean all column names in DataFrame 'df':
1. Strip whitespace from each column name
2. Replace spaces with underscores
3. Convert to lowercase
Print the cleaned column names.
```

**TODO 3** — Parse dates and summarize:

```
Write Python pandas code to:
1. Convert the 'date' column in DataFrame 'df' to datetime using format='mixed'
2. Extract month number into a new column 'month'
3. Print a summary table: total revenue and total units_sold grouped by month
4. Print: total revenue, average transaction value, and transaction count
```

**TODO 4** — Build a chart:

```
Write Python matplotlib code to:
1. Create a bar chart of total revenue by product_category from DataFrame 'df'
2. Title: "Revenue by Product Category — Q1"
3. X-axis: "Category", Y-axis: "Total Revenue ($)"
4. Rotate x-axis labels 45 degrees
5. Save to 'data/processed/revenue_by_category.png'
6. Call plt.close() after saving. Print "Chart saved".
```

**6.** Run the script:

| Mac | Windows |
|---|---|
| `python3 scripts/spreadsheet_analysis.py` | `python scripts\spreadsheet_analysis.py` |

**7.** In Explorer, open `data/processed/revenue_by_category.png` to verify the chart

| Error | Fix |
|---|---|
| `ModuleNotFoundError: pandas` | `(venv)` not active — re-run the activate command |
| `FileNotFoundError: sales_data.xlsx` | Run `python3 generate_sample_data.py` from the project root |
| `KeyError: 'date'` | Check column names printed in TODO 1 — adjust if different |
| Chart not saved | Add `plt.close()` after `plt.savefig(...)` in TODO 4 |

---

### Part C — Write the Insight Report

**8.** Open `docs/insight_report_template.md` → press Cmd+\ / Ctrl+\ to split the editor
→ Press Cmd+Shift+V / Ctrl+Shift+V on the right pane to preview as you type

**9.** Fill in the template using your findings from Lab 3 and the chart from this lab:

- **Header** — your name, today's date, branch name (`analysis-yourname`)
- **Finding 1** — use the revenue-by-region result (e.g., "North leads at $47K, +34% vs South")
- **Finding 2** — use the top categories result (e.g., "Electronics drives 42% of total revenue")
- **Data Quality Notes** — list the 4 issues you fixed in Lab 3

**10.** Open Copilot Chat → draft your executive summary first, then paste this prompt to refine it:

```
Rewrite this executive summary for a senior leadership audience.
Requirements:
- Maximum 3 sentences
- Lead with the single most important finding
- Include specific numbers from the original
- Focus on business impact, not methodology

[paste your draft executive summary here]
```

**11.** Replace your draft with Copilot's version → edit until it sounds natural → save

---

### Part D — Final Commit

**12.** Commit everything:

```bash
git add .
git commit -m "Add analysis script, chart, and insight report — YourName"
```

**13.** Push all your work:

```bash
git push origin analysis-yourname
```

---

✅ **Done when:** Chart exists in `data/processed/`, insight report has 2 findings with numbers and an executive summary, and `git log --oneline` shows your final commit.

---

---

## Wrap-Up

| What You Built | Lab |
|---|---|
| Markdown data dictionary + Copilot-improved documentation | Lab 1 |
| Personal Git branch with committed analyst observations | Lab 2 |
| Clean dataset, SQL queries, and 2 business findings | Lab 3 |
| Reusable analysis script, chart, and executive insight report | Lab 4 |

**Follow-up courses:** SQL in VS Code · Python for Analysts · Documentation in Markdown · Copilot for Analytics Workflows

**Stretch goals:** See `docs/stretch_goals.md` — includes data visualization, customer segmentation, alternative hypothesis branching, and more.

---

*Reference files: `docs/git_basics_cheat_sheet.md` · `docs/copilot_prompt_library.md` · `docs/quick_reference_card.md`*
