# Copilot Prompt Library
## VS Code Essentials for Analysts — NovaTrend Retail

> A curated collection of ready-to-use prompts for every lab.
> Copy a prompt, paste it into Copilot Chat, and adapt the result to your needs.
> **Always review and edit Copilot's output — do not paste it in blindly.**

---

## How to Use This Library

1. Find the prompt that matches what you are trying to do
2. Copy the prompt text
3. Open Copilot Chat (`Cmd+Shift+I` / `Ctrl+Shift+I`)
4. Paste and press Enter
5. Review the response — edit anything that does not fit your context
6. If the first answer is not quite right, add a follow-up message refining your request

---

## Lab 1: Documentation Prompts

### Improve Documentation Clarity
```
I am writing analyst notes for a retail sales analysis project.
Here is my project overview section:

[paste your text here]

Rewrite this in 2–3 sentences that are clearer and more professional.
Keep it concise and appropriate for a technical documentation file.
```

### Generate a Data Dictionary Table
```
Write a markdown table data dictionary for these columns from a retail sales CSV:
transaction_id, date, region, product_id, product_category, units_sold,
unit_price, discount_pct, revenue, customer_id.
Include: column name, data type, business description, example value.
```

### Write a Requirements Document Section
```
I am documenting business requirements for a Q1 retail sales analysis.
Write a markdown section that describes what the analysis should include:
- What business questions to answer
- What data is available
- What the output deliverable should be
Keep it short — 3 to 5 bullet points per section.
```

### Generate Process Documentation
```
Write a step-by-step analyst process document in markdown for this workflow:
receiving raw sales data → identifying data quality issues → cleaning the data →
running analysis queries → writing an insight report → sharing with stakeholders.
Use numbered steps and include brief descriptions for each.
```

---

## Lab 2: Git & Repository Prompts

### Explain a Git Concept in Plain Language
```
Explain what a Git branch is to a business analyst with no software development
background. Use an analogy to a spreadsheet or document workflow they would
recognize. Keep it under 3 sentences.
```

### Write a Commit Message
```
Write a clear Git commit message for an analyst who:
- Updated the data dictionary in notes.md
- Added analyst observations to business_context.md
- Fixed two column name typos in the documentation

The message should be one line, under 72 characters, written in imperative form
(e.g., "Add..." not "Added...").
```

### Understand What Changed in a File
```
I am looking at this diff from a Git repository. Explain what changed
in plain English suitable for a business analyst:

[paste git diff output here]
```

---

## Lab 3: Analysis Task Prompts

### Generate Data Exploration Prompts
```
I have a CSV file with retail sales data for a company called NovaTrend Retail.
The columns are: transaction_id, date, region, product_id, product_category,
units_sold, unit_price, discount_pct, revenue, customer_id.

What are the 5 most important business questions I should investigate?
Please focus on questions that would matter to a Chief Revenue Officer.
```

### Prioritize Questions for Leadership
```
Which two of those questions would be most urgent if the CRO is presenting
to the board next week about Q1 performance?
```

### Identify Data Quality Risks
```
What are the most common data quality issues in retail sales transaction datasets?
Which issues would have the biggest impact on revenue reporting accuracy?
```

### Explain Code in Plain Language
```
Explain what this Python code does in plain English suitable for a
business analyst with no coding background. Avoid jargon.
Describe what it does to the data, step by step.

[paste your code here]
```

### Rewrite Outdated SQL Logic
```
Here is a SQL query written for MySQL. Rewrite it to work with SQLite,
which uses strftime() instead of MONTH() and DATE_FORMAT().

[paste your SQL here]
```

### Generate Field Definitions
```
Write field definitions for a business analyst audience for these columns
from a retail sales transaction dataset:
transaction_id, discount_pct, revenue, product_category.

For each field include: field name, data type, business definition (1 sentence),
example value, and common analyst questions about this field.
Format as a markdown table.
```

---

## Lab 3: SQL Prompts

### Query 1 — Revenue by Region
```
Write SQL to calculate the SUM of a column named 'revenue' grouped by 'region'
from a table called 'sales_transactions'.
Order results by total revenue descending.
Label the sum column as 'total_revenue'.
```

### Query 2 — Top Product Categories
```
Write SQL to find the top 5 product_category values by total revenue
from a table called 'sales_transactions'.
Include SUM(revenue) as total_revenue and SUM(units_sold) as total_units.
Order by total_revenue descending.
```

### Query 3 — Transaction Count by Region
```
Write SQL to count the number of transactions per region
from a table called 'sales_transactions'.
Order by transaction count descending.
Label the count column as 'transaction_count'.
```

### Query 4 — Monthly Revenue Trend (SQLite)
```
Write SQLite SQL to extract the month from a column named 'date' formatted as
YYYY-MM-DD, and calculate total revenue per month from 'sales_transactions'.
Use strftime('%m', date) for the month extraction.
Order by month ascending.
Note: This is SQLite — do NOT use MONTH() function.
```

### Query 5 — Discount Impact Analysis
```
Write SQL to compare average revenue per transaction between:
1. Orders that had a discount applied (discount_pct > 0)
2. Orders with no discount (discount_pct = 0)
From the table 'sales_transactions'.
Show: the discount group, count of transactions, average revenue, and total revenue.
```

---

## Lab 4: Spreadsheet Analysis Prompts

### Load a Spreadsheet
```
Write Python pandas code to load an Excel file named 'sales_data.xlsx'
from a folder called 'data/raw/' into a DataFrame called 'df'.
Specify sheet_name='Sales Transactions' to load the correct sheet.
Print the shape (number of rows and columns) and first 5 rows.
```

### Clean Column Names
```
Write Python pandas code to clean all column names in a DataFrame called 'df':
1. Strip leading and trailing whitespace from each column name
2. Replace spaces with underscores
3. Convert all column names to lowercase
Print the cleaned column names.
```

### Parse Dates and Summarize
```
Write Python pandas code to:
1. Convert a column named 'date' in DataFrame 'df' to datetime format.
   The dates have mixed formats — use format='mixed' to handle this.
2. Extract the month number into a new column called 'month'
3. Print a summary table showing total revenue and total units_sold per month
4. Print overall summary statistics: total revenue, average transaction value,
   and transaction count
```

### Build a Bar Chart
```
Write Python matplotlib code to:
1. Create a bar chart showing total revenue by product_category from DataFrame 'df'
2. Add a title: "Revenue by Product Category — Q1"
3. Label the x-axis "Category" and y-axis "Total Revenue ($)"
4. Rotate x-axis labels by 45 degrees for readability
5. Save the chart as 'data/processed/revenue_by_category.png'
6. Print "Chart saved" when complete
```

### Summarize Spreadsheet Quality Issues
```
I have a pandas DataFrame loaded from an Excel spreadsheet.
Here are the column names and a sample of the data:

[paste df.dtypes or df.head() output here]

What data quality issues should I look for before analyzing this data?
List the most common issues analysts encounter in Excel exports.
```

### Make a Script Reusable for Any Spreadsheet
```
I have a Python script that analyzes a specific spreadsheet.
Rewrite the file-loading section so it accepts the filename as a
command-line argument (using sys.argv) instead of a hardcoded filename.
Add a helpful error message if no filename is provided.
```

---

## Phase 2: Data Exploration Prompts

### Generate Business Questions
```
I have a CSV file with retail sales data for a company called NovaTrend Retail.
The columns are: transaction_id, date, region, product_id, product_category,
units_sold, unit_price, discount_pct, revenue, customer_id.
What are the 5 most important business questions I should investigate?
Please focus on questions that would matter to a Chief Revenue Officer.
```

### Prioritize Questions for Leadership
```
Which two of those questions would be most urgent if the CRO is presenting
to the board next week about Q1 performance?
```

### Understand a Column
```
In a retail business dataset, what does a column called 'discount_pct' typically
represent? What business rules usually apply to how it is collected and recorded?
```

### Identify Data Quality Risks
```
What are the most common data quality issues in retail sales transaction datasets?
Which issues would have the biggest impact on revenue reporting accuracy?
```

### Generate a Data Dictionary
```
Write a markdown table data dictionary for these columns from a retail sales CSV:
transaction_id, date, region, product_id, product_category, units_sold,
unit_price, discount_pct, revenue, customer_id.
Include: column name, data type, description, example value, and potential quality issues.
```

### Understand Negative Revenue
```
In a retail sales dataset, what does a negative value in a revenue column
typically represent? How should it be handled in analysis?
```

---

## Phase 3: Data Cleaning Prompts

### Fix Mixed Date Formats
```
Write Python pandas code to parse a column named 'date' in a DataFrame called 'df'
that contains mixed date formats including:
  - '2024-01-15' (ISO format)
  - '01/15/2024' (US format)
  - 'Jan 15 2024' (English format)
Convert all values to standard Python datetime first, then format as YYYY-MM-DD string.
Store the result back into df['date'].
```

### Standardize Category Names
```
Write Python pandas code to:
1. Strip leading and trailing whitespace from the 'product_category' column in DataFrame 'df'
2. Convert all values to Title Case
3. Replace the misspelled value 'Electronis' with 'Electronics'
Store the cleaned result back into df['product_category'].
```

### Fill Missing Numeric Values
```
Write one line of Python pandas code to fill all NaN (missing) values in
a column named 'discount_pct' in DataFrame 'df' with the value 0.
Store the result back in the column.
```

### Separate Returns from Sales
```
Write Python pandas code to:
1. Create a new DataFrame called 'returns_df' containing all rows where
   the 'revenue' column is negative in DataFrame 'df'
2. Remove those negative-revenue rows from 'df' (keep only positive revenue)
3. Print how many return rows were found
```

### Strip Column Name Whitespace
```
Write Python pandas code to strip leading and trailing whitespace from
all column names in DataFrame 'df'. This handles cases where a column
was imported with an extra space in its name.
```

### Explain Code in Plain English
```
Explain what this Python code does in plain English suitable for a
non-technical business manager. Avoid jargon.

[paste your code here]
```

---

## Phase 4: SQL Analysis Prompts

### Query 1 — Revenue by Region
```
Write SQL to calculate the SUM of a column named 'revenue' grouped by 'region'
from a table called 'sales_transactions'.
Order results by total revenue descending.
Label the sum column as 'total_revenue'.
```

### Query 2 — Top Product Categories
```
Write SQL to find the top 5 product_category values by total revenue
from a table called 'sales_transactions'.
Include SUM(revenue) as total_revenue and SUM(units_sold) as total_units.
Order by total_revenue descending.
```

### Query 3 — Transaction Count by Region
```
Write SQL to count the number of transactions per region
from a table called 'sales_transactions'.
Order by transaction count descending.
Label the count column as 'transaction_count'.
```

### Query 4 — Monthly Revenue Trend (SQLite)
```
Write SQLite SQL to extract the month from a column named 'date' formatted as
YYYY-MM-DD, and calculate total revenue per month from 'sales_transactions'.
Use strftime('%m', date) for the month extraction.
Order by month ascending.
Note: This is SQLite — do NOT use MONTH() function.
```

### Query 5 — Discount Impact Analysis
```
Write SQL to compare average revenue per transaction between:
1. Orders that had a discount applied (discount_pct > 0)
2. Orders with no discount (discount_pct = 0)
From the table 'sales_transactions'.
Show: the discount group, count of transactions, average revenue, and total revenue.
```

### Query 6 — Customer Purchase Value Ranking
```
Write SQL to calculate:
- Total number of transactions per customer_id
- Total revenue per customer_id
From 'sales_transactions'.
Order by total revenue descending.
Show only the top 10 customers.
Label columns clearly.
```

### Query 7 — Discount vs Non-Discount Average Order
```
Write SQL to compare average revenue between transactions that had
a discount (discount_pct > 0) and those that did not (discount_pct = 0)
from sales_transactions. Show the count and average for each group.
```

---

## Phase 4: Python Analysis Prompts (Advanced Path)

### Customer Lifetime Value Estimate
```
Write Python pandas code to calculate a simplified customer lifetime value (CLV) estimate.
Use a DataFrame called 'df' with columns: customer_id, revenue, transaction_id.
Calculate: average order value per customer × number of transactions per customer.
Call the resulting column 'estimated_clv'.
Show the top 10 customers ranked by estimated_clv in a new DataFrame.
```

### Join Sales with Customer Segments
```
Write Python pandas code to:
1. Load 'data/raw/customers.csv' into a DataFrame called 'df_customers'
2. Join it with 'df' (the sales DataFrame) on 'customer_id'
3. Show the first 5 rows of the joined result
```

### Customer Segmentation by Spend
```
Write Python pandas code to create a new column called 'value_tier' in a
DataFrame called 'df_joined' that categorizes customers by total spend:
- 'High' if total revenue per customer > $500
- 'Medium' if total revenue is between $200 and $500
- 'Low' if total revenue < $200
Show the count of customers in each tier.
```

---

## Phase 5: Documentation Prompts

### Executive Summary Rewrite
```
Rewrite this executive summary for a senior leadership audience.
Requirements:
- Maximum 2–3 sentences
- Lead with the single most important finding
- Focus on business impact, not methodology
- Keep all specific numbers from the original
- Use direct, confident language

[paste your draft executive summary here]
```

### Write a Finding Headline
```
Write a punchy, specific business headline for this finding.
The headline should lead with a specific number or percentage.
Format: [Key Metric + Context]

Finding details: [describe your finding with numbers]
```

### Generate a Recommendation
```
Based on this data finding from a retail company's Q1 sales analysis,
suggest one concrete, actionable business recommendation that a CRO could
realistically implement in Q2:

Finding: [describe your finding]
```

### Write a Methodology Section
```
Write a 2-sentence methodology section for a business report.
Tools used: Python (pandas library) for data cleaning, SQLite SQL for analysis,
Jupyter notebook for running queries, VS Code as the development environment,
and GitHub Copilot for code assistance.
Keep it factual and free of jargon.
```

### Improve Clarity for Business Audience
```
Rewrite this paragraph to be clearer and more impactful for a business audience.
Avoid technical jargon. Use concrete, specific language.
Keep all numbers and findings intact.

[paste your paragraph here]
```

### Generate Next Steps
```
Based on these findings from a Q1 retail sales analysis, suggest 3 specific
next steps that a data or business team should prioritize.
Be concrete — not "investigate further" but "obtain store count by region from
operations team to normalize revenue per location."

Findings: [describe your key findings]
```

---

## Stretch Goal Prompts

### Bar Chart Visualization
```
Write Python matplotlib code to create a clean horizontal bar chart
showing total revenue by region from a pandas DataFrame.
The DataFrame has columns 'region' and 'total_revenue'.
Add a descriptive title, axis labels, and use a professional color palette.
Save the chart to a file called 'regional_revenue.png'.
```

### Data Dictionary from Schema
```
Write a markdown table data dictionary for a retail sales dataset.
Include these columns: transaction_id, date, region, product_id, product_category,
units_sold, unit_price, discount_pct, revenue, customer_id.
For each column include: column name, data type, description, example value,
and any known data quality issues.
```

### Alternative Hypothesis
```
I found that West region has the lowest transaction count in Q1 sales data.
What alternative explanations besides "underperformance" should I consider
before making a recommendation? What additional data would I need to
distinguish between these explanations?
```

---

## General Tips for Better Prompts

| Do This | Instead of This |
|---|---|
| "In DataFrame 'df' with column 'revenue'..." | "Fix the revenue column..." |
| "Write SQLite SQL — do NOT use MONTH()" | "Write SQL for monthly trends" |
| "Return results sorted by total_revenue DESC" | "Sort the results" |
| "Explain this in plain English for a business manager" | "Explain this" |
| "Keep all specific numbers from the original" | "Make it shorter" |
| Add follow-up: "That's close, but also include..." | Re-writing from scratch |

---

---

## Wrap-Up: Reusability Prompts

### Adapt This Script for My Own Data
```
I have a Python analysis script designed for a retail dataset with these columns:
transaction_id, date, region, product_category, revenue, units_sold.

My actual dataset has these columns: [list your columns].

What changes do I need to make to the script to work with my data?
List each change needed and what to replace it with.
```

### Write a README for My Analysis
```
Write a short README.md for a Python analysis project.
The project contains:
- A data cleaning script
- A spreadsheet analysis script
- A SQL query file
- Sample output charts in data/processed/

The audience is a business analyst team with mixed technical backgrounds.
Include: what the project does, how to set it up, how to run the scripts.
Keep it under 30 lines.
```

---

*This prompt library covers all four labs. Save it and use it in your own work after the session.*
