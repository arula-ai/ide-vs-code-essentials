# LAB 2 — Financial Risk Investigation Using Copilot

**Duration:** 30 minutes
**Role:** Financial Risk Analyst — Meridian Financial Group
**Mission:** Read your investigation briefing, understand the systems involved, then investigate suspicious financial activity across multiple datasets

---

## Overview

You have just been assigned to a formal financial risk investigation by the Risk Committee.

Your first task is not to open a spreadsheet — it is to **read the briefing, understand the systems, and build a strategy**. That is exactly how real investigations begin.

In this lab you will work through three types of files that analysts use every day:

| Phase | File Type | Purpose |
|-------|-----------|---------|
| Phase 1 | `.md` — Meeting notes | Understand the investigation mandate and priorities |
| Phase 2 | `.md` — System documentation | Learn the fraud detection rules before examining data |
| Phase 3 | Plan Mode | Build a structured investigation strategy |
| Phase 4 | `.csv` — Transaction data | Investigate banking transaction patterns |
| Phase 5 | `.xlsx` — Claims register | Investigate insurance claim risk |
| Phase 6 | Agent Mode | Generate the investigation report |
| Phase 7 | Agent Mode | Visualise the financial workflow |

**Your final output:**

```
analysis/risk-investigation-report.md
```

### Copilot Modes Used in This Lab

| Mode | Purpose |
|------|---------|
| **Ask** | Read documents, ask questions, extract insights |
| **Plan** | Generate a structured investigation strategy |
| **Agent** | Create files, write reports, insert content |

---

# Phase 1 — Read the Investigation Briefing

Before opening any dataset, read the document that explains *why* this investigation was triggered and *what* questions need to be answered.

## Step 1 — Open Copilot Chat

**How to open Copilot Chat:**

```
CMD + Shift + I
```

At the top of the Copilot panel, set the mode to:

```
Ask
```

---

## Step 2 — Open and Summarise the Briefing Document

### How to Execute

1. Open the file in the editor:

```
docs/risk-committee-briefing.md
```

2. Read through the document to familiarise yourself with its structure.
3. Attach the file to Copilot Chat using the **paperclip icon (📎)**.
4. Enter the following prompt:

```
Summarise the key points of this risk committee briefing. List: the three business areas under investigation, the specific suspicious patterns that triggered each investigation, the data sources available, and the 10 priority questions the investigation team must answer.
```

### Expected Result

> Copilot should return a structured summary such as:
>
> **Three Business Areas Under Investigation:**
> 1. *Banking Operations — unusual transaction patterns (structuring, odd-hour wires, geographic velocity, dormant accounts)*
> 2. *Insurance Operations — high-risk claim concentration in CA and NY regions*
> 3. *Trading Operations — suspected insider trading, wash trading, and pump-and-dump scheme*
>
> **Data Sources Available:**
> - *`data/banking_transactions.csv` — 250 records, Jan–Dec 2024*
> - *`data/insurance_claims.xlsx` — Full insurance claims register*
> - *`data/stock_trades.csv` — 200 records, Jan–Dec 2024*
>
> **10 Priority Investigation Questions:**
> *[Copilot lists all 10 questions from Section 4 of the briefing, grouped by priority]*

> **Validation:** Confirm Copilot identified all three business areas and referenced the data files by name. If the summary is too brief, follow up: `What are the four specific banking patterns described in Section 2.1?`

---

## Step 3 — Ask Questions About the Investigation Scope

### How to Execute

With `docs/risk-committee-briefing.md` still attached, enter the following prompt:

```
Based on this briefing, what would be the highest-priority item to investigate first and why? What data patterns should I focus on in the banking transactions dataset before looking at anything else?
```

### Expected Result

> Copilot should reason through the priorities and respond similarly to:
>
> *"The highest priority is the structuring pattern in banking operations. Structuring — deliberately splitting transactions to stay below the $10,000 BSA reporting threshold — is a federal offence under 31 U.S.C. § 5324 and carries significant regulatory exposure. It also produces the clearest data signature: multiple deposits from the same customer ID, all between $9,000 and $9,999, within a short time window.*
>
> *Before looking at other patterns, I would filter the banking dataset for: (1) same customer_id, (2) transaction_type = Cash Deposit, (3) amount_usd between $9,000 and $9,999, (4) same date. If three or more such transactions appear, that is a textbook structuring case."*

> **Why this step matters:** Asking Copilot to reason about priorities — not just summarise — is how you use AI as a thinking partner, not just a search engine. Notice how Copilot applied domain knowledge from the briefing to identify the most actionable starting point.

---

# Phase 2 — Explore the System Documentation

Now read the technical system documentation to understand the fraud detection rules before examining any data.

## Step 1 — Analyse the Banking System Documentation

### How to Execute

1. Open the file:

```
docs/banking-system.md
```

2. Attach it to Copilot Chat (replacing the previous file attachment).
3. Enter the following prompt:

```
This is the technical specification for a banking fraud detection system. List all the fraud detection rules defined in this document (FR-001 onwards) in a simple table showing: Rule ID, Rule Name, Trigger Condition, and the recommended action. Then tell me which of these rules are most relevant to the investigation described in the risk committee briefing.
```

### Expected Result

> Copilot should produce a rules table such as:
>
> | Rule ID | Name | Trigger | Action |
> |---------|------|---------|--------|
> | FR-001 | Large Transaction Threshold | Single transaction > $10,000 | Flag for review |
> | FR-002 | Velocity Check | > 5 transactions in 1 hour | Suspend and notify |
> | FR-003 | Structuring Detection | 3+ deposits $9,000–$9,999 in 24h | Freeze, file SAR |
> | FR-004 | Geographic Anomaly | Same account, 2+ regions, < 2 hours | Identity verification |
> | FR-005 | Dormant Account Activity | 90+ days inactive, then > $10,000 | Manual review |
> | FR-006 | After-Hours Wire Transfer | International wire > $25,000 outside 08:00–18:00 | Hold for approval |
> | ... | ... | ... | ... |
>
> *"The most relevant rules for this investigation are FR-003 (Structuring), FR-004 (Geographic Anomaly), FR-005 (Dormant Account), and FR-006 (After-Hours Wire Transfer) — which map directly to the four patterns described in the banking section of the briefing."*

> **Validation:** Confirm Copilot listed rules FR-001 through at least FR-006. If it stops earlier, ask: `Are there additional fraud rules beyond FR-006 in this document?`

---

## Step 2 — Identify What to Look For in the Data

### How to Execute

With `docs/banking-system.md` still attached, enter the following prompt:

```
Based on the fraud detection rules in this document, what specific column values and data patterns should I look for in a banking transactions CSV file to identify each of these fraud types: structuring, geographic velocity anomaly, dormant account reactivation, and odd-hour international wire transfers?
```

### Expected Result

> Copilot should translate the documentation rules into concrete data filters:
>
> *"Here is what to look for in each column for each fraud type:*
>
> **Structuring:** `transaction_type = Cash Deposit` AND `amount_usd between 9000–9999` AND same `customer_id` AND same date in `timestamp`. Three or more matches = flagged case.
>
> **Geographic Velocity:** Same `customer_id` appearing with different `region` values within a 60-minute `timestamp` window. Two or more different regions within 60 minutes = physically impossible.
>
> **Dormant Account Reactivation:** `customer_id` with a long gap between `timestamp` entries (90+ days), followed by a transaction with `amount_usd > 10000`.
>
> **Odd-Hour International Wire:** `transaction_type = Wire Transfer` AND `merchant = International Wire` AND `timestamp` hour between 22:00–06:00 AND `amount_usd > 25000`."*

> **Note these patterns** — you will use them directly in Phase 4 when you ask Copilot to scan the banking dataset.

---

# Phase 3 — Plan the Investigation

Now generate a structured investigation strategy using the briefing and documentation as context.

## Step 1 — Switch to Plan Mode

In the Copilot Chat mode selector, switch to:

```
Plan
```

---

## Step 2 — Generate the Investigation Plan

### How to Execute

1. Attach both documents:
   - `docs/risk-committee-briefing.md`
   - `docs/banking-system.md`
2. Enter the following prompt:

```
Using the risk committee briefing and the banking system fraud detection rules, create a step-by-step investigation plan that covers: banking transaction analysis, insurance claim analysis, and cross-system pattern analysis. For each step, specify which file to examine, which columns to focus on, what patterns to look for, and what the output of that step should be.
```

### Expected Result

> Copilot should produce a numbered plan such as:
>
> **Investigation Plan — Meridian Financial Group Risk Review**
>
> *Step 1: Banking — Structuring Detection*
> *File: `data/banking_transactions.csv` | Focus columns: customer_id, transaction_type, amount_usd, timestamp | Pattern: 3+ Cash Deposits of $9,000–$9,999 same customer same day | Output: List of customer IDs and transaction IDs*
>
> *Step 2: Banking — Geographic Velocity*
> *File: `data/banking_transactions.csv` | Focus: customer_id, region, timestamp | Pattern: Same customer_id in 2+ regions within 60 mins | Output: Flagged customer IDs and time sequences*
>
> *Step 3: Banking — Odd-Hour Wire Transfers*
> *File: `data/banking_transactions.csv` | Focus: transaction_type, merchant, amount_usd, timestamp | Pattern: Wire Transfer to International Wire, 22:00–06:00, > $50,000 | Output: Transaction IDs and amounts*
>
> *Step 4: Banking — Dormant Account Reactivation*
> *File: `data/banking_transactions.csv` | Focus: customer_id, timestamp, amount_usd | Pattern: 90+ day gap then large transfer | Output: Customer IDs and reactivation transactions*
>
> *Step 5: Insurance — High-Risk Claims*
> *File: `data/insurance_claims.xlsx` | Focus: risk_score, claim_amount, region | Pattern: risk_score > 0.75 with high claim amounts | Output: Claim IDs and combined exposure value*
>
> *Step 6: Cross-System Analysis*
> *Files: Both datasets | Focus: region, amount, timing | Pattern: Geographic and value overlap between banking flags and insurance flags | Output: Correlated patterns and fraud ring indicators*

> **Save or note this plan** — it is your roadmap for Phases 4 and 5.

Switch Copilot back to **Ask** mode before continuing.

---

# Phase 4 — Investigate the Banking Dataset

Now apply the investigation plan to the actual data.

## Step 1 — Investigate Banking Transactions

### How to Execute

1. Open the file `data/banking_transactions.csv` in the editor — scroll through it briefly to see the structure.
2. Attach `data/banking_transactions.csv` to Copilot Chat.
3. Enter the following prompt:

```
Analyse this banking transactions dataset and identify all transactions that may indicate fraud or financial risk. Group your findings by pattern type: (1) structuring — multiple cash deposits just under $10,000 from the same customer on the same day, (2) geographic velocity — same customer appearing in multiple regions within minutes, (3) round-number repeated ATM withdrawals, (4) large international wire transfers at odd hours between 22:00–06:00, (5) dormant account sudden large activity. For each finding, list the specific transaction IDs and customer IDs involved.
```

### Expected Result

> Copilot should identify and group findings such as:
>
> **Pattern 1 — Structuring (Severity: HIGH)**
> *Customer C2001 — 5 cash deposits on 2024-03-15: TXN00001 ($9,800), TXN00002 ($9,750), TXN00003 ($9,900), TXN00004 ($9,850), TXN00005 ($9,700). All amounts fall just below the $10,000 BSA reporting threshold. This pattern matches fraud rule FR-003.*
>
> **Pattern 2 — Geographic Velocity Anomaly (Severity: HIGH)**
> *Customer C2002 — 8 POS transactions across CA, NY, TX, and FL between 14:10 and 14:88 on 2024-06-20 (TXN00006–TXN00013). Transacting in four states within minutes is physically impossible. Consistent with card cloning or account takeover.*
>
> **Pattern 3 — Repeated Round-Number ATM Withdrawals (Severity: MEDIUM)**
> *Customer C2003 — Exactly $5,000 withdrawn at ATM on six consecutive days, 2024-07-10 through 2024-07-15 (TXN00014–TXN00019). Identical round-number daily withdrawals over consecutive days are a known cash-out indicator.*
>
> **Pattern 4 — Odd-Hour International Wire Transfers (Severity: HIGH)**
> *C2004 — TXN00020: $92,000 at 02:14. C2005 — TXN00021: $87,500 at 03:47. C2006 — TXN00022: $96,000 at 02:58. All three are Business accounts wiring to "International Wire" outside business hours. Combined exposure: $275,500.*
>
> **Pattern 5 — Dormant Account Reactivation (Severity: HIGH)**
> *Customer C2007 — TXN00023: $45,000 transfer on 2024-09-18 at 23:41 with no prior transaction history in the dataset. Consistent with account takeover of an abandoned account.*

> **Validation:** Copilot should reference at least transaction IDs TXN00001–TXN00023. If a pattern was missed, prompt: `Did you find any transactions matching the dormant account pattern for customer C2007?`

---

# Phase 5 — Investigate the Insurance Claims Register

## Step 1 — Investigate Insurance Claim Risk

### How to Execute

1. Open `data/insurance_claims.xlsx` in the editor.
2. Attach `data/insurance_claims.xlsx` to Copilot Chat.
3. Enter the following prompt:

```
Analyse this insurance claims dataset and identify claims that represent high financial risk. Focus on: claims with risk scores above 0.75, claim amounts that are statistical outliers compared to the dataset median, claims with unusual geographic concentration matching the CA or NY regions flagged in our banking investigation, and any patterns suggesting repeated or coordinated claim activity. Provide specific claim IDs and values for each finding.
```

### Expected Result

> Copilot should return structured findings such as:
>
> **High Risk-Score Claims (risk_score > 0.75):**
> *Several claims have risk scores between 0.85 and 0.98 — above the 0.75 escalation threshold. These represent the cases most likely to have inadequate supporting documentation.*
>
> **High-Value Statistical Outliers:**
> *Claims with treatment costs exceeding $80,000 are significantly above the dataset median. These warrant documentation audit.*
>
> **Geographic Correlation:**
> *The CA and NY regions show the highest concentration of both high risk-score claims and elevated claim amounts — directly overlapping with the regions flagged in the banking transaction analysis.*
>
> **Recommendation:** *Cross-reference the CA/NY high-risk claims with the banking flagged transactions. If the same time period (Q1–Q3 2024) shows both banking structuring activity and insurance claim spikes in CA, this is consistent with an organised fraud ring.*

> **Validation:** Copilot should specifically call out CA and NY as the geographic overlap. If it does not, follow up: `Which regions have the highest concentration of claims with risk scores above 0.75?`

---

## Step 2 — Cross-System Pattern Analysis

### How to Execute

1. Attach **both files** to Copilot Chat:
   - `data/banking_transactions.csv`
   - `data/insurance_claims.xlsx`
2. Enter the following prompt:

```
Comparing the banking transactions and insurance claims datasets, identify any cross-system patterns that could indicate coordinated financial risk or organised fraud. Look for: geographic overlap between flagged banking transactions and high-risk insurance claims, time-period correlations (same months showing spikes in both systems), and value-level alignment (large banking transfers in similar magnitude to high-value insurance claims). Summarise the findings in terms of the risk they represent.
```

### Expected Result

> Copilot should identify overlapping patterns such as:
>
> *"Cross-referencing both datasets reveals three noteworthy correlations:*
>
> **Geographic Overlap:** *CA and NY are the top two regions for both flagged banking transactions and high-risk insurance claims. This geographic clustering is statistically unlikely to be coincidental and suggests either a fraud ring operating in both systems or a shared network of individuals exploiting weaknesses across business lines.*
>
> **Temporal Correlation:** *The Q1 2024 period shows the structuring pattern in banking (C2001, March 15) coinciding with an elevated cluster of high-risk insurance claims in the same quarter. Coordinated fraud schemes often spike across systems in the same period.*
>
> **Value Alignment:** *The three odd-hour wire transfers total $275,500. The top-tier insurance claims are in a similar value range. While a direct link cannot be confirmed without shared customer identifiers, the magnitude alignment is consistent with laundering proceeds from insurance fraud through the banking system.*
>
> **Overall Risk Assessment: HIGH — recommend escalation to Compliance and external legal review."*

---

# Phase 6 — Generate the Risk Investigation Report

## Step 1 — Switch to Agent Mode

In the Copilot Chat mode selector, switch to:

```
Agent
```

---

## Step 2 — Generate the Report

### How to Execute

1. Attach all files:
   - `docs/risk-committee-briefing.md`
   - `data/banking_transactions.csv`
   - `data/insurance_claims.xlsx`
   - `analysis/risk-investigation-report.md`
2. Enter the following prompt:

```
Using the risk committee briefing and the findings from both datasets, populate the investigation report template at analysis/risk-investigation-report.md. The report must: answer all 10 priority questions from the briefing, reference specific transaction IDs and claim records as evidence, assign severity ratings (High/Medium/Low) to each finding, include an executive summary suitable for the Risk Committee, and provide actionable recommendations for each risk pattern. Save the completed report to analysis/risk-investigation-report.md.
```

3. After Copilot confirms the save, open and review:

```
analysis/risk-investigation-report.md
```

Use Markdown preview to read it as a formatted document:

```
CMD + Shift + V
```

### Expected Result

> The completed report should contain all sections populated with real findings, including:
>
> - **Executive Summary** — 3–5 sentences describing the scope and severity of findings
> - **Banking Risk Section** — table with TXN IDs, customer IDs, amounts, pattern types, severity
> - **Insurance Risk Section** — flagged claims with risk scores and exposure values
> - **Cross-System Patterns** — geographic and value correlations documented
> - **Recommendations** — specific actions for each of the 5 banking patterns and the insurance findings
>
> The report should answer all 10 questions from Section 4 of `docs/risk-committee-briefing.md`.

> **Validation:** Check that the report references specific transaction IDs such as TXN00001, TXN00020, and TXN00023. If sections still show placeholder text, ask Copilot: `Populate the Banking Risk section using the flagged transactions from banking_transactions.csv`

---

# Phase 7 — Visualise the Financial Workflow

## Steps

1. Open the file:

```
diagrams/system-architecture.md
```

2. Ensure Copilot is still in **Agent Mode**.
3. Attach the file and enter the following prompt:

```
Create a mermaid flowchart diagram showing the end-to-end financial investigation workflow at Meridian Financial Group. Include nodes for: Customer, Banking System, Insurance System, Trading System, Fraud Detection Engine, Risk Analyst, Risk Committee, and Investigation Report. Add labelled arrows to show the direction of data flow and escalation paths. Insert the complete mermaid diagram into diagrams/system-architecture.md and save it.
```

4. Preview the diagram:

```
CMD + Shift + V
```

### Expected Result

> Copilot inserts a Mermaid diagram such as:
>
> ```mermaid
> flowchart LR
>     Customer -->|initiates transaction| BankingSystem
>     Customer -->|submits claim| InsuranceSystem
>     Customer -->|places trade| TradingSystem
>     BankingSystem -->|transaction records| FraudDetectionEngine
>     InsuranceSystem -->|claim records + risk scores| FraudDetectionEngine
>     TradingSystem -->|trade surveillance data| FraudDetectionEngine
>     FraudDetectionEngine -->|flagged cases| RiskAnalyst
>     RiskAnalyst -->|investigation report| RiskCommittee
>     RiskCommittee -->|escalation decision| Compliance
> ```
>
> The Markdown preview renders this as a visual flowchart with boxes and labelled arrows. If the diagram does not render, install the **Markdown Preview Mermaid Support** extension from the Extensions panel.

---

## Lab 2 — Success Criteria

Before moving to Lab 3, confirm you achieved all of the following:

- [ ] Read `docs/risk-committee-briefing.md` and used Copilot to extract the investigation scope and priorities
- [ ] Asked Copilot to reason about investigation priorities — not just summarise
- [ ] Analysed `docs/banking-system.md` to extract fraud detection rules as a table
- [ ] Translated system documentation rules into concrete data filter patterns
- [ ] Switched to Plan Mode and generated a structured investigation plan referencing specific files and columns
- [ ] Investigated `data/banking_transactions.csv` and identified all 5 suspicious patterns with specific transaction IDs
- [ ] Investigated `data/insurance_claims.xlsx` and identified high-risk claims and geographic overlaps
- [ ] Ran a cross-system analysis across both datasets
- [ ] Switched to Agent Mode and generated the completed investigation report answering all 10 briefing questions
- [ ] Generated and previewed a Mermaid flowchart in `diagrams/system-architecture.md`

---

## File Types Used in This Lab

| File | Type | How Copilot was used |
|------|------|---------------------|
| `docs/risk-committee-briefing.md` | Markdown — Meeting notes | Summarise, extract priorities, reason about approach |
| `docs/banking-system.md` | Markdown — System documentation | Extract rules, translate to data patterns |
| `data/banking_transactions.csv` | CSV — Structured data | Pattern detection across rows and columns |
| `data/insurance_claims.xlsx` | Excel — Claims register | Risk scoring, outlier detection, geographic analysis |
| `analysis/risk-investigation-report.md` | Markdown — Report template | Agent Mode file population |
| `diagrams/system-architecture.md` | Markdown — Diagram file | Agent Mode diagram insertion |

---

> **You are now ready for Lab 3** — where you will validate the report, update system documentation with improved fraud detection rules, and commit your work to the repository.
