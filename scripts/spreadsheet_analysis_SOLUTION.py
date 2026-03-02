#!/usr/bin/env python3
# spreadsheet_analysis_SOLUTION.py
# ============================================================
# Lab 4: Spreadsheet Analysis for Analysts — SOLUTION VERSION
#
# ⚠️  FOR INSTRUCTOR USE ONLY — Do not share with participants during the lab.
#     Reveal on the solution-reference branch at the end of the session.
#
# This is the completed version of scripts/spreadsheet_analysis.py.
# All four TODOs have been filled in with working code.
# ============================================================

import pandas as pd
import matplotlib
matplotlib.use('Agg')  # Non-interactive backend — saves charts without opening a window
import matplotlib.pyplot as plt
import os

print()
print("=" * 50)
print("Spreadsheet Analysis — NovaTrend Retail")
print("=" * 50)

os.makedirs('data/processed', exist_ok=True)


# ── TODO 1 SOLUTION: Load the spreadsheet ─────────────────────────────────────
df = pd.read_excel('data/raw/sales_data.xlsx', sheet_name='Sales Transactions')
print(f"\nFile loaded: {df.shape[0]} rows, {df.shape[1]} columns")
print(f"Columns: {', '.join(df.columns.tolist())}")
print(df.head())


# ── TODO 2 SOLUTION: Clean column names ───────────────────────────────────────
df.columns = [col.strip().replace(' ', '_').lower() for col in df.columns]
print(f"\nColumn names cleaned.")
print(f"Columns: {', '.join(df.columns.tolist())}")


# ── TODO 3 SOLUTION: Parse dates and summarize key metrics ────────────────────
df['date'] = pd.to_datetime(df['date'], format='mixed')
df['month'] = df['date'].dt.month

# Filter out returns (negative revenue) for the summary
df_sales_only = df[df['revenue'] > 0].copy()

monthly_summary = (
    df_sales_only
    .groupby('month')
    .agg(
        total_revenue=('revenue', 'sum'),
        total_units=('units_sold', 'sum')
    )
    .reset_index()
)
monthly_summary['total_revenue'] = monthly_summary['total_revenue'].round(2)

print(f"\nMonthly Revenue Summary:")
print(monthly_summary.to_string(index=False))

total_revenue = df_sales_only['revenue'].sum()
avg_transaction = df_sales_only['revenue'].mean()
transaction_count = len(df_sales_only)

print(f"\nOverall Summary:")
print(f"  Total Revenue:      ${total_revenue:,.2f}")
print(f"  Avg Transaction:    ${avg_transaction:,.2f}")
print(f"  Transaction Count:  {transaction_count}")


# ── TODO 4 SOLUTION: Produce a chart ──────────────────────────────────────────
category_revenue = (
    df_sales_only
    .groupby('product_category')['revenue']
    .sum()
    .sort_values(ascending=False)
)

fig, ax = plt.subplots(figsize=(9, 5))
ax.bar(category_revenue.index, category_revenue.values, color='#2563EB', edgecolor='white')
ax.set_title('Revenue by Product Category — Q1', fontsize=14, fontweight='bold', pad=12)
ax.set_xlabel('Category', fontsize=11)
ax.set_ylabel('Total Revenue ($)', fontsize=11)
ax.tick_params(axis='x', rotation=45)
ax.yaxis.set_major_formatter(plt.FuncFormatter(lambda x, _: f'${x:,.0f}'))
plt.tight_layout()
plt.savefig('data/processed/revenue_by_category.png', dpi=150)
plt.close()
print(f"\nChart saved: data/processed/revenue_by_category.png")


print()
print("=" * 50)
print("Analysis complete!")
print("=" * 50)
