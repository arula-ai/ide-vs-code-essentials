# Git Basics for Analysts
## The 6 Commands Every Analyst Needs

> Git is a system that tracks every change to every file in a project — and lets you work
> safely without overwriting anyone else's work. You do not need to know all of Git.
> You need these 6 commands.

---

## The Analogy

| Git Concept | Think of It As |
|---|---|
| **Repository (repo)** | A shared project folder with complete version history |
| **Branch** | Your personal copy of the folder — safe to edit without affecting others |
| **Staging** | Selecting which files to include in your next "save" |
| **Commit** | A named, permanent snapshot — "Save with a description" |
| **Push** | Uploading your saves to the shared server |
| **Pull** | Downloading the latest changes from the shared server |

---

## The 6 Commands

### 1. `git status`
**What it does:** Shows what has changed since your last save.

```bash
git status
```

- **Red files** = changed but not staged yet
- **Green files** = staged and ready to commit
- **Nothing listed** = everything is saved and up to date

**When to use it:** Before anything else. Always run this first to know where you stand.

---

### 2. `git checkout -b [branch-name]`
**What it does:** Creates a new branch and switches to it.

```bash
git checkout -b analysis-sarah
```

This creates your personal workspace. Changes you make here do not affect the main branch
until you intentionally merge them.

**Naming convention:** Use lowercase, hyphens for spaces.
- `analysis-sarah` ✅
- `Analysis Sarah` ❌

**When to use it:** At the start of any new piece of work.

---

### 3. `git add .`
**What it does:** Stages all changed files for the next commit.

```bash
git add .
```

The `.` means "all changed files." To stage just one file:
```bash
git add scripts/spreadsheet_analysis.py
```

**When to use it:** After you have finished making changes and are ready to save.

---

### 4. `git commit -m "Your message here"`
**What it does:** Creates a permanent, named snapshot of all staged changes.

```bash
git commit -m "Add Q1 spreadsheet analysis script — Sarah Johnson"
```

**Good commit messages:**
- `Add spreadsheet analysis script with monthly summary`
- `Fix date format in data cleaning script`
- `Update data dictionary with discount_pct definition`

**Bad commit messages:**
- `updates` ❌
- `asdf` ❌
- `final final FINAL` ❌

**When to use it:** After `git add .`, whenever you want to checkpoint your work.

---

### 5. `git log --oneline`
**What it does:** Shows a compact history of all commits on your current branch.

```bash
git log --oneline
```

Output looks like:
```
a3f8c12 Add Q1 spreadsheet analysis script — Sarah Johnson
b7d2e91 Update data dictionary with discount_pct definition
c1a4f05 Initial lab setup
```

The short code on the left (`a3f8c12`) is the commit's unique ID. You can return to any
commit using `git checkout a3f8c12`.

**When to use it:** To verify your commit was saved, or to review work history.

---

### 6. `git push origin [branch-name]`
**What it does:** Uploads your branch and its commits to the remote server (GitHub/GitLab).

```bash
git push origin analysis-sarah
```

First-time push on a new branch:
```bash
git push --set-upstream origin analysis-sarah
```

**When to use it:** When you are ready to share your work or back it up to the server.

---

## The Standard Analyst Workflow

```
1. git checkout -b analysis-[yourname]    ← Create your branch
2. [do your work — edit files, run scripts]
3. git status                              ← See what changed
4. git add .                               ← Stage everything
5. git commit -m "Describe what you did"  ← Save with a description
6. git push origin analysis-[yourname]    ← Upload to the server
```

Repeat steps 2–6 as many times as needed.

---

## Common Errors & Fixes

| Error Message | What It Means | Fix |
|---|---|---|
| `nothing to commit` | No files have changed | Make a change, save it, then try `git add .` again |
| `not a git repository` | You are in the wrong folder | Make sure you opened the `vscode-analyst-ai-lab` folder |
| `branch already exists` | That branch name is taken | Add a suffix: `analysis-sarah-v2` |
| `Your branch has no upstream` | Branch not yet on the server | Run `git push --set-upstream origin [branch-name]` |
| `Changes not staged for commit` | You forgot `git add .` | Run `git add .` then `git commit` again |
| `Merge conflict` | Two people edited the same line | Stop and ask your instructor — do not try to resolve alone |

---

## VS Code Git Panel (Visual Alternative)

VS Code has a built-in Git panel that provides a visual interface for all of these commands:

1. Click the **Source Control** icon in the left sidebar (looks like a branch with dots)
2. Changed files appear in a list — click the `+` to stage them
3. Type a commit message at the top and press `Cmd+Enter` (Mac) or `Ctrl+Enter` (Windows)
4. Click the `...` menu to push, pull, or create a new branch

Both the terminal commands and the VS Code panel do exactly the same thing — use whichever
you find more comfortable.

---

## Vocabulary Reference

| Term | Definition |
|---|---|
| **Repository (repo)** | A project folder with complete version history built in |
| **Branch** | An isolated copy of the repo for safe, independent work |
| **Commit** | A saved snapshot with a description — the core unit of Git |
| **Staging area** | A holding zone where you select changes before committing |
| **Push** | Sending your local commits to a remote server (GitHub, GitLab, Azure DevOps) |
| **Pull** | Downloading the latest commits from the remote server |
| **Merge** | Combining changes from one branch into another |
| **Pull Request (PR)** | A formal request to review and merge your branch — used in team workflows |
| **Clone** | Downloading a remote repository to your local machine for the first time |
| **Origin** | The default name for the remote server your repository lives on |

---

*Keep this cheat sheet. The 6 commands above cover 90% of what analysts need from Git.*
