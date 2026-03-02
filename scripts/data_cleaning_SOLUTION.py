# data_cleaning_SOLUTION.py
# ============================================================
# SOLUTION FILE — For instructor/facilitator reference only.
# Do NOT distribute to participants before the session ends.
# This file lives on the solution-reference branch only.
# ============================================================
#
# Run from the scripts/ folder:
#   cd scripts
#   python data_cleaning_SOLUTION.py
# ============================================================

import pandas as pd

# ── Load the raw data ──────────────────────────────────────────────────────────
df = pd.read_csv('../data/raw/sales_transactions.csv')

print("=" * 60)
print("RAW DATA SUMMARY")
print("=" * 60)
print(f"Rows loaded:   {df.shape[0]}")
print(f"Columns:       {df.shape[1]}")
print(f"\nMissing values per column:")
print(df.isnull().sum().to_string())
print(f"\nSample date values:")
print(df['date'].head(8).to_string())
print(f"\nProduct category unique values:")
print(sorted(df['product_category'].dropna().unique()))
print("=" * 60)
print()


# ── TODO 1 SOLUTION: Fix the date column ──────────────────────────────────────
# Parse mixed date formats and convert to YYYY-MM-DD string
df['date'] = pd.to_datetime(df['date'], infer_datetime_format=True).dt.strftime('%Y-%m-%d')

print("✅ TODO 1 complete: Dates standardized to YYYY-MM-DD")
print(f"   Sample: {df['date'].head(5).tolist()}")


# ── TODO 2 SOLUTION: Clean the product_category column ────────────────────────
# Strip whitespace, convert to Title Case, fix the 'Electronis' typo
df['product_category'] = (
    df['product_category']
    .str.strip()
    .str.title()
    .replace('Electronis', 'Electronics')
)

print("\n✅ TODO 2 complete: Product categories standardized")
print(f"   Unique categories: {sorted(df['product_category'].unique())}")


# ── TODO 3 SOLUTION: Handle missing discount values ───────────────────────────
# Fill null discount_pct with 0 (business rule: no discount recorded = 0% applied)
df['discount_pct'] = df['discount_pct'].fillna(0)

print(f"\n✅ TODO 3 complete: Null discounts filled with 0")
print(f"   Remaining nulls in discount_pct: {df['discount_pct'].isnull().sum()}")


# ── TODO 4 SOLUTION: Handle negative revenue rows (returns) ───────────────────
# Separate returns into their own DataFrame, remove from main df
returns_df = df[df['revenue'] < 0].copy()
df = df[df['revenue'] >= 0].copy()

print(f"\n✅ TODO 4 complete: Returns separated")
print(f"   Returns found: {len(returns_df)} rows")
print(f"   Sales rows remaining: {len(df)} rows")


# ── Save cleaned data ──────────────────────────────────────────────────────────
df.to_csv('../data/processed/clean_sales.csv', index=False)

print()
print("=" * 60)
print("✅ Cleaning complete!")
print("=" * 60)
print(f"   Clean rows saved:      {df.shape[0]}")
print(f"   Returns separated:     {len(returns_df)}")
print(f"   Columns:               {df.shape[1]}")
print(f"   Output:                data/processed/clean_sales.csv")
print()
print("VALIDATION CHECKS:")
print(f"   Date formats valid:    {df['date'].apply(lambda x: '-' in str(x) and len(str(x)) == 10).all()}")
print(f"   Category null count:   {df['product_category'].isnull().sum()}")
print(f"   Discount null count:   {df['discount_pct'].isnull().sum()}")
print(f"   Negative revenue rows: {(df['revenue'] < 0).sum()}")
print("=" * 60)
