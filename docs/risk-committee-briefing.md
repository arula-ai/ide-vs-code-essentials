# Risk Committee — Investigation Briefing

**Meeting Date:** September 23, 2024
**Classification:** CONFIDENTIAL — Internal Use Only
**Distribution:** Risk Analysts, Compliance Officers, Head of Financial Investigations
**Prepared by:** Chief Risk Officer — Meridian Financial Group

---

## 1. Meeting Purpose

This briefing documents the outcome of the Emergency Risk Committee session convened on September 23, 2024 in response to a series of unusual financial signals detected across our banking, insurance, and trading operations.

The committee has authorised a **formal multi-system financial risk investigation** to determine whether the patterns observed represent isolated anomalies or coordinated financial misconduct.

This document is the primary reference for the assigned investigation team.

---

## 2. Background — What Triggered This Investigation

Over the past 90 days, our automated monitoring systems flagged activity that falls outside established risk thresholds across three business units.

### 2.1 Banking Operations — Unusual Transaction Patterns

Our banking fraud detection system (FR-001 through FR-009) raised alerts on the following:

- **Structuring activity detected:** Multiple cash deposit sequences just below the $10,000 federal reporting threshold were identified in Q1 2024, originating from a small number of customer accounts in the California region. The pattern is consistent with intentional transaction structuring to evade Bank Secrecy Act (BSA) reporting obligations.

- **Odd-hour international wire transfers:** Three large outbound wire transfers exceeding $85,000 each were initiated between 02:00–04:00 on separate dates. All three transfers were routed to the same correspondent bank category (International Wire). Current controls did not trigger a hold.

- **Geographic velocity anomalies:** Our fraud engine detected a customer account initiating POS transactions across four US states within a 90-minute window — physically implausible behaviour consistent with card cloning or account takeover.

- **Dormant account activity:** At least one account with no activity for over eight months suddenly initiated a $45,000 transfer. This was not caught by real-time monitoring.

### 2.2 Insurance Operations — High-Risk Claim Concentration

Our insurance claims processing team flagged an unusual concentration of high-value claims with elevated risk scores in Q2–Q3 2024:

- A subset of claims has risk scores in the 0.85–0.98 range (our escalation threshold is 0.75), with claim amounts significantly above the regional average.
- The geographic distribution of flagged claims overlaps with regions showing elevated banking transaction risk (California and New York).
- Claims processing did not trigger manual review for all flagged cases — a gap that the committee identified as a process failure.

### 2.3 Trading Operations — Market Surveillance Alerts

Our market surveillance system (built on FINRA reporting obligations) identified:

- A concentrated options position in a Technology sector stock built up one business day before a significant price movement — consistent with pre-knowledge trading.
- Offsetting buy/sell trades between two trader accounts on the same stocks, same day, within minutes of each other — consistent with wash trading.
- A coordinated buying pattern in a Retail sector stock across multiple trader IDs over a 3-hour window, followed by a rapid sell-off — consistent with a pump-and-dump scheme.

---

## 3. Systems and Data Sources Available

The investigation team has been granted access to the following operational data exports. All data is anonymised at the customer level.

| System | Data File | Period Covered | Record Count |
|--------|-----------|---------------|-------------|
| Banking Transaction Ledger | `data/banking_transactions.csv` | Jan–Dec 2024 | 250 records |
| Insurance Claims Register | `data/insurance_claims.xlsx` | Jan–Dec 2024 | Full register |
| Market Trade Surveillance | `data/stock_trades.csv` | Jan–Dec 2024 | 200 records |

### System Documentation

The following system documentation files are available to help interpret the data:

| Document | Location | Purpose |
|----------|----------|---------|
| Banking System Specification | `docs/banking-system.md` | Fraud detection rules, risk thresholds, data schema |
| Healthcare Platform Specification | `docs/healthcare-platform.md` | Claims processing rules, risk scoring model |
| Trading Surveillance Specification | `docs/trading-system.md` | Market surveillance rules, insider trading indicators |

---

## 4. Investigation Mandate

The Risk Committee has tasked the investigation team with answering the following questions:

### Priority 1 — Banking Investigation
1. Which specific transactions match structuring patterns (multiple deposits just below $10,000)?
2. Are the odd-hour wire transfers linked to the same customer profiles or geographic clusters?
3. Can the geographic velocity anomalies be attributed to account compromise or are they legitimate?
4. Which dormant accounts were reactivated and what is the total value of activity?

### Priority 2 — Insurance Investigation
5. Which claims exceed the 0.75 risk score threshold and what is the combined exposure value?
6. Is there a geographic correlation between flagged insurance claims and flagged banking transactions?
7. Are any claim amounts statistical outliers relative to the dataset median?

### Priority 3 — Cross-System Investigation
8. Are there customer or geographic patterns that appear across both the banking and insurance datasets?
9. Could any of the flagged banking transfers represent laundering of insurance fraud proceeds?
10. Does the trading activity timeline correlate with any major banking movements?

---

## 5. Expected Deliverable

The investigation team is required to produce a formal report saved to:

```
analysis/risk-investigation-report.md
```

The report must include:

- Executive summary of findings
- Banking transaction risk analysis (pattern type, transaction IDs, severity)
- Insurance claim risk analysis (claim IDs, risk scores, exposure value)
- Cross-system pattern analysis
- Recommendations for each risk category
- Proposed fraud detection rule improvements

**Report deadline:** End of investigation session.

---

## 6. Investigation Constraints

- All analysis must reference specific record IDs from the source datasets — no unsupported assertions
- Severity ratings (High / Medium / Low) must be applied to each finding
- The report is subject to legal review — maintain factual, evidence-based language
- Do not access systems or data outside the approved list in Section 3

---

## 7. Action Items

| # | Action | Owner | Due |
|---|--------|-------|-----|
| 1 | Review this briefing and summarise key investigation priorities | Risk Analyst | Before starting data analysis |
| 2 | Read banking system fraud detection rules in `docs/banking-system.md` | Risk Analyst | Before analysing banking data |
| 3 | Investigate banking transaction dataset for all four flagged pattern types | Risk Analyst | Lab 2 Phase 3 |
| 4 | Investigate insurance claims for risk score outliers and claim anomalies | Risk Analyst | Lab 2 Phase 3 |
| 5 | Identify cross-system patterns across banking and insurance datasets | Risk Analyst | Lab 2 Phase 3 |
| 6 | Generate completed investigation report | Risk Analyst | Lab 2 Phase 4 |
| 7 | Present findings and proposed fraud detection rule updates | Risk Analyst | Lab 3 |

---

## 8. Committee Attendees

- **M. Patterson** — Chief Risk Officer (Chair)
- **D. Lau** — Head of Banking Fraud Investigations
- **S. Okonkwo** — Director, Insurance Risk
- **R. Mehta** — Market Surveillance Lead
- **T. Bright** — Head of Compliance and Regulatory Affairs
- **Investigation Analyst** — *You*

---

*End of Risk Committee Briefing — September 23, 2024*
*Next review: Upon submission of investigation report*
*Document owner: Chief Risk Officer, Meridian Financial Group*
