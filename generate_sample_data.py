#!/usr/bin/env python3
# generate_sample_data.py
# ============================================================
# Run this script ONCE to create all sample data files for the lab.
# Run from the repository root directory:
#   python3 generate_sample_data.py
#
# Creates:
#   data/raw/sales_transactions.csv  — 200 rows, intentionally messy
#   data/raw/customers.csv           — 51 rows (includes 1 duplicate)
#   data/raw/products.csv            — 5 rows (intentionally clean)
#   data/raw/sales_data.xlsx         — Excel version for Lab 4 spreadsheet analysis
# ============================================================

import pandas as pd
import numpy as np
import os
from datetime import datetime, timedelta
import random

random.seed(42)
np.random.seed(42)

# ── Create directories ─────────────────────────────────────────────────────────
os.makedirs('data/raw', exist_ok=True)
os.makedirs('data/processed', exist_ok=True)
print("✅ Directories ready: data/raw/ and data/processed/")


# ── Generate sales_transactions.csv ───────────────────────────────────────────
# Regional distribution — intentionally uneven for analysis purposes
regions = ['North', 'South', 'East', 'West']
region_weights = [0.35, 0.25, 0.22, 0.18]  # North leads, West trails

product_ids = ['P007', 'P012', 'P015', 'P022', 'P031']

# Map product_id to category (used for realistic category assignments)
product_category_map = {
    'P007': 'Home & Garden',
    'P012': 'Electronics',
    'P015': 'Sports & Fitness',
    'P022': 'Apparel',
    'P031': 'Home & Garden'
}

# Map product_id to unit price
product_price_map = {
    'P007': 49.99,
    'P012': 299.99,
    'P015': 79.99,
    'P022': 99.99,
    'P031': 149.99
}

# Date range: Q1 2024 (January 1 — March 31)
start_date = datetime(2024, 1, 1)
dates = [start_date + timedelta(days=random.randint(0, 89)) for _ in range(200)]


def format_date_messy(d):
    """Randomly apply one of three date formats to simulate real-world inconsistency."""
    fmt = random.choice(['iso', 'us', 'english'])
    if fmt == 'iso':
        return d.strftime('%Y-%m-%d')      # 2024-01-15
    elif fmt == 'us':
        return d.strftime('%m/%d/%Y')      # 01/15/2024
    else:
        return d.strftime('%b %d %Y')      # Jan 15 2024


rows = []
for i in range(200):
    region = random.choices(regions, weights=region_weights)[0]
    product_id = random.choice(product_ids)
    unit_price = product_price_map[product_id]

    # Get the base category and intentionally introduce errors
    base_cat = product_category_map[product_id]
    rand = random.random()
    if rand < 0.06 and base_cat == 'Electronics':
        cat = 'Electronis'          # Typo
    elif rand < 0.12:
        cat = base_cat.upper()      # ELECTRONICS
    elif rand < 0.18:
        cat = base_cat.lower()      # electronics
    else:
        cat = base_cat              # Electronics (clean)

    units = random.randint(1, 8)
    discount_options = [0.0, 0.05, 0.10, 0.15, 0.20, 0.25, 0.30]
    discount = random.choice(discount_options)

    # ~15% of rows have no discount recorded (will be null)
    if random.random() < 0.15:
        discount = np.nan

    revenue = round(units * unit_price * (1 - (discount if not pd.isna(discount) else 0)), 2)

    # ~4% of rows are product returns (negative revenue)
    is_return = random.random() < 0.04
    if is_return:
        revenue = -round(unit_price, 2)
        units = np.nan  # Returns don't have units_sold recorded

    rows.append({
        'transaction_id': f'T{str(i + 1).zfill(3)}',
        'date': format_date_messy(dates[i]),
        'region': region,
        'product_id': product_id,
        'product_category': cat,
        'units_sold': units,
        'unit_price': unit_price,
        'discount_pct': discount,
        'revenue': revenue,
        'customer_id': f'C{str(random.randint(1, 50)).zfill(3)}'
    })

df_sales = pd.DataFrame(rows)
df_sales.to_csv('data/raw/sales_transactions.csv', index=False)
print(f"✅ sales_transactions.csv: {len(df_sales)} rows")
print(f"   Date formats: mixed (ISO, US, English)")
print(f"   Nulls in discount_pct: {df_sales['discount_pct'].isnull().sum()} rows (~15%)")
print(f"   Negative revenue rows (returns): {(df_sales['revenue'] < 0).sum()} rows")
print(f"   Category issues: uppercase + lowercase + typo 'Electronis'")


# ── Generate customers.csv ─────────────────────────────────────────────────────
first_names = [
    'Sarah', 'Marcus', 'Aisha', 'Derek', 'Linda',
    'James', 'Priya', 'Carlos', 'Emily', 'Kwame',
    'Jennifer', 'Michael', 'Fatima', 'David', 'Anna'
]
last_names = [
    'Johnson', 'Williams', 'Patel', 'Chen', 'Okafor',
    'Kowalski', 'Sharma', 'Rivera', 'Thompson', 'Mensah',
    'Garcia', 'Robinson', 'Kim', 'Anderson', 'Nakamura'
]


def format_date_customer(d):
    """Apply one of three date formats for the join_date column."""
    fmt = random.choice(['%Y-%m-%d', '%m/%d/%Y', '%b %d %Y'])
    return d.strftime(fmt)


customers = []
for i in range(50):
    fn = random.choice(first_names)
    ln = random.choice(last_names)
    cid = f'C{str(i + 1).zfill(3)}'
    region = random.choices(regions, weights=region_weights)[0]

    # ~10% of customers have no segment recorded
    segment = random.choice(['Premium', 'Standard', 'Basic', None])
    join = datetime(random.randint(2018, 2023), random.randint(1, 12), random.randint(1, 28))

    customers.append({
        'customer_id': cid,
        'customer_name': f'{fn} {ln}',
        'region': region,
        'segment': segment,
        'join_date': format_date_customer(join),
        'email': f'{fn.lower()}.{ln.lower()[0]}@example.com'
    })

# Add one intentional duplicate customer (same ID, slightly different email — realistic typo)
duplicate = customers[4].copy()
duplicate['email'] = duplicate['email'].replace('.', '_')  # Slightly different email
customers.append(duplicate)

df_customers = pd.DataFrame(customers)
df_customers.to_csv('data/raw/customers.csv', index=False)
print(f"\n✅ customers.csv: {len(df_customers)} rows")
print(f"   Includes 1 intentional duplicate customer_id")
print(f"   Null segments: {df_customers['segment'].isnull().sum()} rows (~10%)")
print(f"   Mixed join_date formats")


# ── Generate products.csv ──────────────────────────────────────────────────────
# This file is intentionally clean — it is the reference/dimension table
products = [
    ('P007', 'Ceramic Planter Set',   'Home & Garden',   12.50,  49.99, 'GreenThumb Co.'),
    ('P012', 'UltraSound Speaker',    'Electronics',     89.00, 299.99, 'TechWave Ltd.'),
    ('P015', 'Yoga Mat Pro',          'Sports & Fitness', 18.00, 79.99, 'ActiveLife Inc.'),
    ('P022', 'Merino Pullover',       'Apparel',         28.00,  99.99, 'WoolCraft'),
    ('P031', 'Smart Desk Lamp',       'Home & Garden',   35.00, 149.99, 'BrightHome'),
]

df_products = pd.DataFrame(
    products,
    columns=['product_id', 'product_name', 'category', 'cost_price', 'list_price', 'supplier']
)
df_products.to_csv('data/raw/products.csv', index=False)
print(f"\n✅ products.csv: {len(df_products)} rows (intentionally clean — no issues)")


# ── Generate sales_data.xlsx (for Lab 4 — Spreadsheet Analysis) ───────────────
# This Excel workbook combines sales, products, and a summary tab
# It is the "spreadsheet" analysts load in Lab 4 using openpyxl + pandas
try:
    with pd.ExcelWriter('data/raw/sales_data.xlsx', engine='openpyxl') as writer:
        df_sales.to_excel(writer, sheet_name='Sales Transactions', index=False)
        df_customers.to_excel(writer, sheet_name='Customers', index=False)
        df_products.to_excel(writer, sheet_name='Products', index=False)
    print(f"\n✅ sales_data.xlsx: Excel workbook with 3 sheets")
    print(f"   Sheet 1 — Sales Transactions: {len(df_sales)} rows")
    print(f"   Sheet 2 — Customers: {len(df_customers)} rows")
    print(f"   Sheet 3 — Products: {len(df_products)} rows")
except ImportError:
    print("\n⚠️  openpyxl not installed — skipping sales_data.xlsx")
    print("   Install it with: pip install openpyxl")
    print("   Then re-run this script to generate the Excel file.")


# ── Summary ────────────────────────────────────────────────────────────────────
print()
print("=" * 60)
print("🎉 All sample data files generated successfully!")
print("=" * 60)
print(f"  data/raw/sales_transactions.csv  — {len(df_sales)} rows")
print(f"  data/raw/customers.csv           — {len(df_customers)} rows")
print(f"  data/raw/products.csv            — {len(df_products)} rows")
print(f"  data/raw/sales_data.xlsx         — Excel workbook (3 sheets)")
print()
print("INTENTIONAL DATA QUALITY ISSUES INCLUDED:")
print("  sales_transactions.csv:")
print("    ✓ Mixed date formats (ISO, US, English)")
print("    ✓ Inconsistent product_category casing")
print("    ✓ Typo: 'Electronis' in product_category")
print("    ✓ ~15% null values in discount_pct")
print("    ✓ Negative revenue rows (product returns)")
print()
print("  customers.csv:")
print("    ✓ One duplicate customer_id (slight email variation)")
print("    ✓ ~10% null segment values")
print("    ✓ Mixed join_date formats")
print()
print("  products.csv:")
print("    ✓ Intentionally clean — no issues")
print("=" * 60)
