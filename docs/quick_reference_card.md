# Quick Reference Card
## AI-Powered Analyst Workflow Lab — NovaTrend Retail

> Keep this open throughout the session. Everything you need is on this page.

---

## VS Code: Essential Shortcuts

| Action | Mac | Windows |
|---|---|---|
| Open terminal | `` Ctrl+` `` | `` Ctrl+` `` |
| Find and open a file | `Cmd+P` | `Ctrl+P` |
| Open Copilot Chat | `Cmd+Shift+I` | `Ctrl+Shift+I` |
| Split editor pane | `Cmd+\` | `Ctrl+\` |
| Preview Markdown | `Cmd+Shift+V` | `Ctrl+Shift+V` |
| Save file | `Cmd+S` | `Ctrl+S` |
| Format document | `Shift+Option+F` | `Shift+Alt+F` |
| Open command palette | `Cmd+Shift+P` | `Ctrl+Shift+P` |
| Open Extensions panel | `Cmd+Shift+X` | `Ctrl+Shift+X` |
| Find text in file | `Cmd+F` | `Ctrl+F` |
| Undo last action | `Cmd+Z` | `Ctrl+Z` |

---

## GitHub Copilot: How to Use

| Action | How to Do It |
|---|---|
| Accept inline suggestion | Press `Tab` |
| Dismiss suggestion | Press `Esc` |
| See next suggestion | `Option+]` (Mac) / `Alt+]` (Windows) |
| Open Chat panel | `Cmd+Shift+I` / `Ctrl+Shift+I` |
| Ask about selected code | Select code → right-click → Copilot → Explain This |
| Trigger suggestion manually | Type a `#` comment describing what you want |

### Tips for Better Copilot Results

| Tip | Example |
|---|---|
| Be specific — name your variables | "In DataFrame 'df' with column 'revenue'..." |
| Include file or table names | "From table called 'sales_transactions'..." |
| State what format you want | "Return the result as a pandas DataFrame" |
| Ask it to explain | "Explain what this code does in plain English" |
| Iterate if the first answer is off | "That's close — but I also need to include units_sold" |

---

## Git: The 6 Commands You Need Today

```bash
git checkout lab-start           # Switch to the lab starting branch
git status                       # See which files you have changed (red = unstaged)
git add .                        # Stage ALL changed files for the next commit
git checkout -b insight-[name]   # Create YOUR named branch and switch to it
git commit -m "Your message"     # Save a snapshot with a description
git log --oneline                # View your commit history (one line per commit)
```

**Bonus — if you push to GitHub:**
```bash
git push origin insight-[name]   # Upload your branch to GitHub
git push --set-upstream origin insight-[name]  # First push (sets tracking)
```

---

## Git in Plain English

| Git Term | Plain English Equivalent | Analogy |
|---|---|---|
| Repository | Project folder with full history | A shared filing cabinet with every version ever saved |
| Branch | A named working copy | "Save As" with a different filename |
| Commit | A saved checkpoint with a label | Clicking Save with a description written on it |
| Staging (`git add`) | Choosing what to include in the save | Highlighting the sections you want to copy |
| Pull Request | Submitting your version for review | Emailing a document for feedback before finalizing |
| Merge | Combining two versions together | Accepting tracked changes in Word |
| Clone | Downloading a full copy of a repository | Checking out a project file from the company shared drive |

---

## Jupyter Notebook: How to Run Code

| Action | How to Do It |
|---|---|
| Run a cell | `Shift+Enter` |
| Run all cells from top | Menu → Run → Run All |
| Add a new cell below | Click `+` button at top of notebook |
| Cell not yet run | Shows `[ ]` on the left |
| Cell ran successfully | Shows `[1]` or `[2]` etc. |
| Cell ran with an error | Shows red error text below the cell |

**Important:** Always run cells in order — top to bottom. Later cells depend on earlier ones.

---

## Python Quick Reference

| What You See | What It Means |
|---|---|
| `df` | Your data table (DataFrame) — like a spreadsheet in memory |
| `df.head()` | Show the first 5 rows |
| `df.shape` | Show (number of rows, number of columns) |
| `df.isnull().sum()` | Count missing values per column |
| `df['column_name']` | Select a single column |
| `df.to_csv('file.csv')` | Save the DataFrame to a CSV file |
| `#` | Comment — the computer ignores this line; it is a note for humans |

---

## Markdown Quick Reference

```
# Heading 1               → Largest heading
## Heading 2              → Section heading
### Heading 3             → Subsection heading
**bold text**             → Bold
*italic text*             → Italic
- bullet point            → Bulleted list item
  - indented bullet       → Sub-bullet (indent with 2 spaces)
- [ ] task not done       → Unchecked checkbox
- [x] task done           → Checked checkbox
| Col A | Col B |         → Table (add | --- | --- | on the next line)
| --- | --- |             → Table divider row
`code snippet`            → Inline code (single backtick)
```

---

## Terminal Navigation (Bash)

| Command | What It Does |
|---|---|
| `pwd` | Print working directory — shows where you are |
| `ls` | List files and folders in current location |
| `cd scripts` | Move into the `scripts` folder |
| `cd ..` | Go up one level (back to parent folder) |
| `python data_cleaning.py` | Run a Python script |
| `pip install pandas` | Install the pandas package |

---

## Common Errors and Fixes

| Error | What It Means | Fix |
|---|---|---|
| `ModuleNotFoundError: pandas` | Pandas not installed | Run `pip install pandas numpy` |
| `FileNotFoundError` | Python can't find the file | Check you ran `cd scripts` first |
| `NameError: returns_df` | Variable was never created | Complete TODO 4 in the script |
| `IndentationError` | Python spacing is off | Make sure pasted code aligns with surrounding code |
| `OperationalError: no such table` | SQL engine not set up | Re-run Cells 3 and 5 in the notebook |
| Red text in terminal | There was an error | Read the last red line — it describes the problem |

---

## Phase Timing At a Glance

| Phase | Activity | Time |
|---|---|---|
| 1 | Warm-Up: Orient in VS Code | 0:00 – 0:05 |
| 2 | Explore: AI-assisted question forming | 0:05 – 0:15 |
| 3 | Clean: Fix raw data with Python | 0:15 – 0:30 |
| 4 | Analyze: SQL insights | 0:30 – 0:45 |
| 5 | Document: Write the insight report | 0:45 – 0:55 |
| 6 | Collaborate: Git commit and branch | 0:55 – 1:00 |

---

*Print this card. Keep it visible throughout the session.*
