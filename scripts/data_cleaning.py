# data_cleaning.py
# ============================================================
# Goal: Clean sales_transactions.csv → output clean_sales.csv
# ============================================================
#
# HOW TO USE THIS FILE:
# ─────────────────────────────────────────────────────────────
# 1. Run this script from the scripts/ folder in the terminal:
#      cd scripts
#      python data_cleaning.py
#
# 2. Each TODO section has two ways to complete it:
#
#    Option A — Inline Copilot suggestion:
#      Type a descriptive comment on the next line.
#      Wait 2–3 seconds for Copilot's gray suggestion.
#      Press Tab to accept it.
#
#    Option B — Copilot Chat:
#      Copy the prompt provided in each section.
#      Paste it into Copilot Chat (Cmd+Shift+I / Ctrl+Shift+I).
#      Copy the suggested code and paste it below the TODO.
#
# 3. After completing all TODOs, run the script and check:
#      - No red error text in the terminal
#      - "✅ Cleaning complete!" appears
#      - data/processed/clean_sales.csv exists
#
# ─────────────────────────────────────────────────────────────
# WHAT THIS SCRIPT FIXES:
#
#  Issue 1: Mixed date formats (3 different formats → standardize to YYYY-MM-DD)
#  Issue 2: Inconsistent product_category casing + typo ("Electronis")
#  Issue 3: Missing discount_pct values (~15% null → fill with 0)
#  Issue 4: Negative revenue rows (product returns → separate into returns file)
#
# ─────────────────────────────────────────────────────────────

import pandas as pd

# ── Load the raw data ──────────────────────────────────────────────────────────
df = pd.read_csv('../data/raw/sales_transactions.csv')

print("=" * 60)
print("RAW DATA SUMMARY")
print("=" * 60)
print(f"Rows loaded:   {df.shape[0]}")
print(f"Columns:       {df.shape[1]}")
print(f"\nColumn names:  {df.columns.tolist()}")
print(f"\nFirst 3 rows:")
print(df.head(3).to_string())
print(f"\nMissing values per column:")
print(df.isnull().sum().to_string())
print(f"\nSample date values (to show mixed formats):")
print(df['date'].head(10).to_string())
print(f"\nProduct category unique values (to show inconsistency):")
print(sorted(df['product_category'].dropna().unique()))
print("=" * 60)
print()


# ── TODO 1: Fix the date column ────────────────────────────────────────────────
#
# PROBLEM: The 'date' column has three different formats mixed together:
#   - '2024-01-15'   ← ISO format (international standard)
#   - '01/15/2024'   ← US format (month/day/year)
#   - 'Jan 15 2024'  ← English format (abbreviated month name)
#
# GOAL: Convert ALL dates to a single consistent format: YYYY-MM-DD
#       This makes them sortable and comparable in SQL queries.
#
# BUSINESS WHY: If dates are in different formats, monthly trend analysis
#   breaks down entirely. January "01" sorts before "Jan" alphabetically.
#
# ─────────────────────────────────────────────────────────────
# Copilot Chat Prompt (Option B):
#
# "Write Python pandas code to parse a column named 'date' in a DataFrame
#  called 'df' that contains mixed date formats:
#    - '2024-01-15' (ISO)
#    - '01/15/2024' (US format)
#    - 'Jan 15 2024' (English abbreviated month)
#  Use pd.to_datetime with infer_datetime_format=True or dayfirst=False.
#  Then format the result as a YYYY-MM-DD string.
#  Store the result back into df['date']."
#
# ─────────────────────────────────────────────────────────────
# Inline Copilot hint — type this comment on the next blank line,
# then wait for Copilot to suggest the code:
#   # parse df['date'] with mixed formats using pd.to_datetime, store as YYYY-MM-DD string

# [Copilot will suggest code here — press Tab to accept]

# parse df['date'] with mixed formats using pd.to_datetime, store as YYYY-MM-DD string
# use errors='coerce' to surface unparsable dates as NaT
df['date'] = pd.to_datetime(df['date'], infer_datetime_format=True, errors='coerce')
df['date'] = df['date'].dt.strftime('%Y-%m-%d')




# ── TODO 2: Clean the product_category column ──────────────────────────────────
#
# PROBLEM: The category values have inconsistent casing AND a typo:
#   'Electronics' / 'ELECTRONICS' / 'electronics' → should all be 'Electronics'
#   'Electronis' ← typo → should be 'Electronics'
#   'Home & Garden' / 'home & garden' → should be 'Home & Garden'
#
# GOAL: Standardize all category values to Title Case. Fix the typo.
#
# BUSINESS WHY: SQL GROUP BY on 'product_category' will treat 'Electronics' and
#   'electronics' as two DIFFERENT categories — splitting your revenue numbers.
#
# ─────────────────────────────────────────────────────────────
# Copilot Chat Prompt (Option B):
#
# "Write Python pandas code to clean the 'product_category' column in DataFrame 'df':
#  1. Strip leading and trailing whitespace from each value
#  2. Convert all values to Title Case using .str.title()
#  3. Replace the misspelled value 'Electronis' with 'Electronics'
#  Store the result back into df['product_category']."
#
# ─────────────────────────────────────────────────────────────
# Inline Copilot hint:
#   # strip whitespace, title case, and fix typo 'Electronis' in product_category

# strip whitespace, title case, and fix typo 'Electronis' in product_category
# operate only on non-null values to avoid converting NaN to the string 'nan'
mask_cat = df['product_category'].notna()
df.loc[mask_cat, 'product_category'] = (
	df.loc[mask_cat, 'product_category']
	.str.strip()
	.str.title()
	.replace({'Electronis': 'Electronics'})
)


# ── TODO 3: Handle missing discount values ─────────────────────────────────────
#
# PROBLEM: About 15% of rows (~30 rows) have no value in 'discount_pct'.
#
# BUSINESS RULE: If no discount was recorded, it means 0% discount was applied.
#   This is confirmed by the finance team — unrecorded discounts are always 0.
#
# GOAL: Fill all null (NaN/missing) values in 'discount_pct' with 0.
#
# BUSINESS WHY: Missing values in discount_pct cause incorrect average calculations.
#   SQL AVG() ignores nulls — so your reported average discount will be overstated.
#
# ─────────────────────────────────────────────────────────────
# Copilot Chat Prompt (Option B):
#
# "Write one line of Python pandas code to fill all NaN (missing) values in
#  a column named 'discount_pct' in DataFrame 'df' with the value 0.
#  Use fillna() and store the result back in the column."
#
# ─────────────────────────────────────────────────────────────
# Inline Copilot hint:
#   # fill missing discount_pct values with 0

# fill missing discount_pct values with 0
df['discount_pct'] = pd.to_numeric(df['discount_pct'], errors='coerce').fillna(0.0)



# ── TODO 4: Handle negative revenue rows (product returns) ─────────────────────
#
# PROBLEM: Some rows have negative revenue — these are product returns.
#   They are VALID data but should NOT be included in sales revenue analysis.
#   Mixing returns with sales understates your true revenue numbers.
#
# GOAL:
#   1. Identify rows where revenue < 0 → these are returns
#   2. Copy them into a separate DataFrame called 'returns_df'
#   3. Remove them from the main 'df' (keep only positive revenue rows)
#   4. Print a count so we know how many were found
#
# BUSINESS WHY: Your CRO wants to know Q1 sales revenue. Returns are not sales.
#   They should be reported separately — not subtracted silently from the total.
#
# ─────────────────────────────────────────────────────────────
# Copilot Chat Prompt (Option B):
#
# "Write Python pandas code to:
#  1. Create a new DataFrame called 'returns_df' containing all rows where
#     the 'revenue' column is less than 0 in DataFrame 'df'
#  2. Remove those negative-revenue rows from 'df' (keep only rows where revenue >= 0)
#     Use boolean indexing: df = df[df['revenue'] >= 0]
#  3. Print a message like: 'Returns separated: X rows'
#  Use .copy() when creating returns_df to avoid the SettingWithCopyWarning."
#
# ─────────────────────────────────────────────────────────────
# Inline Copilot hint:
#   # create returns_df from rows where revenue < 0, then filter df to keep only revenue >= 0

# create returns_df from rows where revenue < 0, then filter df to keep only revenue >= 0
# ensure numeric types for revenue and units_sold before filtering
df['revenue'] = pd.to_numeric(df['revenue'], errors='coerce')
df['units_sold'] = pd.to_numeric(df['units_sold'], errors='coerce')
returns_df = df[df['revenue'] < 0].copy()
df = df[df['revenue'] >= 0].copy()
print(f"Returns separated: {len(returns_df)} rows")



# ── Save cleaned data ──────────────────────────────────────────────────────────
df.to_csv('../data/processed/clean_sales.csv', index=False)
if 'returns_df' in locals():
	returns_df.to_csv('../data/processed/returns.csv', index=False)

print()
print("=" * 60)
print("✅ Cleaning complete!")
print("=" * 60)
print(f"   Clean rows saved:      {df.shape[0]}")
print(f"   Returns separated:     {len(returns_df) if 'returns_df' in dir() else 0}")
print(f"   Columns:               {df.shape[1]}")
print(f"   Output:                data/processed/clean_sales.csv")
print()
print("VALIDATION CHECKS:")
print(f"   Date formats unique:   {df['date'].apply(lambda x: '-' in str(x) and len(str(x)) == 10).all()}")
print(f"   Category null count:   {df['product_category'].isnull().sum()}")
print(f"   Discount null count:   {df['discount_pct'].isnull().sum()}")
print(f"   Negative revenue rows: {(df['revenue'] < 0).sum()}")
print()
print("Sample cleaned data (first 3 rows):")
print(df[['transaction_id', 'date', 'region', 'product_category', 'discount_pct', 'revenue']].head(3).to_string())
print("=" * 60)
