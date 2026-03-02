# Sales Performance Insight Brief
**Prepared by:** [Your Full Name]
**Date:** [Today's Date — e.g., February 27, 2026]
**Branch:** insight-[yourfirstname]
**Data Period:** Q1 2024 (January 1 – March 31)
**Data Source:** NovaTrend Retail — sales_transactions.csv (cleaned)

---

## Executive Summary

> *Write 2–3 sentences here. Answer: What did you find? Why does it matter to the business?
> A busy executive should understand the key point in 30 seconds.
> Lead with the most important finding, then the business implication.
> Delete this instruction block when you have written your summary.*

**Example of a strong executive summary:**
*"North region delivered 34% more Q1 revenue than the South, yet West region — despite the lowest
transaction count — shows the highest average order value at $312 per transaction, suggesting
untapped premium demand. Electronics drove 41% of total revenue but received the most discount
pressure, creating a margin risk heading into Q2. Immediate action on discount strategy and
West region expansion could materially impact Q2 targets."*

[Write your own executive summary here — use your actual numbers]

---

## Key Findings

---

### Finding 1: [Write a punchy, specific headline]

> **Examples of strong headlines:**
> - "North Region Leads Q1 Revenue by 34% — But West Shows Highest Basket Size"
> - "Electronics Drives 41% of Revenue Yet Carries the Most Discount Risk"
> - "15% of Discount Values Were Missing — May Understate True Margin Impact"

**Data:**

[Specific numbers that support this finding. Be precise.]

*Example: "North region: $47,200 total revenue (35% of all transactions). South: $35,100.
East: $31,800. West: $24,900 — lowest by transaction count, but $312 average order value
vs North's $268."*

**So What:**

[Why does this matter to the business? What decision does it affect?]

*Example: "North's volume dominance suggests strong market penetration, but West's higher
basket size indicates a premium customer base that may be undertapped."*

**Recommendation:**

[One concrete action leadership should consider]

*Example: "Investigate whether West's low transaction count reflects market size constraints
or underinvestment in sales and marketing. A targeted Q2 campaign could test elasticity."*

---

### Finding 2: [Headline]

**Data:**

[Specific numbers]

**So What:**

[Business implication]

**Recommendation:**

[One concrete action]

---

### Finding 3: [Headline]

**Data:**

[Specific numbers — if you ran the discount analysis or customer value query, use those here.
Otherwise, use your data quality finding as Finding 3.]

**So What:**

[Business implication]

**Recommendation:**

[One concrete action]

---

### Finding 4 (Optional): [Headline]

**Data:**

**So What:**

**Recommendation:**

---

## Data Quality Notes

> *Document what you found and fixed. This section builds trust in your numbers.
> A report that acknowledges data quality issues is more credible than one that doesn't.*

| Issue Found | Volume | How It Was Handled |
|---|---|---|
| Mixed date formats (3 formats: YYYY-MM-DD, MM/DD/YYYY, Mon DD YYYY) | All 200 rows affected | Standardized to YYYY-MM-DD using pandas |
| Inconsistent product_category casing (Electronics / ELECTRONICS / electronics) | [N] rows | Converted to Title Case |
| Typo in product_category: "Electronis" | [N] rows | Corrected to "Electronics" |
| Missing discount_pct values | ~15% of rows (~30 rows) | Filled with 0 (business rule: no discount recorded = 0% applied) |
| Negative revenue rows (product returns) | [N] rows | Separated into returns dataset; excluded from revenue analysis |
| [Any other issues you found] | | |

**Confidence in the numbers:** [High / Medium — explain briefly]

---

## Methodology

> *2–3 sentences on what tools and approach you used. Keep it factual and brief.*

*Example: "Q1 sales data was cleaned using Python (pandas library) to standardize date
formats, resolve category inconsistencies, and separate product returns. Business insights
were generated using SQL queries executed via SQLite in a Jupyter notebook. The report
was written in Markdown using VS Code with GitHub Copilot assistance for code generation
and executive summary drafting."*

[Write your methodology here]

**Tools used:**
- [ ] Python (pandas) — data cleaning
- [ ] SQL (SQLite via Python) — business analysis
- [ ] GitHub Copilot — code generation assistance
- [ ] VS Code — development environment
- [ ] Git — version control

---

## Next Steps

> *What would you want to investigate further with more time or data?
> Be specific — vague next steps don't drive action.*

- [ ] [Recommended action 1 — e.g., "Investigate West region market size data to determine if low transaction count reflects market constraints or underinvestment"]
- [ ] [Recommended action 2 — e.g., "Analyze Q2 vs Q1 discount strategy to test whether Electronics discounting drove volume or simply eroded margin"]
- [ ] [Data needed — e.g., "Obtain store count by region to normalize revenue per location"]
- [ ] [Follow-on analysis — e.g., "Run customer segmentation to identify Premium customers in West region and test a targeted outreach campaign"]

---

*Report prepared as part of the AI-Powered Analyst Workflow Lab.*
*Tools: VS Code · GitHub Copilot · Python · SQL · Git*
