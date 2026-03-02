#!/usr/bin/env python3
# preflight_check.py
# ============================================================
# Run this script BEFORE the lab session to verify your setup.
# Run from the repository root directory:
#   python3 preflight_check.py
#
# All checks should show PASS. If any show FAIL, follow the
# fix instructions provided.
# ============================================================

import sys
import os
import importlib

print()
print("=" * 60)
print("  VS CODE ESSENTIALS FOR ANALYSTS — PRE-FLIGHT CHECK")
print("=" * 60)
print()

results = []
all_passed = True


def check(name, condition, fix_message=""):
    global all_passed
    if condition:
        print(f"  ✅ PASS   {name}")
        results.append((name, True))
    else:
        print(f"  ❌ FAIL   {name}")
        if fix_message:
            print(f"           FIX: {fix_message}")
        results.append((name, False))
        all_passed = False


# ── Python Version Check ───────────────────────────────────────────────────────
print("PYTHON ENVIRONMENT")
print("-" * 40)

version = sys.version_info
check(
    f"Python version ≥ 3.10 (you have {version.major}.{version.minor})",
    version >= (3, 10),
    "Download Python 3.10+ from https://python.org/downloads"
)


# ── Package Checks ─────────────────────────────────────────────────────────────
packages = {
    'pandas': '2.0.0',
    'numpy': '1.24.0',
    'matplotlib': '3.7.0',
    'openpyxl': '3.1.0'
}

for pkg, min_version in packages.items():
    try:
        mod = importlib.import_module(pkg)
        version_str = getattr(mod, '__version__', 'unknown')
        check(
            f"Package '{pkg}' installed (version: {version_str})",
            True
        )
    except ImportError:
        check(
            f"Package '{pkg}' installed",
            False,
            f"Run: pip install {pkg}"
        )


# ── Folder Structure Checks ────────────────────────────────────────────────────
print()
print("REPOSITORY STRUCTURE")
print("-" * 40)

folders_to_check = [
    ('data/raw',        'data/raw/ folder exists'),
    ('data/processed',  'data/processed/ folder exists'),
    ('docs',            'docs/ folder exists'),
    ('scripts',         'scripts/ folder exists'),
    ('sql',             'sql/ folder exists'),
    ('notebooks',       'notebooks/ folder exists'),
]

for path, label in folders_to_check:
    check(
        label,
        os.path.isdir(path),
        f"Run: python3 generate_sample_data.py (from repo root)"
    )


# ── File Checks ────────────────────────────────────────────────────────────────
print()
print("REQUIRED FILES")
print("-" * 40)

files_to_check = [
    ('data/raw/sales_transactions.csv',     'data/raw/sales_transactions.csv exists'),
    ('data/raw/customers.csv',              'data/raw/customers.csv exists'),
    ('data/raw/products.csv',               'data/raw/products.csv exists'),
    ('data/raw/sales_data.xlsx',            'data/raw/sales_data.xlsx exists (Lab 4)'),
    ('scripts/data_cleaning.py',            'scripts/data_cleaning.py exists'),
    ('scripts/spreadsheet_analysis.py',     'scripts/spreadsheet_analysis.py exists (Lab 4)'),
    ('sql/analysis_queries.sql',            'sql/analysis_queries.sql exists'),
    ('notebooks/exploration.ipynb',         'notebooks/exploration.ipynb exists'),
    ('docs/lab_instructions.md',            'docs/lab_instructions.md exists'),
    ('docs/quick_reference_card.md',        'docs/quick_reference_card.md exists'),
    ('docs/git_basics_cheat_sheet.md',      'docs/git_basics_cheat_sheet.md exists'),
    ('docs/business_context.md',            'docs/business_context.md exists'),
    ('docs/copilot_prompt_library.md',      'docs/copilot_prompt_library.md exists'),
]

for path, label in files_to_check:
    check(
        label,
        os.path.isfile(path),
        "Run: python3 generate_sample_data.py (or re-clone the repository)"
    )


# ── Data Quality Quick Check ───────────────────────────────────────────────────
print()
print("DATA QUALITY VALIDATION")
print("-" * 40)

try:
    import pandas as pd
    df = pd.read_csv('data/raw/sales_transactions.csv')

    check(
        f"sales_transactions.csv has ~200 rows (found: {len(df)})",
        150 <= len(df) <= 250
    )
    check(
        f"Has 10 required columns",
        len(df.columns) == 10
    )

    required_cols = ['transaction_id', 'date', 'region', 'product_id',
                     'product_category', 'units_sold', 'unit_price',
                     'discount_pct', 'revenue', 'customer_id']
    missing_cols = [c for c in required_cols if c not in df.columns]
    check(
        "All required columns present",
        len(missing_cols) == 0,
        f"Missing columns: {missing_cols}"
    )

    null_discount = df['discount_pct'].isnull().sum()
    check(
        f"Has null discount_pct values ({null_discount} rows — expected ~15%)",
        null_discount > 0
    )

    negative_revenue = (df['revenue'] < 0).sum()
    check(
        f"Has negative revenue rows ({negative_revenue} rows — expected 5–10)",
        negative_revenue > 0
    )

except Exception as e:
    check("Data validation", False, f"Error reading CSV: {e}")


# ── Summary ────────────────────────────────────────────────────────────────────
print()
print("=" * 60)
passed = sum(1 for _, p in results if p)
total = len(results)

if all_passed:
    print(f"  🎉 ALL {total} CHECKS PASSED — You are ready for the lab!")
else:
    failed = total - passed
    print(f"  ⚠️  {passed}/{total} checks passed — {failed} issue(s) need attention.")
    print()
    print("  Failed checks:")
    for name, passed_check in results:
        if not passed_check:
            print(f"    ❌ {name}")
    print()
    print("  Resolve the issues above before the session starts.")
    print("  Contact your instructor if you need help.")

print("=" * 60)
print()
