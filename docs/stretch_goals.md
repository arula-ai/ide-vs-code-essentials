# Stretch Goals
## For Participants Who Complete All Phases with Time Remaining

> Only attempt these after you have completed Phase 6 (git commit).
> These are entirely optional — there are no wrong answers here.

---

## Stretch 1: Add a Data Visualization (10 min)

Create a bar chart directly in the Jupyter notebook.

1. Open `notebooks/exploration.ipynb`
2. Add a new code cell at the bottom (click the `+` button)
3. Open Copilot Chat and use this prompt:

```
Write Python matplotlib code to create a clean horizontal bar chart
showing total revenue by region from a pandas DataFrame.
The DataFrame has columns 'region' and 'total_revenue' (which you will
create from running a SQL query first).
Add a descriptive title, x-axis label, and y-axis label.
Use a blue color palette. Show the chart inline in a Jupyter notebook.
```

4. Before running the chart code, add a cell above it to create the data:

```python
# First: create the regional revenue data
regional_revenue = pd.read_sql_query("""
    SELECT region, SUM(revenue) as total_revenue
    FROM sales_transactions
    GROUP BY region
    ORDER BY total_revenue DESC
""", conn)
```

5. Run both cells — the chart should appear below the code cell
6. **Reflection question:** Does seeing the data visually change how you interpret it?

---

## Stretch 2: Alternative Hypothesis Branch (10 min)

Practice Git branching while thinking analytically.

1. Create a second branch from your current one:
   ```bash
   git checkout -b hypothesis-[yourname]
   ```

2. Add a new section to `notes.md`:

```markdown
---

## Alternative Hypothesis: West Region

### The Initial Finding
West region had the lowest transaction count in Q1 — only 18% of all transactions.

### The Question
Is West *underperforming* — or is it performing *appropriately* for its market?

### What We Would Need to Know
Before calling West an underperformer, we would need:
- Population data or market size estimates by region
- Store count per region (to normalize revenue per location)
- Year-over-year comparison — is West declining or steady?
- Customer satisfaction scores by region

### A Different Interpretation
If West has the fewest stores but the highest average order value ($312 vs North's $268),
the "underperformance" may actually be *premium market positioning*.
A targeted expansion — not a fix — may be the right strategy.

### Recommendation
Do not make a resource reallocation decision based on transaction count alone.
Request store count and market size data from the operations team before Q2 planning.
```

3. Commit this update:
   ```bash
   git add notes.md
   git commit -m "Add alternative hypothesis for West region analysis"
   ```

4. View your branches:
   ```bash
   git branch
   ```

   You should see both `insight-[yourname]` and `hypothesis-[yourname]`.

**Why This Matters:** In real teams, you would open separate Pull Requests for different
analytical directions. Your hypothesis branch shows you are thinking beyond the surface finding.

---

## Stretch 3: Build a Data Dictionary (8 min)

Create a reusable reference document for this dataset.

1. In the Explorer panel, right-click `docs/` → **New File**
2. Name it `data_dictionary.md`
3. Open Copilot Chat and use this prompt:

```
Write a markdown table data dictionary for a retail sales dataset.
Include columns: transaction_id, date, region, product_id, product_category,
units_sold, unit_price, discount_pct, revenue, customer_id.
For each column include:
- Column name
- Data type (string, integer, decimal, date)
- Description (one sentence)
- Example value
- Notes on data quality issues found in this dataset
```

4. Review the output and edit it to reflect what YOU actually found in the data
   (mixed date formats, the "Electronis" typo, the nulls in discount_pct, the negative revenue)

5. Save and commit:
   ```bash
   git add docs/data_dictionary.md
   git commit -m "Add data dictionary for NovaTrend Q1 dataset"
   ```

**Why This Matters:** A data dictionary is one of the most valuable assets a data team can
have. It prevents misunderstandings, speeds up onboarding, and builds trust in the data.
Teams that maintain data dictionaries make better decisions faster.

---

## Stretch 4: Customer Segmentation Analysis (12 min)

Join the customer data and build a value tier model.

1. Open `notebooks/exploration.ipynb`
2. Add a new Markdown cell:
   ```markdown
   ## Customer Segmentation Analysis
   Joining sales data with customer profiles to identify value tiers.
   ```

3. Add a code cell and use this prompt in Copilot Chat:
   ```
   Write Python pandas code to:
   1. Load '../data/raw/customers.csv' into a DataFrame called 'df_customers'
   2. Join it with the existing 'df' DataFrame on 'customer_id' (left join)
   3. Calculate total revenue per customer
   4. Create a new column 'value_tier' with these categories:
      - 'High Value' if total revenue > $500
      - 'Mid Value' if total revenue is $200–$500
      - 'Low Value' if total revenue < $200
   5. Show a summary: count and total revenue for each tier
   6. Also show which 'segment' (Premium/Standard/Basic) maps to each value tier
   ```

4. Run the analysis and answer:
   - Do Premium customers always fall in the High Value tier? (They should — but does the data confirm it?)
   - Are there any "Basic" customers in the High Value tier? What would that mean?

5. Add your findings to `notes.md` under a new section:
   ```markdown
   ## Customer Segmentation Findings
   - High Value customers (>$500): [N] customers, $[X] total revenue
   - Observation about Premium vs High Value alignment: [your insight]
   - Interesting anomaly (if any): [describe]
   ```

---

## Stretch 5: Pre-Lab Pre-Flight Script (5 min)

Create a setup verification script that instructors can share with participants before future sessions.

1. In the root folder, create a new file: `preflight_check.py`
2. Ask Copilot:
   ```
   Write a Python script called preflight_check.py that:
   1. Checks that Python version is 3.10 or higher — prints PASS or FAIL
   2. Checks that pandas is installed — prints PASS or FAIL
   3. Checks that numpy is installed — prints PASS or FAIL
   4. Checks that a folder called 'data/raw' exists — prints PASS or FAIL
   5. Checks that 'data/raw/sales_transactions.csv' exists — prints PASS or FAIL
   6. Prints a final summary: "All checks passed — you are ready for the lab!" or lists failures
   Run this from the project root directory.
   ```

3. Run it: `python preflight_check.py`
4. Commit it: `git add preflight_check.py && git commit -m "Add pre-flight environment check script"`

**Why This Matters:** Pre-flight checks are standard practice for any serious workshop or
onboarding process. They prevent setup issues from eating into session time.

---

## Reflection Prompts (For Personal Notes)

After completing any stretch goal, consider:

1. **What surprised you** about how this workflow actually works?
2. **What would you use** from today in your actual job — even without writing code?
3. **What would you teach** a colleague in 5 minutes based on what you learned today?
4. **What question** do you now know to ask your data team that you did not know before?

---

*Stretch goals are designed to deepen your understanding — not just add more work.
Pick the one that interests you most, not necessarily the one that sounds hardest.*
