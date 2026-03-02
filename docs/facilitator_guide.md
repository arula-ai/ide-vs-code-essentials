# Facilitator Guide
## VS Code Essentials for Analysts — NovaTrend Retail

> **For instructor use only.** Do not distribute to participants before the session.

---

## Pre-Session Setup (Complete 30–60 minutes before start)

### Repository Setup Checklist

- [ ] Repository created on GitHub from the lab blueprint
- [ ] `lab-start` branch contains starter files with TODO scaffolding (no solution code)
- [ ] `solution-reference` branch contains all completed files
- [ ] Sample data generated: run `python3 generate_sample_data.py` from repo root
- [ ] This creates CSV files AND `data/raw/sales_data.xlsx` (needed for Lab 4)
- [ ] All three branches pushed to GitHub
- [ ] Participant access granted — each person can clone the repo
- [ ] Participants have confirmed: repo cloned locally, Python packages installed
- [ ] Confirm openpyxl is installed on participant machines: `pip install openpyxl`

### Demo Machine Setup Checklist (10 minutes before participants arrive)

- [ ] VS Code open with `vscode-analyst-ai-lab` folder loaded
- [ ] On `lab-start` branch: `git checkout lab-start`
- [ ] GitHub Copilot signed in and responding (test a prompt in Copilot Chat)
- [ ] Extensions installed: Rainbow CSV, Python, Jupyter, GitLens, Markdown All-in-One
- [ ] Terminal open and working (`Ctrl+``)
- [ ] Projector or screen share showing your VS Code (zoom in if needed — font size 16+)
- [ ] Quick reference cards printed — **one per participant** — placed at each station
- [ ] Visible countdown timer ready (phone, projector timer, or second tab)
- [ ] Backup plan: PDF of solution walkthrough on your desktop

### Participant Verification (the day before)

Send participants a simple pre-lab check email:
```
Please confirm before the session:
1. VS Code is installed (code.visualstudio.com)
2. Python 3.10+ is installed (python.org)
3. Run in terminal: pip install pandas numpy matplotlib openpyxl
4. Clone the lab repo: git clone [your-repo-url]
5. Open the folder in VS Code and confirm you see the data/ and docs/ folders
6. Run: python3 generate_sample_data.py  (creates all data files including Excel)

If anything fails, reply to this email immediately.
```

---

## Audience Context — Read Before Every Session

**Who is in the room:**
- Business analysts, data analysts, financial analysts, operations analysts
- Some have written SQL; most have never used a terminal or Python
- Excel, BI dashboards, and SQL tools are their typical environment
- Primary anxiety: "I will break something" and "I won't understand the Python parts"
- Primary motivation: Becoming faster at their actual work; learning to use Copilot effectively

**What creates engagement:**
- Business context before technology — always explain WHY before HOW
- Visible quick wins — the first file open, first Copilot response, first commit
- Relatable analogies — use the ones in the guide, they work
- Celebrating every milestone out loud ("Who just got clean_sales.csv? Raise your hand!")
- Normalizing confusion — "If this feels weird, good. That means you are learning."

**What creates anxiety:**
- Moving too fast through Phase 3 (Python) — slow down here
- Error messages in the terminal with no explanation — demystify immediately
- Git commands without context — always give the analogy before the command

---

## Core Analogies to Use Throughout

| Technical Concept | Analogy That Works |
|---|---|
| Git repository | Filing cabinet that keeps every version of every document |
| Git branch | "Save As" with a different filename — your work, your name |
| Git commit | Clicking Save with a required description attached |
| Git staging (`git add`) | Highlighting the changes you want to include before saving |
| Pull Request | Sending a document for review before you finalize it |
| Terminal | The command line is like talking to your computer instead of clicking |
| Python script | An automated Excel macro — runs instructions top to bottom |
| DataFrame (`df`) | A spreadsheet table living in computer memory |
| SQL query | A very precise question you ask a database in a structured language |
| Markdown | Word formatting but simplified — `**bold**` instead of Ctrl+B |
| Copilot | A very fast, knowledgeable intern who writes first drafts instantly |

---

## Lab-by-Lab Facilitation Guide

### Lab 1: Workspace & Documentation (0:00 – 0:05)

**Start by saying:**
> "Welcome everyone. Let's start by setting up your workspace — think of this as
> getting your office ready before the workday. VS Code is where analysts and
> developers alike manage their data, scripts, and documentation."

**Demonstrate live:**
1. Open the folder, trust the authors, show extension install popup
2. Click through the folder structure in Explorer — name each folder
3. Open `business_context.md` → show formatted preview (Cmd+Shift+V)
4. Create `notes.md` live — show Copilot auto-suggestion with Tab
5. Show how to use Copilot Chat to improve the project overview text

**Facilitator observations:**
- Who cannot find the Explorer panel? → View → Explorer (left sidebar icon)
- Who sees raw Markdown symbols? → Remind them of `Cmd+Shift+V`
- Who is not getting Copilot suggestions? → Verify Copilot extension + GitHub sign-in

**Success check (ask aloud):**
> "Who can see their notes.md in the Explorer panel with a data dictionary table?"

---

### Lab 2: Clone & Update Analytics Repo (0:05 – 0:15)

**Start by saying:**
> "Your data team works in Git every day — this is how they share code without
> overwriting each other's work. Today you are going to use the exact same workflow.
> First commit ever? That is the milestone we are celebrating."

**Demonstrate the Git workflow live before participants try:**
1. Show `git status` — explain red vs. green files
2. Run `git checkout -b analysis-demo` on the projector
3. Make a small edit to `notes.md`
4. Run `git add .`, then `git commit -m "Demo commit"`
5. Show `git log --oneline` — point to the commit hash and message

**Key teaching moment:** Pause on the commit message.
> "What you write here is the description in your version history. 'Updates' is useless.
> 'Add analyst observations to data dictionary' tells a story."

**Facilitator watch points:**
- If participants are on the wrong branch: `git status` shows the branch name at top
- If `nothing to commit`: they did not save the file (Cmd+S first)
- If push fails: skip push — local commit is sufficient for the lab objective

**Success check:**
> "Run `git log --oneline` — who sees their commit at the top? Raise your hand."

---

### Lab 3: Copilot for Analysis Tasks (0:15 – 0:25)

**Start by saying:**
> "Copilot is not magic — it is a very fast first-draft writer. You give it context,
> it gives you code. You review whether it makes sense. That combination is what
> makes your team faster. Today you are joining that workflow."

**Demonstrate one interaction live:**
1. Open `scripts/data_cleaning.py` — show the TODO 1 comment
2. Paste the date parsing prompt into Copilot Chat
3. Read the response together: "Is this doing what we asked? Let's check..."
4. Paste the code into the script

**Then show the 'explain this code' prompt:**
1. Select a chunk of Python code
2. Paste into Copilot Chat with "Explain in plain English"
3. Read the response aloud — ask group: "Is this accurate?"

**Key discussion at 0:22:**
> "What analyst tasks could you ask Copilot to do that you currently spend the most time on?"

**Facilitator watch points:**
- Participants accepting code without reading it — prompt them: "What does TODO 2 do?"
- Copilot giving MySQL syntax instead of SQLite — remind them to specify "SQLite" in the prompt

**Success check:**
> "Who has at least one code block pasted into a script file? Who has a plain-English
> explanation added to their notes?"

---

### Lab 4: Spreadsheet Analysis (0:25 – 0:40) — HIGHEST COMPLEXITY LAB

**Start by saying:**
> "You receive spreadsheets from 10 people formatted 10 different ways. What if you
> had a script that automatically cleaned, summarized, and charted any spreadsheet
> you received? That is what you are building right now — and you can adapt it for
> your own work starting tomorrow."

**Demonstrate virtual environment setup live before participants try:**
1. Run `python3 -m venv venv` — explain: "a clean room for this project's software"
2. Run `source venv/bin/activate` (Mac) — show `(venv)` appearing in prompt
3. Run `pip install pandas openpyxl matplotlib` — let it install on screen
4. Confirm with `pip list`

**Walk the room during TODO completion — do not stay at the projector.**

Common issues to watch for:
- `(venv)` not showing → venv not activated → re-run activate command
- `FileNotFoundError` for xlsx → `generate_sample_data.py` not run yet → run it now
- Chart file not appearing → check `data/processed/` folder in Explorer
- Script exits immediately → missing TODO code → show one TODO solution as example

**Intervention at ~0:35 (10 minutes in):**
> "Who has the monthly revenue summary printing in their terminal? Raise your hand."
> Help anyone who is stuck on venv activation — that is the most common blocker.

**Celebrate every output:**
> "Who just saw the chart file appear in their processed folder? You just built an
> analysis pipeline. That script works on any Excel file you point it at."

**At 0:38, call out to the group:**
> "Everyone should have at least one query result on their screen by now.
> If you don't, raise your hand."

**At 0:43, ask 2–3 participants:**
> "What did you find? Tell me a number."
> Push for specificity: "North had more revenue — how much more? What percentage?"

This normalizes sharing results and reinforces that specific numbers matter.

**Common facilitator interventions:**
- Cell ran with error → check they ran Cell 3 and Cell 5 first (most common miss)
- `MONTH()` function error → show SQLite syntax: `strftime('%m', date)`
- Participant can't see results → check they ran `run_query(query_1)` not just defined `query_1`

**Success check:**
> "State your best finding with a specific number. If you can't yet, keep going."

---

### Phase 5: Documentation (0:45 – 0:55)

**Start by saying:**
> "A finding without a story is just a number. Your job now is to translate
> what you found into something a busy executive can absorb in 90 seconds.
> This is the skill your data teams desperately wish their business stakeholders had."

**Demonstrate the split view live:**
1. Open `insight_report_template.md`
2. Press `Cmd+\` to split — show both panes
3. Press `Cmd+Shift+V` in the right pane — show the live preview
4. Type a few characters on the left — let them watch the right update
5. This is often a "wow" moment — lean into it

**Common facilitator interventions:**
- Participants spending too long on formatting → "Content first. Formatting second."
- Participants pasting Copilot text without editing → "Does it sound like you? Does it have your numbers?"
- Participants paralyzed by finding 3 → "Use your data quality finding as Finding 3"

**Success check:**
> "Who has an executive summary written — even a rough one? Raise your hand."

---

### Phase 6: Collaboration / Git (0:55 – 1:00) — SECOND HIGHEST ANXIETY PHASE

**Start by saying:**
> "Last step — something developers do dozens of times every week. We are going to save
> your work to a branch. Think of it as naming a document before sending it for review."

**Type every command live on the projector — participants follow along:**
1. `git status` — show the red files — "This is everything you changed"
2. `git add .` — "We are staging — selecting what to save"
3. `git status` again — "Green means staged — ready to commit"
4. `git checkout -b insight-[yourname]`
5. `git commit -m "Add analysis and insight report — [Your Name]"`
6. `git log --oneline` — show the commit

**Say after the commit:**
> "That commit is permanent. Your work is saved with your name on it.
> Every developer on your team has done that exact sequence today."

**If participants get stuck:**
- Have the quick reference card Git section visible on the projector
- Offer to pair — type together
- The `git status` → `git add .` → `git commit` sequence is the core

**Success check:**
> "Who sees their own commit message in `git log`? Raise your hand."

**After the last hand goes up — show the solution branch:**
```bash
git checkout solution-reference
```
Walk through:
1. Completed `data_cleaning.py` — show how close participants got
2. Sample completed SQL queries
3. A sample filled insight report — show what "good" looks like
4. `git log --oneline` — the commit history

---

## Post-Session Debrief (5–10 minutes)

Facilitate this discussion before releasing participants:

1. **"What surprised you most about this workflow?"**
   *(Listen for: AI is faster than expected / data is messier than expected)*

2. **"Where do you see this being useful in your own work — without becoming a developer?"**
   *(Listen for: Copilot for writing, understanding team work, better questions to ask)*

3. **"How does going through this change how you'll work with your technical team?"**
   *(Listen for: more empathy, better requirements, less fear of the tools)*

4. **"What is one thing you will try in the next week?"**
   *(Concrete commitment — increases follow-through significantly)*

---

## Contingency Plans

### If Copilot is not working for participants:
1. Show the prompts and expected outputs live on the projector
2. Participants copy from the projector into their files manually
3. The learning is in reading and understanding the code — not just the typing

### If Python/terminal is blocking a majority of the room at Phase 3:
1. Provide the solution code from `solution-reference`
2. Let participants focus on RUNNING and READING the output
3. The data cleaning content is: knowing what issues exist and that tools can fix them

### If time runs short:
- **Must preserve:** Phase 2 (Copilot exploration) and Phase 6 (Git commit)
- **Can compress:** Phase 3 (provide solution code) and Phase 5 (require only 1 finding + exec summary)
- **Never skip:** The debrief — it is where the learning crystallizes

### If a participant gets a merge conflict:
- Stop them immediately — do not let them try to resolve it alone
- Pair with them directly
- In most cases: `git checkout lab-start` and start the branch again from scratch

---

## Assessment During the Session

Use the observer sheet in `docs/assessment_rubric.md` to track each participant.

Key observations to make:
- Who completes `clean_sales.csv` before the 30-minute mark?
- Who states a finding with a specific number vs. a vague observation?
- Who evaluates Copilot's output critically vs. accepting it blindly?
- Who successfully creates their own branch and commit?

---

## Session Variations

### 45-Minute Version (remove one phase):
- Skip Phase 3 entirely — pre-clean the data and provide `clean_sales.csv` already in `data/processed/`
- Focus on: Environment → AI Exploration → Insight Generation → Documentation → Git

### 90-Minute Version (add depth):
- Allow 20 minutes for Phase 3 (group discussion after cleaning)
- Allow 20 minutes for Phase 4 (intermediate queries required, not optional)
- Add a 10-minute "sharing" segment at the end where each participant presents their top finding

### 2-Hour Workshop Version:
- Full lab as designed (60 min) + 30 min of stretch goals + 30 min group presentation

---

## What to Reveal from `solution-reference` at the End

Only after every participant has committed their own branch:

```bash
git checkout solution-reference
```

Walk through in this order:
1. `scripts/data_cleaning.py` — completed — compare with what participants wrote
2. `sql/analysis_queries.sql` — completed — compare approaches
3. `docs/insight_report_template.md` — filled sample — what "good" looks like
4. `git log --oneline` — show the full commit history

Keep this brief (5 minutes maximum). The point is not to show the "right answer" —
it is to validate their work and show the benchmark.

---

## Post-Session Actions

**Immediately after the session:**
- [ ] Distribute post-lab survey (digital or paper) — response rate drops dramatically after 24 hours
- [ ] Share the post-lab resource list and take-home challenge
- [ ] Collect observation/assessment sheets
- [ ] Note 3 things to improve for next session while fresh

**Within 24 hours:**
- [ ] Send follow-up email with: repo link, resource list, two-week challenge
- [ ] Score observation sheets and flag participants for follow-up sessions

**At 30 days:**
- [ ] Send 30-day follow-up survey (4 questions, 2 minutes max)
- [ ] Track "VS Code opened since lab" and "Copilot used since lab" rates

---

## Success Metrics Targets

| Metric | Target |
|---|---|
| Reach Phase 5 | 90% of participants |
| Produce `clean_sales.csv` | 95% of participants |
| State a finding with a number | 85% of participants |
| Complete a Git commit | 80% of participants |
| Attempt 3+ Copilot prompts | 100% of participants |
| Post-survey confidence delta | +1.5 average across all 5 questions |

---

*Facilitator Guide — Internal document. Review before every session.*
*Last updated: Production v1.0*
