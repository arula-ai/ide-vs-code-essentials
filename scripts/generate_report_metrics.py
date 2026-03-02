import pandas as pd
import json
from pathlib import Path

BASE = Path(__file__).resolve().parents[1]
RAW = BASE / 'data' / 'raw' / 'sales_transactions.csv'
CLEAN = BASE / 'data' / 'processed' / 'clean_sales.csv'
RETURNS = BASE / 'data' / 'processed' / 'returns.csv'
OUT = BASE / 'data' / 'processed' / 'report_metrics.json'

raw = pd.read_csv(RAW)
clean = pd.read_csv(CLEAN)
returns = pd.read_csv(RETURNS)

metrics = {}
# Raw
metrics['raw_rows'] = int(len(raw))
metrics['raw_missing_discount'] = int(raw['discount_pct'].isnull().sum())
metrics['raw_negative_revenue'] = int((pd.to_numeric(raw['revenue'], errors='coerce') < 0).sum())
metrics['raw_category_variants'] = int(raw['product_category'].nunique())
# date formats
iso = int(raw['date'].astype(str).str.match(r"^\d{4}-\d{2}-\d{2}$").sum())
mdy = int(raw['date'].astype(str).str.match(r"^\d{1,2}/\d{1,2}/\d{4}$").sum())
mon = int(raw['date'].astype(str).str.match(r"^[A-Za-z]{3} \d{1,2} \d{4}$").sum())
metrics['raw_date_iso'] = iso
metrics['raw_date_mdy'] = mdy
metrics['raw_date_mon'] = mon

# Clean
metrics['clean_rows'] = int(len(clean))
metrics['returns_rows'] = int(len(returns))
metrics['total_revenue'] = float(clean['revenue'].astype(float).sum())

rev_by_region = clean.groupby('region')['revenue'].sum().sort_values(ascending=False)
metrics['revenue_by_region'] = {r: float(v) for r,v in rev_by_region.items()}
metrics['transactions_by_region'] = {r: int(v) for r,v in clean.groupby('region').size().items()}
metrics['avg_rev_by_region'] = {r: float(v) for r,v in clean.groupby('region')['revenue'].mean().round(2).items()}

rev_by_cat = clean.groupby('product_category')['revenue'].sum().sort_values(ascending=False)
metrics['revenue_by_category'] = {c: float(v) for c,v in rev_by_cat.items()}
metrics['top_5_categories'] = [{"category": c, "revenue": float(v)} for c,v in rev_by_cat.head(5).items()]
metrics['avg_discount_by_category'] = {c: float(v) for c,v in clean.groupby('product_category')['discount_pct'].mean().round(3).items()}

metrics['null_dates_clean'] = int(clean['date'].isnull().sum() + (clean['date'].astype(str).isin(['nan','NaT','', 'None']).sum()))
metrics['missing_discount_clean'] = int(clean['discount_pct'].isnull().sum())

# Write
OUT.parent.mkdir(parents=True, exist_ok=True)
with open(OUT, 'w') as f:
    json.dump(metrics, f, indent=2)

print(f"Wrote metrics to: {OUT}")
for k,v in metrics.items():
    if isinstance(v, (dict, list)):
        print(f"{k}: (see JSON) len={len(v)}")
    else:
        print(f"{k}: {v}")
