# Business Context: NovaTrend Retail — Q1 Sales Review

---

## Your Role Today

You are a **Business Analyst at NovaTrend Retail**, a mid-sized retail company
operating across four regions: **North, South, East, and West**.

You have been brought in specifically because leadership believes better data literacy
across business teams will lead to faster, smarter decisions. Today, you will do exactly
what your data team does — except with AI assistance that lets you move much faster.

---

## Why This Matters

Before we start, a quick note on why this workflow is worth your time:

- Companies that invest in data-driven decisions outperform peers by **5-6% in productivity**
  (McKinsey, 2022)
- The biggest bottleneck in most analytics pipelines is **not the data or the tools —
  it is the communication gap between business and technical teams**
- After this lab, you will speak the language your data teams use every day

---

## The Business Situation

The **Chief Revenue Officer (CRO)** needs to walk into next week's executive strategy meeting
with clear, data-backed answers to four critical questions. Your team has Q1 transaction data,
but it is messy — dates in different formats, inconsistent product categories, missing values.

**You have been asked to:**
1. Clean and validate the data so it can be trusted
2. Run analysis to surface the four key answers
3. Write a concise insight brief the CRO can present to the board

**You have 60 minutes.** This is a realistic deadline — tight, but achievable with the right tools.

---

## The Four Questions Leadership Needs Answered

### Question 1: Regional Performance
> **"Which regions are outperforming or underperforming — and why does it matter?"**

Are there regional trends worth acting on? Should we shift marketing spend or sales targets?

### Question 2: Product Category Performance
> **"Which product categories drive the most revenue?"**

Where should we focus promotions next quarter? Are we investing in the right product mix?

### Question 3: Customer Segmentation
> **"Are there customer segments worth targeting differently?"**

Who are our best customers? Are we retaining Premium customers at the right rate?

### Question 4: Data Quality
> **"Can we trust the numbers we're presenting to the board?"**

This is often the most overlooked question — and the most important. A finding built on
bad data is worse than no finding at all.

---

## Your Deliverable

A short **Insight Report** (written in Markdown format) containing:

- **3–5 headline findings** — specific numbers, not vague observations
- **One actionable recommendation** per finding
- **Clear, jargon-free language** suitable for an executive audience
- **A data quality section** noting any issues discovered and how they were handled

**Standard:** If you handed this report to the CRO right now, would she be able to
present it with confidence? That is your bar.

---

## The Data You Have Access To

| File | Description | Status |
|---|---|---|
| `data/raw/sales_transactions.csv` | ~200 rows of Q1 transaction records | Messy — needs cleaning |
| `data/raw/customers.csv` | ~50 customer records with segment info | Has some issues |
| `data/raw/products.csv` | ~30 product records with cost and category | Clean reference table |

**Important:** Do not edit the files in `data/raw/`. These are your source of truth.
Your cleaning script will create a new file in `data/processed/`.

---

## A Note on AI Assistance

You have access to **GitHub Copilot**. This is the same tool your engineering and data teams
use every day. Think of Copilot as a very capable, very fast intern who:

- Knows a lot of syntax and patterns
- Can suggest code, rewrite text, and answer questions
- **Can also be confidently wrong** — always evaluate its output

Your value as a business analyst is your judgment — understanding what the numbers mean,
whether they make business sense, and what actions they should drive.

**Copilot helps you move faster. Your expertise makes the output meaningful.**

---

## Quick Business Vocabulary

| Term | Plain English |
|---|---|
| Repository | Your project folder with full version history |
| Branch | A named copy of the project where you can work safely |
| Commit | A saved checkpoint — like "Save As" with a description |
| DataFrame | A table of data in Python (like a spreadsheet in code) |
| SQL Query | A precise question you ask a database ("Show me revenue by region") |
| Markdown | Simplified formatting — like a stripped-down Word document |

---

## Timeline

| Phase | Activity | Duration |
|---|---|---|
| 1 | Warm-Up — Orient in VS Code | 5 min |
| 2 | Explore — Form questions with Copilot | 10 min |
| 3 | Clean — Fix the raw data | 15 min |
| 4 | Analyze — Find insights with SQL | 15 min |
| 5 | Document — Write the insight report | 10 min |
| 6 | Collaborate — Commit your work | 5 min |
| **Total** | | **60 min** |

**The brief is due end of session. Let's go.**
