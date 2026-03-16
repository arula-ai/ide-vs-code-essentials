# LAB 3 — Validation, Documentation & Collaboration

**Duration:** 15 minutes
**Role:** Product Manager reviewing a financial risk investigation report
**Mission:** Validate findings, improve documentation, and submit updates to the shared repository

---

## Overview

In this lab you will act as a **product manager who has received a risk investigation report** from your analytics team.

Your job is to:

1. Review and validate the report against the source data
2. Improve the report's clarity using Copilot
3. Update the banking system documentation with new fraud detection rules
4. Review your changes in Source Control
5. Commit and push your updates to the team repository

This simulates the final stage of a **real enterprise analytics workflow** — where business and technical teams collaborate to validate findings, update documentation, and share outputs.

---

## Task 1 — Open and Review the Investigation Report

**What you will learn:** How to read and evaluate an AI-generated analytical report as a business stakeholder.

### Steps

1. Open the file:

```
analysis/risk-investigation-report.md
```

2. Open it in Markdown preview for easier reading:

```
CMD + Shift + V
```

3. Read through the report and check that it covers all three investigation areas:

| Section | What to look for |
|---------|-----------------|
| Banking Transaction Risk | Suspicious transaction IDs listed, risk pattern types named |
| Insurance Claim Risk | High risk-score claims identified, amounts noted |
| Cross-System Patterns | Geographic or value correlations described |

### Expected Result

> The report renders as a formatted document with clear section headings. All four sections (Executive Summary, Banking Risk, Insurance Risk, Cross-System Patterns) should be populated — not blank.
>
> If any section is still showing placeholder text `[Copilot will generate this section...]`, return to Lab 2 Phase 4 and re-run the Agent Mode prompt before continuing.

---

## Task 2 — Validate the Report Using Copilot

**What you will learn:** Use Copilot as a validation tool — checking whether AI-generated findings accurately reflect the source data.

### Steps

1. Open **Copilot Chat** (`CMD + Shift + I`).
2. Set the mode to **Ask**.
3. Attach all three files using the paperclip icon (📎):
   - `analysis/risk-investigation-report.md`
   - `data/banking_transactions.csv`
   - `data/insurance_claims.xlsx`
4. Enter the following prompt:

```
Review the risk investigation report and verify whether the findings are supported by the datasets provided. For each finding in the report, confirm whether the relevant transaction IDs or claim records exist in the data. Identify any suspicious patterns in the datasets that are missing from the report, and flag any statements in the report that cannot be verified from the data.
```

### Expected Result

> Copilot should return a structured validation response such as:
>
> **Verified Findings:**
> *"The structuring pattern for customer C2001 is confirmed — transactions TXN00001–TXN00005 show five cash deposits between $9,700–$9,900 on 2024-03-15.*
>
> *The geographic velocity anomaly for C2002 is confirmed — 8 transactions across CA, NY, TX, FL within minutes on 2024-06-20.*
>
> *Wire transfers for C2004 ($92,000), C2005 ($87,500), and C2006 ($96,000) all initiated between 02:00–04:00 are confirmed in the dataset."*
>
> **Potential Gaps:**
> *"The report does not specifically mention the business account anomaly for customer C2009. The dataset contains flagged unusual cash deposits into a Business account that should be included in the report."*
>
> **Unverifiable Claims:**
> *"The statement about 'coordinated fraud rings' cannot be confirmed from the current datasets without a shared customer identifier linking the banking and insurance records."*

> **Validation checkpoint:** Copilot should confirm at least 3 specific transaction IDs from the banking dataset. If it cannot, try rephrasing: `Check whether transaction TXN00001 through TXN00005 are mentioned in the report and whether they match the data.`

---

## Task 3 — Improve the Investigation Report

**What you will learn:** Use Copilot Agent Mode to act on validation feedback and improve document quality.

### Steps

1. Switch Copilot to **Agent Mode** using the mode selector.
2. Attach:
   - `analysis/risk-investigation-report.md`
   - `data/banking_transactions.csv`
3. Enter the following prompt:

```
Improve the financial risk investigation report at analysis/risk-investigation-report.md by: reorganising the findings into clearly labelled sections for Banking Risk, Insurance Claim Risk, and Cross-System Patterns; ensuring each finding references the specific transaction ID or claim ID from the datasets; replacing any vague or generic statements with specific, evidence-based observations; and adding a concise risk severity rating (High, Medium, or Low) next to each finding. Save the updated file.
```

4. After Copilot confirms the file was saved, open it in Markdown preview and review the changes.

### Expected Result

> The updated report should have:
>
> - Clear section headings (`## Banking Risk Analysis`, `## Insurance Claim Risk`, `## Cross-System Patterns`)
> - Specific transaction IDs referenced (e.g. *"TXN00020 — C2004 — $92,000 wire transfer at 02:14 — HIGH"*)
> - Risk severity labels (High / Medium / Low) on each finding
> - No placeholder text remaining
>
> Example of an improved finding entry:
>
> ```
> | TXN00001–TXN00005 | C2001 | $9,700–$9,900 | Structuring | HIGH |
> | TXN00020          | C2004 | $92,000       | Odd-hour international wire | HIGH |
> | TXN00023          | C2007 | $45,000       | Dormant account reactivation | HIGH |
> ```

> **Save the file** before continuing to Task 4.

---

## Task 4 — Update System Documentation

**What you will learn:** How business professionals update technical documentation using findings from analytical work — a key collaboration task in engineering teams.

### Steps

1. Open the documentation file:

```
docs/banking-system.md
```

2. Scroll to the bottom of the file and locate the existing **Fraud Detection Framework** section.
3. Open Copilot Chat. Attach:
   - `docs/banking-system.md`
   - `data/banking_transactions.csv`
   - `analysis/risk-investigation-report.md`
4. Enter the following prompt:

```
Based on the suspicious patterns identified in the banking transactions dataset and the investigation report, generate an updated set of fraud detection rules for the banking system. Format them as a numbered list with: Rule ID, Rule Name, Trigger Condition, Threshold, and Recommended Action. Append these rules as a new section titled "## Updated Fraud Detection Rules — Q1 2024 Review" at the bottom of docs/banking-system.md. Save the file.
```

### Expected Result

> Copilot appends a new section to `docs/banking-system.md` with rules such as:
>
> ```markdown
> ## Updated Fraud Detection Rules — Q1 2024 Review
>
> **FR-010 — Structuring Detection (Enhanced)**
> - Trigger: 3 or more cash deposits between $9,000–$9,999 from the same customer within 24 hours
> - Threshold: Any amount < $10,000 deposited 3+ times in one day
> - Action: Freeze account pending SAR filing; escalate to Compliance team
>
> **FR-011 — Geographic Velocity Alert**
> - Trigger: Same customer_id in more than 2 distinct regions within 60 minutes
> - Threshold: 2+ states, < 60 minutes
> - Action: Suspend transaction processing; require identity verification
>
> **FR-012 — After-Hours Wire Transfer Review**
> - Trigger: International wire transfer > $50,000 initiated between 22:00–06:00
> - Threshold: Amount > $50,000, timestamp outside business hours
> - Action: Hold for next-business-day manual approval by Risk Officer
>
> **FR-013 — Dormant Account Reactivation**
> - Trigger: Account with no activity for 90+ days initiates a transfer > $10,000
> - Threshold: 90-day inactivity followed by transfer > $10,000
> - Action: Require two-factor authentication; notify account holder
> ```

> **Validation:** Open `docs/banking-system.md` and confirm the new section appears at the bottom of the file. The rules should reference patterns actually found in the `banking_transactions.csv` data.

---

## Task 5 — Review Changes in Source Control

**What you will learn:** How to review file changes in VS Code before committing — identical to how engineering teams review documentation updates.

### Steps

1. Open the **Source Control panel** in the Activity Bar (the branch icon), or use:

```
CMD + Shift + G
```

2. You should see the following files listed under **Changes**:

```
analysis/risk-investigation-report.md   (M — Modified)
docs/banking-system.md                  (M — Modified)
diagrams/system-architecture.md         (M — Modified)
```

3. Click on `docs/banking-system.md` in the Changes list to open the **diff view**.
4. Review the highlighted changes:
   - **Green lines** — newly added content
   - **Red lines** — removed or replaced content
5. Repeat for `analysis/risk-investigation-report.md`.

### Expected Result

> The diff view shows the new fraud detection rules section added at the bottom of `docs/banking-system.md` highlighted in green. No existing content should be shown in red (the task was to append, not replace).
>
> For `analysis/risk-investigation-report.md`, the diff shows the improved findings sections replacing the placeholder text — old placeholder lines in red, new populated content in green.

> **Why this matters:** Reviewing diffs before committing ensures you are only sharing intended changes with your team. In real projects this step prevents accidental data exposure, avoids overwriting a colleague's work, and creates a clear audit trail.

---

## Task 6 — Commit and Push Changes to the Repository

**What you will learn:** Commit changes with a professional commit message and push them to the shared repository.

### Steps

1. In the **Source Control panel**, click the **+** icon next to each modified file to stage it:

```
analysis/risk-investigation-report.md
docs/banking-system.md
diagrams/system-architecture.md
```

2. Click the **Message** box at the top of the Source Control panel.
3. Type the following commit message:

```
Add financial risk investigation report and update fraud detection rules
```

4. Click the **✓ Commit** button (or press `CMD + Enter` in the message box).
5. Click **Sync Changes** (or **Push**) to push the commit to the remote repository.

### Expected Result

> VS Code confirms the commit with a notification. The changed files disappear from the Changes list — meaning they are now clean and committed.
>
> The Source Control panel shows **0 pending changes** and the sync indicator shows the branch is up to date with the remote.
>
> If prompted to set upstream, click **OK** — this happens the first time you push a branch.

> **Commit message best practice:** Good commit messages describe *what changed and why*, not just *what file was edited*. The message `Add financial risk investigation report and update fraud detection rules` tells a teammate exactly what this commit contains — without needing to open any files.

---

## Lab 3 — Success Criteria

Confirm you completed all of the following before finishing the course:

- [ ] Opened and reviewed the investigation report in Markdown preview
- [ ] Validated the report against source data using Copilot Ask Mode
- [ ] Identified at least one gap or unverified claim in the report
- [ ] Improved the report using Copilot Agent Mode with specific transaction IDs and severity ratings
- [ ] Updated `docs/banking-system.md` with new fraud detection rules based on investigation findings
- [ ] Opened the Source Control panel and reviewed the diff for each changed file
- [ ] Staged all changed files and committed with a descriptive commit message
- [ ] Pushed changes to the remote repository

---

## Course Workflow Summary

You have now completed the full enterprise analytics workflow:

| Lab | Role | Activity | Output |
|----|------|---------|--------|
| Lab 1 | Team Member | Workspace setup and data exploration | Familiarity with the project |
| Lab 2 | Risk Analyst | Financial investigation using Copilot | `analysis/risk-investigation-report.md` |
| Lab 3 | Product Manager | Validation, documentation, and collaboration | Updated docs committed to repository |

---

## What You Can Now Do

After completing this course you can apply these skills immediately:

| Skill | Real-world application |
|-------|----------------------|
| Navigate VS Code | Work alongside engineering teams in shared project environments |
| Open and read datasets | Review operational data without needing separate tools |
| Use Copilot Ask Mode | Get instant explanations of data, code, and documentation |
| Use Copilot Plan Mode | Generate structured analysis approaches for any problem |
| Use Copilot Agent Mode | Create reports, update files, and automate documentation tasks |
| Use Source Control | Review and commit changes as part of team workflows |
| Write commit messages | Communicate changes clearly in shared repositories |

These capabilities allow you to **collaborate directly with engineering and analytics teams** inside modern AI-assisted development environments — using the same tools, the same workflows, and the same repositories.

---

> **Course complete.** Well done.
