
Top 3 Business Questions to Investigate

- Which products and product categories drive the most revenue and profit? (metrics: total revenue, units_sold, average selling price, revenue share, estimated margin)
- How effective are discounts at increasing units sold and net revenue? (metrics: discount_pct vs units_sold lift, revenue per transaction, incremental margin)
- Which regions and categories are over/under-performing and where is there growth opportunity? (metrics: revenue by region × category, MoM growth, regional share)

Data Oddities Observed

- Missing or blank `units_sold` paired with negative `revenue` (e.g., T020, T079, T082, T102, T115, T146, T160). Likely returns/refunds recorded inconsistently.
- Inconsistent `product_category` values and typos (case variants and misspellings: HOME & GARDEN / home & garden / Electronis / ELECTRONICS / sports & fitness). This will break aggregations.
- Mixed `date` formats (ISO `YYYY-MM-DD`, `Jan 04 2024`, `03/27/2024`, `Mar 22 2024`) — needs normalization to a single date type.
- Many blank `discount_pct` values; must decide whether blank means 0 (no discount) or unknown.
- Some rows show revenue mismatches or negative revenue with missing numeric fields; recompute `expected_revenue = units_sold * unit_price * (1 - discount_pct)` and flag mismatches.

Recommended next steps

- Normalize `product_category` values and fix typos.
- Parse and standardize `date` to `YYYY-MM-DD`.
- Decide handling for blank `discount_pct` (0 vs NULL) and fill accordingly.
- Infer or tag return transactions where revenue < 0; populate or mark `units_sold` consistently.
- Recompute and validate `revenue`, then generate a small data-quality report before analysis.
