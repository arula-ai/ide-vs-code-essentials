# Banking Transaction Processing System

**Version:** 4.2.1
**Classification:** INTERNAL — RESTRICTED
**Owner:** Core Banking Technology Group
**Last Updated:** 2024-11-15
**Compliance Review Date:** 2025-Q1

---

## System Overview

The Banking Transaction Processing System (BTPS) is the enterprise-grade platform responsible for ingesting, validating, routing, and archiving all financial transactions across the organization's retail, commercial, and business banking divisions. The system processes more than 2.4 million transactions per day across 14 regional processing centers and serves as the authoritative source of record for all monetary movement.

A core function of the BTPS is real-time fraud detection. Every transaction entering the system is evaluated against a multi-layer fraud detection engine that applies rule-based scoring, behavioral analytics, and machine learning models trained on historical fraud patterns. Transactions that exceed defined risk thresholds are automatically flagged for review by the Financial Crimes Compliance (FCC) team.

The BTPS integrates directly with the Bank Secrecy Act (BSA) reporting module, the Anti-Money Laundering (AML) screening engine, and the Office of Foreign Assets Control (OFAC) watchlist service. Compliance with federal and state-level regulations is enforced at the transaction ingestion layer before any funds movement is authorized.

---

## Architecture Components

### 1. Transaction Ingestion Layer
The ingestion layer accepts transaction events from all downstream source systems including ATM networks, point-of-sale processors, ACH gateways, SWIFT wire transfer interfaces, mobile banking applications, online banking portals, and branch teller workstations. All events are standardized into the canonical transaction schema (described below) before passing to the processing pipeline.

### 2. Real-Time Fraud Detection Engine (RFDE)
The RFDE is a distributed stream-processing system built on Apache Kafka and Apache Flink. It evaluates each transaction in under 80 milliseconds using the following detection layers:

- **Layer 1 — Rule Engine:** Static threshold and pattern rules (BSA currency reporting, structuring detection, velocity checks)
- **Layer 2 — Behavioral Analytics:** Deviation from customer baseline behavior (average transaction size, typical merchants, typical channels, typical transaction timing)
- **Layer 3 — Graph Analytics:** Network-level anomaly detection linking accounts through shared attributes (device fingerprint, IP address, payee accounts)
- **Layer 4 — ML Scoring Model:** Gradient-boosted ensemble model producing a continuous fraud probability score (0.0–1.0)

### 3. Case Management System (CMS)
Transactions flagged by the RFDE are automatically routed to the CMS where FCC analysts manage investigation workflows, document findings, escalate to SAR (Suspicious Activity Report) filing, and coordinate with law enforcement as required.

### 4. Reporting and Regulatory Filing Module
Automated generation and submission of:
- FinCEN Currency Transaction Reports (CTRs) for transactions exceeding $10,000
- Suspicious Activity Reports (SARs) for confirmed fraud patterns
- State-level regulatory reports as required by jurisdiction

### 5. Data Warehouse and Archive
All transaction records are persisted in an immutable append-only data warehouse. Records are retained for a minimum of seven years in accordance with BSA requirements. The warehouse feeds downstream analytics, audit, and regulatory reporting systems.

---

## Data Schema

The primary transaction dataset (`banking_transactions.csv`) conforms to the following schema. Each row represents one completed or attempted transaction event.

| Column | Data Type | Description |
|---|---|---|
| `transaction_id` | String | Unique transaction identifier. Format: `TXN` followed by 5-digit zero-padded integer (e.g., `TXN00001`). Immutable once assigned. |
| `customer_id` | String | Internal customer identifier. Format: `C` followed by 4-digit number. Links to the Customer Master Record in CRM. |
| `account_type` | String | Classification of the account from which the transaction originates. Valid values: `Checking`, `Savings`, `Business`. |
| `transaction_type` | String | The category of transaction. Valid values: `Deposit`, `Withdrawal`, `Transfer`, `POS Purchase`, `Wire Transfer`, `Online Payment`, `Cash Deposit`. |
| `merchant` | String | The destination entity, merchant name, or transaction description. For internal transfers, this reflects the receiving account label. |
| `amount_usd` | Numeric | Transaction amount in US Dollars. Stored as a decimal to two places. Negative values are not permitted; credits and debits are distinguished by `transaction_type`. |
| `region` | String | Two-letter US state code representing the geographic origin of the transaction as determined by the originating channel's registered location or IP geolocation. |
| `channel` | String | The channel through which the transaction was initiated. Valid values: `Mobile App`, `Online Banking`, `ATM`, `POS Terminal`, `Wire Transfer`, `Branch`. |
| `timestamp` | DateTime | UTC timestamp of transaction authorization. Format: `YYYY-MM-DD HH:MM:SS`. |
| `is_flagged` | Boolean | Indicates whether the transaction has been flagged by the fraud detection engine. Values: `TRUE` or `FALSE`. Flagged transactions require manual review before final disposition. |

---

## Transaction Processing Rules

### Authorization Flow

1. Transaction event received at ingestion layer
2. Schema validation and data type enforcement
3. Customer identity verification against CRM
4. Account status check (active, frozen, closed)
5. Balance sufficiency check (for debit transactions)
6. OFAC watchlist screening (payee and originator)
7. AML rule engine evaluation
8. Fraud detection engine scoring
9. Authorization decision (Approve / Decline / Pending Review)
10. Ledger posting and event publication to downstream systems

### Transaction Limits by Account Type

| Account Type | Single Transaction Limit | Daily Aggregate Limit | Wire Transfer Limit |
|---|---|---|---|
| Checking | $25,000 | $50,000 | $50,000 |
| Savings | $15,000 | $30,000 | $25,000 |
| Business | $500,000 | $2,000,000 | $500,000 |

Transactions that exceed these limits are automatically held for manual authorization by the customer's relationship manager or the operations team.

### Currency Transaction Reporting (CTR)

Under the Bank Secrecy Act 31 U.S.C. § 5313, the bank is required to file a Currency Transaction Report (CTR) with FinCEN for any cash transaction exceeding $10,000. This includes:
- A single cash transaction of more than $10,000
- Multiple cash transactions by the same customer on the same business day that aggregate to more than $10,000 (structuring detection applies)

CTR filing is automated through the Reporting Module with a 15-day filing deadline from the date of the transaction.

---

## Fraud Detection Framework

The fraud detection framework is a critical component of the BTPS. It is designed to identify financial crimes including money laundering, identity theft, account takeover, wire fraud, and structured transactions intended to evade reporting requirements. The framework applies multiple detection methodologies in parallel to maximize detection coverage while minimizing false-positive rates that disrupt legitimate customer activity.

### Fraud Detection Rules (Current Rules with Thresholds)

The following rules are active in the production fraud detection engine as of the current version. Each rule is associated with a severity level and an automatic disposition action.

#### Rule FR-001: Currency Reporting Threshold
- **Trigger:** Any single Cash Deposit or cash Withdrawal exceeding $10,000
- **Action:** Automatic CTR filing; transaction flagged for review
- **Severity:** Medium
- **Rationale:** BSA legal requirement; must be reported to FinCEN

#### Rule FR-002: Structuring Detection
- **Trigger:** Two or more Cash Deposit or Withdrawal transactions from the same customer within a 24-hour period where individual amounts are between $8,000 and $9,999 and the aggregate exceeds $10,000
- **Action:** Flag all qualifying transactions; alert FCC team; initiate SAR review process
- **Severity:** High
- **Rationale:** Structuring (also called "smurfing") is a federal crime under 31 U.S.C. § 5324. Customers who break up large cash transactions to avoid the $10,000 reporting threshold are engaging in a form of money laundering. Structuring is a primary fraud vector used by drug trafficking organizations and other criminal enterprises.

#### Rule FR-003: Geographic Velocity Anomaly
- **Trigger:** Transactions from the same customer originating from two or more distinct geographic regions (based on `region` field or IP geolocation) within a 4-hour window where physical travel between those regions would be impossible
- **Action:** Flag all transactions in the anomalous sequence; trigger step-up authentication; notify fraud operations
- **Severity:** High
- **Rationale:** Rapid transactions across geographically impossible locations indicate account takeover or credential compromise. This is one of the most reliable fraud signals for unauthorized use of stolen payment credentials.

#### Rule FR-004: Round Number Withdrawal Velocity
- **Trigger:** Three or more ATM Withdrawals of the same exact round-dollar amount (e.g., $1,000, $5,000) from the same customer within a 7-day period
- **Action:** Flag transactions; temporarily restrict ATM withdrawal limit; notify customer via registered contact method
- **Severity:** Medium
- **Rationale:** Consistent round-number ATM withdrawals at regular intervals may indicate structured cash-out activity associated with fraud proceeds or money mule operations.

#### Rule FR-005: Large Wire Transfer — Odd Hours
- **Trigger:** Any outbound Wire Transfer exceeding $50,000 initiated between 22:00 and 06:00 UTC
- **Action:** Transaction held for manual authorization; customer authentication required; FCC notified
- **Severity:** High
- **Rationale:** Legitimate high-value wire transfers are almost exclusively initiated during business hours. Wire fraud schemes, including business email compromise (BEC) fraud, frequently exploit overnight processing windows to transfer funds before discovery.

#### Rule FR-006: Dormant Account Reactivation
- **Trigger:** Any transaction exceeding $10,000 on an account that has had zero transactions in the preceding 180 days
- **Action:** Flag transaction; require enhanced identity verification; FCC review within 24 hours
- **Severity:** High
- **Rationale:** Dormant accounts are prime targets for account takeover fraud. Sudden large-value activity after a prolonged period of inactivity is a strong fraud indicator and may suggest the account has been compromised or is being used as a pass-through account for illicit funds.

#### Rule FR-007: Transaction Velocity — High Frequency
- **Trigger:** More than 8 transactions from the same customer within any 60-minute window
- **Action:** Temporary account restriction; fraud operations alert; real-time SMS notification to customer
- **Severity:** Critical
- **Rationale:** High-frequency transaction bursts are characteristic of card testing fraud (where stolen card numbers are tested with small purchases), automated account draining attacks, and point-of-sale compromise scenarios.

#### Rule FR-008: Large Cash Deposits — Business Account
- **Trigger:** Business account receiving more than 3 Cash Deposit transactions from unrelated payees exceeding $10,000 aggregate within a 5-day period
- **Action:** Enhanced due diligence review; request supporting documentation; SAR evaluation initiated
- **Severity:** High
- **Rationale:** Business accounts that receive frequent large cash deposits from multiple unrelated individual payees may be serving as consolidation accounts in money laundering schemes. This pattern is common in trade-based money laundering and cash-intensive business fraud.

#### Rule FR-009: International Wire Concentration
- **Trigger:** More than 2 outbound international wire transfers from the same customer to the same beneficiary institution within a 30-day period, totaling more than $25,000
- **Action:** Enhanced due diligence; OFAC re-screening; relationship manager notification
- **Severity:** Medium
- **Rationale:** Concentrated international wire activity to a single foreign beneficiary institution may indicate layering — the second stage of money laundering — where funds are moved across jurisdictions to obscure their origin.

### Suspicious Activity Indicators

Beyond the automated fraud detection rules, FCC analysts are trained to recognize the following qualitative indicators when reviewing flagged transactions:

**Transaction-Level Indicators:**
- Transactions that are inconsistent with the customer's stated purpose of account or business profile
- Payments to high-risk jurisdictions not aligned with customer's known business relationships
- Round-dollar amounts in wire transfers (exact multiples of $1,000, $5,000, $10,000)
- Transactions with vague or generic memo descriptions (e.g., "consulting," "services rendered") for large amounts
- Back-to-back transactions where funds are deposited and immediately withdrawn or transferred

**Account-Level Indicators:**
- New account receiving large transactions shortly after opening
- Rapid escalation in transaction volume relative to historical baseline
- Multiple accounts controlled by the same customer showing coordinated activity
- Mismatches between transaction channel and customer's registered location

**Customer-Level Indicators:**
- Customer expresses concern about reporting requirements or asks how to avoid documentation
- Customer presents conflicting explanations for transaction purpose across multiple interactions
- Customer conducts transactions in a manner that appears deliberately complex or unusual

### Fraud Reporting Workflow

When a transaction is flagged by the fraud detection engine, the following workflow is initiated:

1. **Automated Hold (T+0):** Transaction placed in pending state; funds movement suspended
2. **FCC Triage (T+4 hours):** FCC analyst reviews flagged transaction against customer history and related transactions
3. **Investigation (T+1 to T+5 days):** Full investigation initiated; customer may be contacted for documentation
4. **Disposition (T+5 days):** Transaction approved, declined, or escalated to SAR filing
5. **SAR Filing (if required, T+30 days from detection):** SAR filed with FinCEN; law enforcement notification if warranted
6. **Case Closure:** Case documented in CMS; ML model updated with outcome label

---

## Risk Thresholds and Alerts

The fraud risk scoring system produces a composite risk score for each transaction on a scale of 0.0 to 1.0. The following alert tiers define the operational response:

| Risk Score | Alert Level | Response |
|---|---|---|
| 0.00 – 0.39 | Low | No action; transaction auto-approved |
| 0.40 – 0.59 | Moderate | Logged for periodic batch review |
| 0.60 – 0.74 | Elevated | Flagged; FCC analyst review within 48 hours |
| 0.75 – 0.89 | High | Transaction held; FCC analyst review within 4 hours |
| 0.90 – 1.00 | Critical | Transaction blocked; immediate FCC escalation; customer authentication required |

In addition to the composite score, any transaction that triggers one or more fraud detection rules (FR-001 through FR-009) is automatically assigned the `is_flagged = TRUE` designation in the transaction record, regardless of the ML model score.

---

## Compliance and Regulatory Requirements

### Bank Secrecy Act (BSA)
The Bank Secrecy Act (31 U.S.C. § 5311 et seq.) requires financial institutions to maintain programs for detecting and reporting suspicious financial activity. Key BSA obligations embedded in the BTPS include:

- **Currency Transaction Reports (CTRs):** Required for cash transactions exceeding $10,000 per day per customer
- **Suspicious Activity Reports (SARs):** Required when the bank knows, suspects, or has reason to suspect that a transaction involves funds from illegal activity, is designed to evade reporting requirements (structuring), lacks a lawful purpose, or involves use of the bank to facilitate criminal activity
- **Recordkeeping:** Transaction records must be maintained for a minimum of 5 years (BSA) and 7 years (internal policy)

### Anti-Money Laundering (AML) Program
The bank's AML program complies with the Financial Crimes Enforcement Network (FinCEN) Customer Due Diligence (CDD) rule and the Bank Secrecy Act. The AML program includes:

- Customer identification and verification at account opening (KYC)
- Ongoing customer due diligence and enhanced due diligence for high-risk customers
- Transaction monitoring through the RFDE
- Independent testing and audit of AML controls at least annually
- Training for all personnel with customer-facing or transaction-processing responsibilities

### USA PATRIOT Act
Section 326 of the USA PATRIOT Act requires customer identification at account opening. The BTPS enforces customer identity verification requirements and screens all customers and transaction counterparties against OFAC's Specially Designated Nationals (SDN) list in real time.

### Regulation E
The Electronic Fund Transfer Act (Regulation E) establishes customer protections for electronic fund transfers. Fraud investigations involving unauthorized electronic transactions must comply with Regulation E error resolution procedures, including provisional credit requirements and investigation timelines.

---

## System Integration Points

| System | Integration Type | Direction | Frequency |
|---|---|---|---|
| Core Banking Ledger (FiServ) | Real-time API | Bidirectional | Per transaction |
| SWIFT Network | Secure message gateway | Outbound | Per wire transfer |
| ACH Gateway (FedACH) | Batch file transfer | Bidirectional | 3x daily |
| OFAC SDN Screening Service | REST API | Outbound | Per transaction |
| FinCEN BSA E-Filing System | Secure file submission | Outbound | Per CTR/SAR |
| CRM (Salesforce Financial Services) | Event streaming | Bidirectional | Near real-time |
| Data Warehouse (Snowflake) | Batch ETL | Outbound | Hourly |
| Fraud Case Management (Actimize) | REST API | Bidirectional | Per flagged transaction |
| Mobile Banking App | REST API | Inbound | Per transaction |
| ATM Network (Fiserv DNA) | ISO 8583 | Bidirectional | Per transaction |

---

## Incident Response Procedures

### Fraud Incident Classification

| Category | Description | Response SLA |
|---|---|---|
| P1 — Critical | Active fraud in progress; customer funds at immediate risk; systemic compromise | 15 minutes |
| P2 — High | Confirmed fraud on multiple accounts; potential coordinated attack | 2 hours |
| P3 — Medium | Single-account fraud confirmed; investigation in progress | 24 hours |
| P4 — Low | Suspected fraud; under investigation; no confirmed loss | 5 business days |

### Response Steps for Confirmed Fraud

1. **Containment:** Freeze affected account(s); disable compromised credentials; block associated payment instruments
2. **Assessment:** Determine scope of unauthorized transactions; identify total customer loss
3. **Customer Notification:** Contact affected customer within 24 hours per Regulation E requirements
4. **Provisional Credit:** Issue provisional credit to customer account within 5 business days of claim receipt
5. **Investigation:** Full forensic review; coordinate with fraud operations, IT security, and legal as appropriate
6. **Regulatory Filing:** File SAR with FinCEN within 30 days of detecting suspicious activity
7. **Recovery:** Initiate return/recall procedures for wire transfers where possible; coordinate with receiving bank
8. **Post-Incident Review:** Document lessons learned; update fraud detection rules; retrain ML models with new fraud patterns

---

## Glossary

| Term | Definition |
|---|---|
| AML | Anti-Money Laundering. Regulatory framework and internal controls designed to prevent the use of the financial system to launder proceeds of criminal activity. |
| BSA | Bank Secrecy Act. Federal law (31 U.S.C. § 5311) requiring financial institutions to assist government agencies in detecting and preventing money laundering. |
| BEC | Business Email Compromise. A fraud scheme where criminals impersonate executives or vendors via email to trick employees into authorizing fraudulent wire transfers. |
| CTR | Currency Transaction Report. A FinCEN form filed for cash transactions exceeding $10,000. |
| CDD | Customer Due Diligence. The process of identifying and verifying customers and assessing their risk profile for AML purposes. |
| FCC | Financial Crimes Compliance. Internal team responsible for investigating fraud, filing regulatory reports, and managing AML/BSA compliance. |
| FinCEN | Financial Crimes Enforcement Network. A bureau of the U.S. Department of the Treasury that administers the BSA. |
| OFAC | Office of Foreign Assets Control. Agency that enforces economic sanctions against countries, individuals, and organizations. |
| SAR | Suspicious Activity Report. A FinCEN form filed when the bank suspects a transaction involves criminal activity. |
| Structuring | The illegal act of breaking up large cash transactions into smaller amounts to avoid the $10,000 CTR reporting requirement. Also called "smurfing." |
| Velocity Rule | A fraud detection rule based on the frequency or rate of transactions within a defined time window. |
| Wire Fraud | Federal crime (18 U.S.C. § 1343) involving the use of electronic communications to carry out a fraudulent scheme. |
| KYC | Know Your Customer. Due diligence process to verify the identity and assess the risk profile of customers. |
| RFDE | Real-Time Fraud Detection Engine. The BTPS component responsible for real-time fraud scoring and rule evaluation. |
| Layering | The second stage of money laundering, involving complex financial transactions designed to obscure the origin of illicit funds. |
| SAR | Suspicious Activity Report. A mandatory report filed with FinCEN within 30 days of detecting suspicious activity that may constitute fraud, money laundering, or other financial crimes. |
