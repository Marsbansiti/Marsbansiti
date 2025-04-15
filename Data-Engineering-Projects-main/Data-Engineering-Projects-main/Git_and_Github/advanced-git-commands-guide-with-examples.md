
# 🧠 Advanced Git Commands Guide with Examples

Welcome! In this reading, you'll **summarize and describe additional Git commands** that you may use while working on your projects, along with the **syntax and examples** for each.

Git is a widely used version control system that offers numerous benefits to developers and teams working on software development projects.

---

## 📜 Git Commands with Descriptions, Syntax & Examples

### 🔹 `git add`
**Description:** Adds changes to the staging area.

**Syntax:**
```bash
git add <filename.txt>
git add .
git add -A
```

**Example:**
```bash
git add index.html          # Add a specific file
git add .                   # Add all files in the current directory
```

---

### 🔹 `git reset`
**Description:** Resets changes in the working directory.

**Syntax:**
```bash
git reset
git reset --hard HEAD
```

**Example:**
```bash
git reset --hard HEAD       # Discards all local changes
```

---

### 🔹 `git branch`
**Description:** Lists, creates, or deletes branches.

**Syntax:**
```bash
git branch
git branch <new-branch>
git branch -d <branch-name>
```

**Example:**
```bash
git branch feature-1        # Create a new branch
git branch                  # List all branches
git branch -d feature-1     # Delete branch
```

---

### 🔹 `git checkout main`
**Description:** Switches to the `main` branch.

**Syntax:**
```bash
git checkout main
```

**Example:**
```bash
git checkout main
```

---

### 🔹 `git clone`
**Description:** Copies a remote repository to your local machine.

**Syntax:**
```bash
git clone <repository-URL>
```

**Example:**
```bash
git clone https://github.com/user/project.git
```

---

### 🔹 `git pull`
**Description:** Fetches changes from a remote repository and merges into your branch.

**Syntax:**
```bash
git pull origin main
```

**Example:**
```bash
git checkout main
git pull origin main
```

---

### 🔹 `git push`
**Description:** Pushes local changes to a remote repository.

**Syntax:**
```bash
git push origin <branch-name>
```

**Example:**
```bash
git push origin feature-1
```

---

### 🔹 `git version`
**Description:** Displays current installed Git version.

**Syntax:**
```bash
git version
```

**Example:**
```bash
git version
# Output: git version 2.34.1
```

---

### 🔹 `git diff`
**Description:** Shows differences between files, commits, or branches.

**Syntax:**
```bash
git diff
git diff HEAD~1 HEAD
git diff <branch-1> <branch-2>
```

**Example:**
```bash
git diff                    # Show unstaged changes
git diff main feature-1     # Compare branches
```

---

### 🔹 `git revert`
**Description:** Reverts the last commit with a new commit.

**Syntax:**
```bash
git revert HEAD
```

**Example:**
```bash
git revert HEAD             # Undo last commit by creating a new one
```

---

### 🔹 `git config`
**Description:** Sets user configuration globally.

**Syntax:**
```bash
git config --global user.email "<Your GitHub Email>"
git config --global user.name "<Your GitHub Username>"
```

**Example:**
```bash
git config --global user.email "you@example.com"
git config --global user.name "YourName"
```

---

### 🔹 `git remote`
**Description:** Manage remote repositories.

**Syntax:**
```bash
git remote
git remote -v
git remote add origin <URL>
git remote rename origin upstream
git remote rm origin
```

**Example:**
```bash
git remote add origin https://github.com/user/project.git
git remote rename origin upstream
git remote -v
```

---

### 🔹 `git format-patch`
**Description:** Generates patches for email sharing.

**Syntax:**
```bash
git format-patch HEAD~3
```

**Example:**
```bash
git format-patch HEAD~2     # Create patches for last 2 commits
```

---

### 🔹 `git request-pull`
**Description:** Creates a summary of pending changes for email.

**Syntax:**
```bash
git request-pull origin/main <branch-name>
```

**Example:**
```bash
git request-pull origin/main feature-1
```

---

### 🔹 `git send-email`
**Description:** Sends patch files as emails.

**Syntax:**
```bash
git send-email *.patch
```

**Example:**
```bash
git send-email 0001-my-patch.patch
```

---

### 🔹 `git am`
**Description:** Applies patch files to the repo.

**Syntax:**
```bash
git am <patchfile.patch>
```

**Example:**
```bash
git am 0001-my-patch.patch
```

---

### 🔹 `git daemon`
**Description:** Exposes repositories using the Git:// protocol.

**Syntax:**
```bash
git daemon --base-path=/path/to/repositories
```

**Example:**
```bash
git daemon --base-path=/home/user/projects/
```

---

### 🔹 `git instaweb`
**Description:** Instantly launches a web interface to view your repo.

**Syntax:**
```bash
git instaweb --httpd=webrick
```

**Example:**
```bash
git instaweb --httpd=webrick
```

---

### 🔹 `git rerere`
**Description:** Reuses resolution of previously resolved merge conflicts.

**Syntax:**
```bash
git config --global rerere.enabled true
git rerere
```

**Example:**
```bash
git config --global rerere.enabled true
git rerere
```

---

## ✅ Conclusion

Git is an incredibly powerful tool for managing your code and collaborating with others. As you work more with Git, many of these commands will become part of your daily workflow.

Happy coding! 🚀
