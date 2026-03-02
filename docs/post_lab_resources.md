# Post-Lab Resources
## Continuing Your Learning After the Session

> You have completed the VS Code Essentials for Analysts lab.
> These resources help you build on what you learned today.

---

## Recommended Learning Path

| Topic | Resource | Format | Cost | Priority |
|---|---|---|---|---|
| VS Code | Microsoft Learn: "Get Started with VS Code" | Interactive | Free | High |
| GitHub Copilot | GitHub Docs: "Getting Started with Copilot" | Documentation | Free | High |
| Git | Oh My Git! (ohmygit.org) | Game | Free | High |
| Git | Atlassian Git Tutorial | Written guide | Free | Medium |
| SQL | Mode Analytics SQL Tutorial | Browser-based | Free | High |
| SQL | SQLZoo.net | Interactive | Free | Medium |
| Markdown | markdownguide.org | Reference | Free | Low |
| Python for Analysts | "Python for Data Analysis" — Wes McKinney | Book | Paid | Advanced |

---

## Two-Week Take-Home Challenge

Repeat this workflow with your own business data to reinforce the skills.

### Week 1 Challenge: Explore Your Own Data

1. Export any regular report you receive as a `.csv` file
   *(Examples: weekly sales report, CRM export, project tracking export)*
2. Open the file in VS Code — install Rainbow CSV if prompted
3. Open Copilot Chat and ask:
   ```
   I have a CSV with business data. The columns are: [list your columns].
   What are the 5 most important business questions I should investigate?
   ```
4. Create a `notes.md` file and document:
   - 3 business questions worth answering
   - 2 data quality issues you notice
5. Share one observation with a colleague

**Goal:** Spend 30 minutes maximum. The point is the habit, not the depth.

---

### Week 2 Challenge: Clean and Analyze

1. Open `scripts/data_cleaning.py` from the lab
2. Adapt the TODOs to your own CSV's specific issues
3. Run the script on your data (may need to adjust column names)
4. Create a simple insight report using `docs/insight_report_template.md`
5. Commit your work: `git add . && git commit -m "Week 2 personal data analysis"`

**Goal:** One concrete insight from your own data, documented in Markdown.

---

## Recommended Follow-Up Courses

| Course | What You Will Learn | Audience |
|---|---|---|
| SQL in VS Code | Writing queries, JOINs, subqueries, window functions, and running them against real databases from VS Code | All analysts |
| Python for Analysts | Automating reports with pandas, working with APIs, scheduling data pulls, advanced data transformations | Anyone who completed today's lab |
| Documentation & Requirements in Markdown | Writing technical specs, requirements documents, data dictionaries, and ADRs at a professional level | Analysts, BAs, product managers |
| Copilot for Analytics Workflows | Advanced prompt engineering for SQL, Python, and documentation — context management, multi-step prompts, code review with Copilot | All analysts who want to go deeper |

---

## Key Concepts to Reinforce

Take 10 minutes this week to explain these concepts to a colleague.
Teaching something is the fastest way to solidify your own understanding.

1. **Git branch analogy:** "It is like creating a separate copy of a document with my name on it, where I can make changes safely without affecting the original."

2. **What Copilot actually is:** "It is an AI trained on billions of lines of code. It predicts what code is most likely to be useful based on context — like autocomplete, but for entire functions. It is fast and often right, but it can be confidently wrong. You always review its output."

3. **Why data cleaning matters:** "In our Q1 data, dates were in three different formats. If you grouped by month without fixing that, January would be split into three separate rows — '01', 'Jan', and '01/'. Your numbers would be completely wrong."

4. **What a commit is:** "It is a permanent, named snapshot of your work at a specific point in time. Every developer on your team has committed code today. Now you have too."

---

## Vocabulary Builder

Print or save this list — use these terms in your next conversation with your technical team:

| Term | Definition | Use It In A Sentence Like This |
|---|---|---|
| **Repository (repo)** | A project folder with complete version history | "Can you share the repo link so I can see the latest version?" |
| **Branch** | An isolated working copy of the project | "Are you working on a feature branch or main?" |
| **Pull Request (PR)** | A request to review and merge your changes | "The PR for the new dashboard is up — who is reviewing it?" |
| **Commit** | A saved snapshot with a description | "When was the last commit before this started breaking?" |
| **DataFrame** | A table of data in Python (like a spreadsheet in memory) | "What does the DataFrame look like after the join?" |
| **Pipeline** | An automated sequence of data processing steps | "Is the data quality issue upstream in the pipeline or downstream?" |
| **Schema** | The structure of a database or table (column names and types) | "Has the schema changed recently? Are all column names the same?" |
| **Environment** | The specific software configuration where code runs | "Does it work in your local environment or only in production?" |
| **Debug** | Finding and fixing the cause of an error | "I need 30 minutes to debug this — the data looks off after the join." |
| **Version control** | System for tracking changes to files over time (Git) | "Is this in version control? I want to see what changed last week." |

---

## Quick Wins You Can Do Today

1. **Open VS Code** and browse any text file you have on your computer. Just get comfortable with the tool.

2. **Ask Copilot a business question.** Go to copilot.github.com or use the chat in VS Code. Ask: "Summarize the key risks of a retail company that relies heavily on discounting."

3. **Read one Git commit message** from a project your team works on. Go to GitHub → your team's repo → click "Commits." What do the messages tell you about what changed?

4. **Export a CSV from any system you use** — a CRM, a project tool, an analytics dashboard. Open it in VS Code. Just look at it.

---

---

## Analyst Use Cases to Try This Week

Here are five things you can do with VS Code and the skills from today's lab:

1. **Open any CSV export** from your CRM, project tracker, or reporting tool in VS Code. Install Rainbow CSV. Browse the data with fresh eyes.

2. **Create a notes.md file** for your next analysis project. Use the data dictionary format from Lab 1 to document columns before you start working.

3. **Copy any SQL query** you use regularly and ask Copilot: *"Explain what this query does in plain English and suggest one way to improve it."*

4. **Run the spreadsheet_analysis.py script** on your own data. Replace `sales_data.xlsx` with any Excel file from your work. Adjust the column names in TODOs 2–4.

5. **Commit your next analysis** to a Git repository. Create a branch with your name, do your work, commit with a descriptive message. Just practice the habit.

---

*These resources are provided as part of the VS Code Essentials for Analysts lab.*
*For questions, contact your session facilitator.*
