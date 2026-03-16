# Participants Guide
## VS Code for Business Professionals — AI-Assisted Data Investigation

**Total Duration:** 60 minutes
**Tools:** Visual Studio Code · GitHub Copilot

---

## Quick Reference

| Shortcut | Action |
|----------|--------|
| `CMD + Shift + P` | Open Command Palette |
| `CMD + Shift + I` | Open Copilot Chat |
| `CMD + Shift + V` | Markdown preview |
| `CMD + Shift + F` | Search across all files |
| `CMD + Shift + G` | Source Control panel |
| `CMD + P` | Quick file open |

**Copilot modes** — select from the dropdown at the top of the Copilot Chat panel:

| Mode | Use it when you want to… |
|------|--------------------------|
| **Ask** | Read a document, explore data, ask questions |
| **Plan** | Generate a step-by-step strategy |
| **Agent** | Create or update a file |

---

---

# LAB 1 — VS Code Workspace Setup

**Duration:** 15 minutes · **Role:** New team member onboarding into the project workspace

---

## Task 1 — Explore the VS Code Interface

1. Launch **VS Code**.
2. Click each icon in the **left Activity Bar** to open and explore these panels:

| Icon | Panel | What it does |
|------|-------|-------------|
| 📄 | Explorer | Browse folders and open files |
| 🔍 | Search | Find text across all files |
| 🌿 | Source Control | Review and commit changes |
| 🧩 | Extensions | Install tools and language support |

3. Switch between Explorer, Search, and Extensions one at a time.

---

## Task 2 — Sign In to VS Code

1. Click the **Accounts icon** at the bottom-left of the Activity Bar.
2. Select **Sign in with GitHub** and complete the browser sign-in.
3. Confirm your GitHub username appears in the Accounts menu.

> Signing in activates GitHub Copilot and repository access.

---

## Task 3 — Configure the Editor Theme

1. Open the Command Palette:

```
CMD + Shift + P
```

2. Type and run:

```
Preferences: Color Theme
```

3. Try `Dark+`, `GitHub Dark`, or `Light+` and select your preference.

---

## Task 4 — Open the Project Workspace

1. Open the Command Palette:

```
CMD + Shift + P
```

2. Run:

```
File: Open Folder
```

3. Navigate to and select the **enterprise-data-insights** project folder.

> The Explorer panel will show the full project structure with `data/`, `docs/`, `analysis/`, and `diagrams/` folders.

---

## Task 5 — Explore Different File Types

Open each of the following files from the Explorer panel and observe how VS Code displays each type differently:

```
data/banking_transactions.csv
data/insurance_claims.xlsx
docs/banking-system.md
```

> CSV opens as plain text. Excel may prompt a viewer extension. Markdown shows raw syntax until previewed.

---

## Task 6 — Preview Markdown Documentation

1. Open the file:

```
docs/banking-system.md
```

2. Open Markdown preview:

```
CMD + Shift + V
```

3. Scroll through the rendered document — headings, tables, and rules should all appear formatted.

---

## Task 7 — Search and Navigate the Repository

1. Open the Search panel:

```
CMD + Shift + F
```

2. Search for:

```
fraud
```

3. Review which files return results and click a result to jump directly to that line.

4. Now use Quick Open to jump to a file by name:

```
CMD + P
```

5. Type `transactions` and open:

```
data/banking_transactions.csv
```

---

## Task 8 — First Look at the Banking Dataset

1. Open the file:

```
data/banking_transactions.csv
```

2. Scroll through the data and note at least **3 things that look unusual** — large amounts, repeated patterns, odd hours, or identical transactions.

> This dataset is the primary source for the investigation in Lab 2.

---

## Lab 1 — Checklist

- [ ] Explored Explorer, Search, Source Control, and Extensions panels
- [ ] Signed in to VS Code with GitHub
- [ ] Changed the editor theme via Command Palette
- [ ] Opened the project folder
- [ ] Opened a CSV, Excel, and Markdown file
- [ ] Previewed `docs/banking-system.md` in Markdown preview
- [ ] Searched for "fraud" across all files
- [ ] Spotted at least 3 unusual patterns in `banking_transactions.csv`

---

---

# LAB 2 — Financial Risk Investigation Using Copilot

**Duration:** 30 minutes · **Role:** Financial Risk Analyst — Meridian Financial Group

You have been assigned to a formal risk investigation by the Risk Committee. Your mandate, the systems involved, and the 10 questions you must answer are all in a briefing document — start there before opening any data.

---

## Phase 1 — Read the Investigation Briefing

**File type: `.md` — Meeting notes**
**Copilot mode: Ask**

Open Copilot Chat:

```
CMD + Shift + I
```

Set mode to **Ask**.

---

### Step 1 — Summarise the Briefing

1. Open the file and read through it:

```
docs/risk-committee-briefing.md
```

2. Attach it to Copilot Chat using the **paperclip icon (📎)**.
3. Run this prompt:

```
Summarise the key points of this risk committee briefing. List: the three business areas under investigation, the suspicious patterns that triggered each investigation, the data sources available, and the 10 priority questions the team must answer.
```

> Copilot returns a structured summary of the investigation scope and data sources.

---

### Step 2 — Ask About Investigation Priorities

With the briefing still attached, run:

```
Based on this briefing, what is the highest-priority pattern to investigate first in the banking transactions dataset and why? What specific column values should I look for?
```

> Copilot reasons about investigation priorities and tells you exactly what data patterns to look for — use this as your starting point for Phase 3.

---

## Phase 2 — Understand the Fraud Detection Rules

**File type: `.md` — System documentation**
**Copilot mode: Ask**

---

### Step 1 — Extract Fraud Rules from System Documentation

1. Open the file:

```
docs/banking-system.md
```

2. Attach it to Copilot Chat.
3. Run this prompt:

```
List all fraud detection rules in this document (FR-001 onwards) as a table with: Rule ID, Rule Name, Trigger Condition, and Recommended Action. Then identify which rules are most relevant to the investigation in the risk committee briefing.
```

> Copilot produces a fraud rules reference table you can use while investigating the data in the next phases.

---

## Phase 3 — Plan the Investigation

**Files: `.md` documents**
**Copilot mode: Plan**

Switch Copilot to **Plan** mode.

---

### Step 1 — Generate the Investigation Plan

1. Attach both files:
   - `docs/risk-committee-briefing.md`
   - `docs/banking-system.md`
2. Run this prompt:

```
Using the risk committee briefing and the banking fraud detection rules, create a step-by-step investigation plan covering: banking transaction analysis, insurance claim analysis, and cross-system pattern analysis. For each step specify: which file to examine, which columns to focus on, and what pattern to look for.
```

> Copilot generates a structured investigation roadmap you will follow in Phases 4 and 5.

Switch Copilot back to **Ask** before continuing.

---

## Phase 4 — Investigate the Banking Dataset

**File type: `.csv` — Structured transaction data**
**Copilot mode: Ask**

---

### Step 1 — Identify Suspicious Transactions

1. Open the file in the editor:

```
data/banking_transactions.csv
```

2. Attach it to Copilot Chat.
3. Run this prompt:

```
Analyse this banking transactions dataset and identify all transactions that may indicate fraud or financial risk. Group findings by pattern type: (1) structuring — multiple cash deposits just under $10,000 from the same customer on the same day, (2) geographic velocity — same customer in multiple regions within minutes, (3) round-number repeated ATM withdrawals, (4) large international wire transfers between 22:00–06:00, (5) dormant account sudden large activity. List the specific transaction IDs and customer IDs for each finding.
```

> Copilot identifies and groups suspicious transactions by fraud pattern type, with specific transaction IDs and severity.

---

## Phase 5 — Investigate the Insurance Claims Register

**File type: `.xlsx` — Excel spreadsheet**
**Copilot mode: Ask**

---

### Step 1 — Identify High-Risk Claims

1. Open the file in the editor:

```
data/insurance_claims.xlsx
```

2. Attach it to Copilot Chat.
3. Run this prompt:

```
Analyse this insurance claims dataset and identify claims that represent high financial risk. Focus on: claims with risk scores above 0.75, claim amounts that are statistical outliers, and geographic concentration in CA or NY regions that overlap with the banking investigation. Provide specific claim IDs and values.
```

> Copilot surfaces high risk-score claims, outlier amounts, and geographic overlaps with the banking findings.

---

## Phase 6 — Generate the Investigation Report

**Copilot mode: Agent**

Switch Copilot to **Agent** mode.

---

### Step 1 — Write the Report

1. Attach all three files:
   - `docs/risk-committee-briefing.md`
   - `data/banking_transactions.csv`
   - `data/insurance_claims.xlsx`
   - `analysis/risk-investigation-report.md`
2. Run this prompt:

```
Using the risk committee briefing and the findings from both datasets, populate the investigation report template at analysis/risk-investigation-report.md. The report must: answer all 10 priority questions from the briefing, reference specific transaction IDs and claim records as evidence, assign severity ratings (High/Medium/Low) to each finding, include an executive summary for the Risk Committee, and provide actionable recommendations. Save the completed report.
```

**Output file:**

```
analysis/risk-investigation-report.md
```

3. Open and preview the report:

```
CMD + Shift + V
```

> The completed investigation report with all sections populated, findings referenced by ID, severity ratings, and recommendations for the Risk Committee.

---

## Lab 2 — Checklist

- [ ] Read `docs/risk-committee-briefing.md` and extracted the 10 investigation questions
- [ ] Asked Copilot to reason about investigation priorities, not just summarise
- [ ] Extracted fraud detection rules from `docs/banking-system.md` as a table
- [ ] Switched to Plan Mode and generated a structured investigation plan
- [ ] Investigated `data/banking_transactions.csv` and identified suspicious patterns with transaction IDs
- [ ] Investigated `data/insurance_claims.xlsx` for high risk-score claims and geographic patterns
- [ ] Switched to Agent Mode and generated the completed investigation report
- [ ] Verified `analysis/risk-investigation-report.md` is fully populated

---

---

# LAB 3 — Validation, Documentation & Collaboration

**Duration:** 15 minutes · **Role:** Product Manager reviewing a report from your analytics team

You have received the investigation report. Your job is to validate it, improve the documentation, and submit the updates to the shared repository.

---

## Task 1 — Review the Investigation Report

1. Open the file:

```
analysis/risk-investigation-report.md
```

2. Preview it:

```
CMD + Shift + V
```

3. Check that all three sections are populated: banking risk, insurance risk, and cross-system patterns.

> If any section shows placeholder text, return to Lab 2 Phase 6 and re-run the Agent Mode prompt.

---

## Task 2 — Validate the Report Against the Source Data

**Copilot mode: Ask**

Open Copilot Chat and set mode to **Ask**.

1. Attach all three files:
   - `analysis/risk-investigation-report.md`
   - `data/banking_transactions.csv`
   - `data/insurance_claims.xlsx`
2. Run this prompt:

```
Review the risk investigation report and verify whether the findings are supported by the datasets. For each finding, confirm whether the transaction IDs or claim records exist in the data. Identify any suspicious patterns in the datasets that are missing from the report, and flag any statements that cannot be verified from the data.
```

> Copilot confirms which findings are data-backed, identifies any gaps, and flags any unsupported claims in the report.

---

## Task 3 — Improve the Investigation Report

**Copilot mode: Agent**

Switch Copilot to **Agent** mode.

1. Attach `analysis/risk-investigation-report.md` and `data/banking_transactions.csv`.
2. Run this prompt:

```
Improve the financial risk investigation report at analysis/risk-investigation-report.md by: organising findings into clearly labelled sections for Banking Risk, Insurance Claim Risk, and Cross-System Patterns; ensuring each finding references a specific transaction ID or claim ID; replacing any vague statements with evidence-based observations; and adding a risk severity rating (High, Medium, or Low) next to each finding. Save the updated file.
```

**Output file:**

```
analysis/risk-investigation-report.md
```

> An improved report with specific IDs, evidence-based language, and severity ratings on every finding.

---

## Task 4 — Update the Banking System Documentation

**Copilot mode: Agent**

1. Open the file:

```
docs/banking-system.md
```

2. Attach `docs/banking-system.md`, `data/banking_transactions.csv`, and `analysis/risk-investigation-report.md`.
3. Run this prompt:

```
Based on the suspicious patterns found in the banking transactions dataset and investigation report, generate updated fraud detection rules for the banking system. Format each rule with: Rule ID, Rule Name, Trigger Condition, Threshold, and Recommended Action. Append these rules as a new section titled "## Updated Fraud Detection Rules — Q1 2024 Review" at the bottom of docs/banking-system.md. Save the file.
```

**Output file:**

```
docs/banking-system.md
```

> New fraud detection rules appended to the banking system documentation, derived directly from investigation findings.

---

## Task 5 — Review Changes in Source Control

1. Open the Source Control panel:

```
CMD + Shift + G
```

2. You should see these files listed under Changes:

```
analysis/risk-investigation-report.md
docs/banking-system.md
diagrams/system-architecture.md
```

3. Click `docs/banking-system.md` to open the **diff view**.
4. Review the highlighted changes — green lines are additions, red lines are removals.
5. Repeat for `analysis/risk-investigation-report.md`.

> The diff view shows exactly what changed — identical to how engineering teams review documentation updates before merging.

---

## Task 6 — Commit and Push to the Repository

1. In the Source Control panel, click **+** to stage each changed file.
2. Enter the following commit message:

```
Add financial risk investigation report and update fraud detection rules
```

3. Click **✓ Commit**.
4. Click **Sync Changes** to push to the remote repository.

> Changes committed and shared with the team — the investigation is complete.

---

## Lab 3 — Checklist

- [ ] Reviewed `analysis/risk-investigation-report.md` in Markdown preview
- [ ] Validated the report against source data and identified any gaps
- [ ] Improved the report with specific IDs and severity ratings
- [ ] Updated `docs/banking-system.md` with new fraud detection rules
- [ ] Reviewed the diff for each changed file in Source Control
- [ ] Committed and pushed all changes with a descriptive commit message

---

---

# Course Complete

You have completed the full enterprise analytics workflow:

| Lab | Role | What you did |
|----|------|-------------|
| Lab 1 | Team member | Set up VS Code and explored the project workspace |
| Lab 2 | Risk Analyst | Read the briefing, extracted fraud rules, investigated data, generated a report |
| Lab 3 | Product Manager | Validated, improved, documented, and committed findings |

**Files you produced:**

```
analysis/risk-investigation-report.md   ← investigation report
docs/banking-system.md                  ← updated with new fraud detection rules
diagrams/system-architecture.md         ← architecture diagram (see Bonus)
```

---

---

# Bonus Activities

Complete these if you finish early or want to go deeper.

---

## Bonus 1 — Cross-System Pattern Analysis

**Copilot mode: Ask**

1. Attach both datasets:
   - `data/banking_transactions.csv`
   - `data/insurance_claims.xlsx`
2. Run this prompt:

```
Comparing the banking transactions and insurance claims datasets, identify cross-system patterns that could indicate coordinated financial risk or organised fraud. Look for: geographic overlap between flagged banking transactions and high-risk insurance claims, time-period correlations, and value-level alignment between large banking transfers and high-value claims. Summarise the combined risk picture.
```

> A cross-system analysis identifying patterns that individual dataset review would miss — the kind of insight that uncovers organised fraud rings.

---

## Bonus 2 — Visualise the Financial Investigation Workflow

**Copilot mode: Agent**

1. Open and attach the file:

```
diagrams/system-architecture.md
```

2. Run this prompt:

```
Create a mermaid flowchart diagram showing the end-to-end financial investigation workflow at Meridian Financial Group. Include nodes for: Customer, Banking System, Insurance System, Trading System, Fraud Detection Engine, Risk Analyst, Risk Committee, and Investigation Report. Add labelled arrows showing data flow and escalation paths. Insert the complete mermaid diagram into diagrams/system-architecture.md and save it.
```

**Output file:**

```
diagrams/system-architecture.md
```

3. Preview the diagram:

```
CMD + Shift + V
```

> A visual Mermaid flowchart of the end-to-end financial investigation workflow, rendered in Markdown preview.

> If the diagram does not render, install **Markdown Preview Mermaid Support** from the Extensions panel.

---

## Bonus 3 — Investigate the Stock Trading Dataset

**Copilot mode: Ask**

1. Open and attach:

```
data/stock_trades.csv
```

2. Run this prompt:

```
Analyse this stock trading dataset and identify trades that may indicate market misconduct. Look for: insider trading patterns (large profitable trades placed immediately before significant price movements), wash trading (offsetting buy and sell trades between related accounts on the same stock and day), and coordinated pump-and-dump activity (multiple traders buying the same stock in a short window followed by rapid selling). List the specific trade IDs and trader IDs for each pattern found.
```

> Copilot identifies suspicious trading patterns including insider trading, wash trading, and coordinated manipulation — extending the investigation into the trading system.

---

## Bonus 4 — Generate a Healthcare Risk Summary

**Copilot mode: Ask**

1. Open and attach:

```
docs/healthcare-platform.md
```

2. Run this prompt:

```
Summarise the key risk indicators described in this healthcare platform documentation. What are the main fraud types it describes, and what data signals would an analyst look for to detect each one?
```

> A summary of healthcare billing fraud types and detection signals — practice reading and extracting insights from a different domain's system documentation.
