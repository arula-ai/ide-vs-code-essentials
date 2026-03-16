
# VS Code for Business Professionals
## AI‑Assisted Data Investigation & Collaboration

**Course Duration:** 60 minutes

This hands‑on course introduces participants to **Visual Studio Code (VS Code)** and **GitHub Copilot** as practical tools for modern data exploration, analysis, and collaboration.

The course focuses on three core capabilities used in real organizations:

**1. Setting up a professional VS Code workspace**
Participants learn how to configure and navigate a modern development environment. This includes exploring project folders, working with different file types — Markdown documents, CSV datasets, and Excel spreadsheets — and understanding how teams organize data, documentation, and analysis inside a shared workspace.

**2. Analyzing real‑world business problems using Copilot**
Participants work as financial risk analysts investigating a real investigation mandate. They begin by reading meeting notes and system documentation, build an investigation strategy, then move into structured datasets to identify suspicious patterns. Using Copilot's Ask, Plan, and Agent modes, they work across multiple file types — exactly as analysts do in real organizations.

**3. Validating insights and documenting results for collaboration**
Participants review the generated investigation report, validate findings against source data, update system documentation, and commit changes to the repository. This simulates the final stage of an enterprise analytics workflow where business and technical teams collaborate using shared repositories.

Together, these activities simulate a modern analytics workflow:

```
Workspace Setup → Read Briefing → Explore Docs → Plan → Investigate Data → Report → Validate → Collaborate
```

---

# Project Repository Structure

Participants work inside a prepared project workspace that simulates a typical enterprise repository.

```
enterprise-data-insights/
│
├── data/
│   ├── banking_transactions.csv     ← banking transaction ledger (250 records)
│   ├── insurance_claims.xlsx        ← insurance claims register
│   └── stock_trades.csv             ← market trade surveillance data (200 records)
│
├── docs/
│   ├── risk-committee-briefing.md   ← investigation mandate and priorities (Lab 2 start)
│   ├── banking-system.md            ← banking fraud detection system specification
│   ├── healthcare-platform.md       ← healthcare platform specification
│   └── trading-system.md            ← market surveillance system specification
│
├── analysis/
│   └── risk-investigation-report.md ← investigation report (generated in Lab 2)
│
└── diagrams/
    └── system-architecture.md       ← architecture diagram (generated in Lab 2)
```

This structure mirrors real project environments used by engineering and analytics teams:

- **data/** — operational datasets exported from enterprise systems
- **docs/** — system specifications, meeting notes, and process documentation
- **analysis/** — analytical outputs and investigation reports
- **diagrams/** — workflow and architecture diagrams

---

# Key Files Used in the Course

Participants work with several common file types used in real projects.

### Documentation Files (Markdown — `.md`)

```
docs/risk-committee-briefing.md    ← read first in Lab 2 — investigation mandate
docs/banking-system.md             ← fraud detection rules and data schema
docs/healthcare-platform.md        ← claims processing and risk scoring
docs/trading-system.md             ← market surveillance rules
```

### Data Files

```
data/banking_transactions.csv      ← CSV — primary banking dataset with flagged transactions
data/insurance_claims.xlsx         ← Excel — insurance claims register with risk scores
data/stock_trades.csv              ← CSV — stock trade surveillance data
```

### Generated Outputs

During the labs participants will create or update:

```
analysis/risk-investigation-report.md    ← produced in Lab 2 using Agent Mode
docs/banking-system.md                   ← updated in Lab 3 with new fraud rules
diagrams/system-architecture.md          ← Mermaid diagram generated in Lab 2
```

These outputs represent the results of the investigation and documentation workflow.

---

# Lab Overview

| Lab | Duration | Role | Focus |
|-----|---------|------|-------|
| **Lab 1** | 15 min | New team member | VS Code setup, file types, workspace navigation |
| **Lab 2** | 30 min | Financial Risk Analyst | Briefing → System docs → Data investigation → Report |
| **Lab 3** | 15 min | Product Manager | Validate, document, review, and commit |

---

# Lab 2 File‑Type Progression

Lab 2 is structured to teach participants how to work with different file types in a logical investigation sequence — exactly as real analysts do:

```
docs/risk-committee-briefing.md  →  docs/banking-system.md  →  data/banking_transactions.csv  →  data/insurance_claims.xlsx
       (Meeting notes .md)              (System docs .md)              (Structured data .csv)             (Spreadsheet .xlsx)
```

This progression ensures participants understand *why* they are looking at data before they look at it — a critical professional habit.

---

# Course Completion Rules

Participants complete the course successfully when they:

### 1. Configure and Explore the Workspace
Participants should be able to:

- navigate VS Code panels
- open project folders
- search across files
- open and preview CSV, Excel, and Markdown files

### 2. Produce an Investigation Report

Participants generate a completed analysis report at:

```
analysis/risk-investigation-report.md
```

The report must:

- answer all 10 priority questions from the risk committee briefing
- reference specific transaction IDs and claim records as evidence
- include severity ratings and actionable recommendations

### 3. Validate and Document Results

Participants update system documentation using investigation findings:

```
docs/banking-system.md
```

Participants review the changes in Source Control and commit to the repository.

---

# Business Outcomes

After completing this course participants will be able to:

- set up and navigate a VS Code workspace
- read and analyse Markdown documentation using Copilot
- extract structured information from meeting notes and system specifications
- use GitHub Copilot Ask Mode to explore data, documents, and ask analytical questions
- use GitHub Copilot Plan Mode to generate structured investigation strategies
- use GitHub Copilot Agent Mode to create reports and update files
- investigate CSV and Excel datasets for suspicious patterns
- generate investigation reports with AI assistance
- validate findings against source data
- update technical documentation with evidence-based improvements
- commit and share results using Git workflows

These capabilities enable business professionals to work effectively within **modern AI‑assisted development environments**, where analysis, documentation, and collaboration happen inside the same workspace.

---

# End of Course Overview
