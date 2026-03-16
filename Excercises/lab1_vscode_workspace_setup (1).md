# LAB 1 — VS Code Workspace Setup & Data Exploration

**Duration:** 15 minutes
**Role:** New team member onboarding into an enterprise analytics workspace

---

## Overview

In this lab you will set up VS Code, explore the editor interface, and familiarise yourself with the project workspace before working with enterprise datasets.

By the end of this lab you will be confident navigating the editor, opening different file types, and finding information across a repository — skills used daily by analytics and engineering teams.

**Workspace structure you will explore:**

```
enterprise-data-insights/
├── data/                    ← operational datasets
├── docs/                    ← system documentation
├── analysis/                ← investigation reports
└── diagrams/                ← architecture diagrams
```

---

## Task 1 — Explore the VS Code Interface

**What you will learn:** Identify the core panels of VS Code and understand what each one is used for.

### Steps

1. Launch **VS Code**.
2. Look at the **left sidebar** — this is the Activity Bar. Click each icon to open the corresponding panel.

| Icon | Panel | Purpose |
|------|-------|---------|
| 📄 | Explorer | Browse and open files and folders |
| 🔍 | Search | Search for text across all files |
| 🌿 | Source Control | Review and commit file changes |
| 🧩 | Extensions | Install tools and language support |

3. Open **Explorer**, then **Search**, then **Extensions** one at a time.
4. Notice how the left panel changes with each selection.

### Expected Result

> You should see each panel open and close as you click the icons. The Explorer panel shows the folder tree on the left. The Search panel shows an input box for searching across files. The Extensions panel shows installed and recommended extensions.

---

## Task 2 — Sign In to VS Code

**What you will learn:** Connect VS Code to your GitHub account to unlock Copilot and repository features.

### Steps

1. Click the **Accounts icon** at the bottom of the Activity Bar (person icon, bottom-left).
2. Select **Sign in with GitHub**.
3. Follow the browser authentication flow.
4. Return to VS Code and confirm your GitHub username appears in the Accounts menu.

### Expected Result

> The Accounts menu shows your GitHub username (e.g. `@yourname`). A notification confirms sign-in was successful. Copilot features become available in the toolbar.

> **Why this matters:** Signing in unlocks GitHub Copilot, settings sync across machines, and direct access to your organisation's repositories — all standard in modern enterprise workflows.

---

## Task 3 — Configure the VS Code Theme

**What you will learn:** Use the Command Palette — the fastest way to run any VS Code command.

### Steps

1. Open the **Command Palette** using the keyboard shortcut:

```
CMD + Shift + P
```

2. Type the following command and press **Enter**:

```
Preferences: Color Theme
```

3. A theme picker appears. Try each of the following:

```
Dark+
GitHub Dark
Light+
```

4. Press **Enter** to apply your preferred theme.

### Expected Result

> The editor background colour changes immediately as you scroll through themes. The theme picker closes when you press Enter and your selection is applied. The theme persists after restarting VS Code.

> **Tip:** The Command Palette (`CMD + Shift + P`) is one of the most powerful tools in VS Code. Any feature can be found by typing a keyword — you do not need to memorise menus.

---

## Task 4 — Explore File Types in VS Code

**What you will learn:** VS Code opens different file types natively — CSV data files, spreadsheets, and documentation.

### Steps

1. In the **Explorer panel**, expand the `data/` folder.
2. Click to open each of the following files:

```
data/banking_transactions.csv
data/insurance_claims.xlsx
docs/banking-system.md
```

3. Observe how each file is displayed differently by VS Code.

### Expected Result

| File | How it appears |
|------|---------------|
| `banking_transactions.csv` | Raw comma-separated text with column headers on line 1 |
| `insurance_claims.xlsx` | VS Code prompts to open with a viewer extension or shows raw XML |
| `banking-system.md` | Markdown source with `#` headers and `**bold**` syntax visible |

> **Observation:** CSV files open as plain text — you can scroll and read them directly. Markdown files show the raw syntax until you switch to Preview mode (covered in the next task).

---

## Task 5 — Preview Markdown Documentation

**What you will learn:** Render documentation as formatted output using VS Code's built-in Markdown preview.

### Steps

1. Open the file:

```
docs/banking-system.md
```

2. Open the Markdown preview panel using the keyboard shortcut:

```
CMD + Shift + V
```

3. Alternatively, click the **preview icon** (split screen icon) in the top-right corner of the editor tab.
4. Scroll through the rendered documentation.

### Expected Result

> The raw `#` headers render as large bold headings. Bullet lists, tables, and bold text all appear formatted. The document reads like a professional system specification.
>
> You should see sections including:
> - Banking Transaction Processing System overview
> - Fraud Detection Framework with rules **FR-001** through **FR-009**
> - Risk Thresholds and Alerts table
> - Compliance and Regulatory Requirements

> **Why this matters:** Engineering and analytics teams write all documentation in Markdown. Being able to read and navigate Markdown docs is essential for collaborating in modern repositories.

---

## Task 6 — Open the Project Workspace

**What you will learn:** Open a project folder in VS Code — the standard way to begin working on any project.

### Steps

1. Open the **Command Palette**:

```
CMD + Shift + P
```

2. Type and run:

```
File: Open Folder
```

3. Navigate to and select the **enterprise-data-insights** project folder provided for this course.
4. VS Code will reload with the full project open in the Explorer panel.

> **In a real project:** Teams share code via Git repositories. You would use `Git: Clone` in the Command Palette, paste the repository URL, and VS Code would download the full project automatically. The workflow after cloning is identical to what you are doing now.

### Expected Result

> The Explorer panel shows the full project tree:
>
> ```
> enterprise-data-insights/
> ├── data/
> │   ├── banking_transactions.csv
> │   ├── healthcare_patients.csv
> │   ├── insurance_claims.xlsx
> │   └── stock_trades.csv
> ├── docs/
> │   ├── banking-system.md
> │   ├── healthcare-platform.md
> │   └── trading-system.md
> ├── analysis/
> │   └── risk-investigation-report.md
> └── diagrams/
>     └── system-architecture.md
> ```

---

## Task 7 — Explore the Repository Structure

**What you will learn:** Understand how enterprise projects organise files across folders.

### Steps

1. In the **Explorer panel**, click the arrow next to each folder to expand it:

```
data/
docs/
analysis/
diagrams/
```

2. Click on any file to open it in the editor.
3. Notice the breadcrumb trail at the top of the editor showing the folder path.

### Expected Result

> Each folder opens to reveal its contents. Clicking a file opens it in the editor tab. The breadcrumb trail at the top shows the full path, for example: `enterprise-data-insights > data > banking_transactions.csv`.

> **Structure explained:**
> - `data/` — raw operational datasets used for analysis
> - `docs/` — system documentation written by engineering teams
> - `analysis/` — output reports generated by analysts
> - `diagrams/` — architecture and workflow diagrams

---

## Task 8 — Search Across the Repository

**What you will learn:** Find content across all files instantly — critical when working with large codebases and documentation.

### Steps

1. Open the **Search panel** in the Activity Bar (magnifying glass icon), or use:

```
CMD + Shift + F
```

2. Type the following keyword into the search box:

```
fraud
```

3. Press **Enter** to run the search.
4. Review the list of files and matching lines returned.
5. Click any result to jump directly to that line in the file.

### Expected Result

> VS Code returns matches across multiple files. You should see results similar to:
>
> ```
> docs/banking-system.md        — 40 matches
> docs/healthcare-platform.md   — 19 matches
> docs/trading-system.md        — 23 matches
> ```
>
> Clicking a result opens the file and highlights the matching line. For example, in `docs/banking-system.md` you will see the Fraud Detection Framework section with rules such as:
> - `FR-001: Flag all transactions exceeding $10,000`
> - `FR-003: Flag structuring patterns — multiple deposits just under $10,000`

> **Why this matters:** In real projects, teams use cross-file search constantly — to find where a rule is defined, to locate references to a system, or to understand how a term is used across documentation.

---

## Task 9 — Quick File Search

**What you will learn:** Open any file instantly by name without clicking through folder trees.

### Steps

1. Use the **Quick Open** shortcut:

```
CMD + P
```

2. Type the following into the search bar:

```
transactions
```

3. VS Code will show matching files. Select:

```
data/banking_transactions.csv
```

4. Press **Enter** to open it.

### Expected Result

> The Quick Open bar shows a filtered list of files containing "transactions" in the name. The file `data/banking_transactions.csv` appears at the top of the results. Pressing Enter opens it immediately in the editor without navigating the Explorer panel.

> **Tip:** Quick Open is the fastest way to jump between files in large projects. Professional developers use it constantly instead of clicking through folder trees.

---

## Task 10 — Investigate the Banking Dataset

**What you will learn:** Read and scan a real enterprise dataset to build familiarity before using Copilot to analyse it in Lab 2.

### Steps

1. Open the file:

```
data/banking_transactions.csv
```

2. Scroll through the data and look for the following patterns manually:

- Large transaction amounts (above $10,000)
- The same customer ID appearing multiple times in a short period
- Wire transfers to "International Wire"
- Transactions at unusual hours (timestamps between 02:00–04:00)
- Cash deposits that are just below $10,000
- Identical amounts repeated by the same customer

3. Note at least **3 observations** that seem unusual.

### Expected Result

> As you scroll, you should be able to spot patterns such as:
>
> | Observation | Example rows |
> |------------|-------------|
> | Customer C2001 makes 5 cash deposits ranging $9,700–$9,900 on the same date (2024-03-15) | TXN00001–TXN00005 |
> | Customer C2003 withdraws exactly $5,000 at an ATM on 6 consecutive days | TXN00014–TXN00019 |
> | Wire transfers of $87,500–$96,000 sent to "International Wire" between 02:00–04:00 | TXN00020–TXN00022 |
> | Customer C2007 — a single large transfer of $45,000 with no prior activity | TXN00023 |
>
> You do not need to fully analyse the data here. This manual scan builds awareness before Copilot accelerates the investigation in Lab 2.

---

## Lab 1 — Success Criteria

Before moving to Lab 2, confirm you can do all of the following:

- [ ] Identify and open Explorer, Search, Source Control, and Extensions panels
- [ ] Sign into VS Code with your GitHub account
- [ ] Open the Command Palette and run commands
- [ ] Change the editor colour theme
- [ ] Open CSV, Excel, and Markdown files in the editor
- [ ] View rendered Markdown documentation using preview
- [ ] Navigate the project folder structure in the Explorer panel
- [ ] Search for keywords across all files using the Search panel
- [ ] Open files instantly by name using Quick Open (`CMD + P`)
- [ ] Identify at least 3 suspicious patterns in `banking_transactions.csv` by eye

---

> **You are now ready for Lab 2** — where you will use GitHub Copilot to analyse the datasets and produce a professional financial risk investigation report.
