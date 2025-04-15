# 🛠️ Git Workflow Practice – Step-by-Step

This document captures a full example of working with Git locally — from initializing a repository to branching, committing, reverting, and merging.

---

## 📁 Step 1: Initialize a New Repository

```bash
mkdir myrepo
cd myrepo
git init
```

> ✅ This creates a new Git repository in the `myrepo` folder.  
> ℹ️ Git uses `master` as the default branch (can be changed to `main`, `development`, etc.).

---

## 📂 Step 2: Check Git Metadata

```bash
ls -la .git
```

> ✅ Lists the internal Git configuration and tracking folders.

---

## 📝 Step 3: Add a New File

```bash
touch newfile
git add newfile
```

> ✅ Creates a new file and stages it for commit.

---

## 🙋‍♀️ Step 4: Configure Git Identity

```bash
git config --global user.email "you@example.com"
git config --global user.name "Your Name"
```

> ✅ Sets your Git identity for commits.

---

## 💾 Step 5: Make Your First Commit

```bash
git commit -m "added newfile"
```

> ✅ Commits the `newfile` with a message.

---

## 🌿 Step 6: Create and Switch to a New Branch

```bash
git branch my1stbranch
git checkout my1stbranch
```

> ✅ Creates and switches to `my1stbranch`.

---

## 🚫 Optional: Trying to Create an Existing Branch Again

```bash
git checkout -b my1stbranch
# Output: fatal: A branch named 'my1stbranch' already exists.
```

> ⚠️ You already created the branch earlier.

---

## ✏️ Step 7: Modify File and Add Another

```bash
echo 'Here is some text in my newfile.' >> newfile
touch readme.md
git add readme.md
git status
```

> ✅ Adds new text to `newfile` and creates `readme.md`.  
> `git status` shows that:
- `readme.md` is staged.
- `newfile` is modified but not staged.

---

## 📥 Step 8: Stage All and Commit

```bash
git add *
git commit -m "added readme.md modified newfile"
```

> ✅ Commits both files in one go.

---

## 📚 Step 9: Review Commit History

```bash
git log
```

> ✅ Shows the commit history with hashes, author, and messages.

---

## ⏪ Step 10: Revert the Last Commit

```bash
git revert HEAD --no-edit
```

> ✅ Reverts the last commit (`readme.md` and `newfile` changes), deleting `readme.md`.

---

## 🆕 Step 11: Add Another File and Commit

```bash
touch goodfile
git add goodfile
git commit -m "added goodfile"
git log
```

> ✅ Adds a new file and shows updated commit history.

---

## 🔀 Step 12: Merge Changes to `master`

```bash
git checkout master
git merge my1stbranch
```

> ✅ Brings changes from `my1stbranch` into `master` via fast-forward merge.

---

## 🧹 Step 13: Delete Merged Branch

```bash
git branch -d my1stbranch
```

> ✅ Deletes the feature branch after merging.

---

## ✅ Final Git Log Overview

```bash
git log
```

> Shows the full history of:
- Initial commit (`newfile`)
- Addition of `readme.md` and modification of `newfile`
- Revert of that commit
- Addition of `goodfile`
- Merge into `master`

---

### 🎉 Summary

| Step | Action                      | Description                             |
|------|-----------------------------|-----------------------------------------|
| 1    | `git init`                  | Start a new repo                        |
| 2    | `git add`, `git commit`     | Track and save changes                  |
| 3    | `git branch`, `git checkout`| Create/switch branches                  |
| 4    | `git revert`                | Undo previous commit                    |
| 5    | `git merge`                 | Merge branches                          |
| 6    | `git log`, `git status`     | Review progress                         |
| 7    | `git branch -d`             | Clean up merged branches                |

---

> 🧠 **Note**: This is a great practice sequence for learning Git basics in real time.
