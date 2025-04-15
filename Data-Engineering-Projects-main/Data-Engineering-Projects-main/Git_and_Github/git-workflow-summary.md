# Summary: Git Workflows with Git Commands

---

## 📚 What You Learned

- GitHub hosts over 100 million repositories.
- You can **clone** a repository and sync changes, or **fork** it to create your own version.
- GitHub workflows include a sequence of common Git operations used to collaborate effectively on projects.

---

## 🔁 GitHub Workflow Steps

1. **Clone** the remote repository or **initialize** a new Git repository.
2. Move files to the **staging area**.
3. Perform an **initial commit**.
4. **Create a branch** and work on new changes.
5. Add files to the staging area and **commit** them.
6. **Push** local commits to the remote repository.
7. **Create a pull request** for review and merging.
8. Use **pull** operation to sync updates from remote to local.

---

## 👥 Git Roles

### Developer
- Uses:  
  `git clone`, `git pull`, `git fetch`, `git push`, `git request-pull`

### Integrator
- Responsibilities:
  - Reviews and merges changes
- Uses:  
  `git pull`, `git revert`, `git push`

### Repository Administrator
- Responsibilities:
  - Manages repo structure and settings
  - Sets up web services and documentation
  - Defines user roles and visual settings

---

## 🛠️ Common Git Commands

| Command | Description |
|--------|-------------|
| `git init` | Initialize a new Git repository |
| `git checkout` | Switch branches or restore files |
| `git revert` | Revert a commit |
| `git-format-patch` | Create patch files |
| `git fetch upstream` | Fetch changes from upstream repo |
| `git status` | Show working directory status |
| `git merge` | Merge branches |
| `git config --global user.email` | Set global email config |
| `git-request-pull` | Generate a summary of changes for pull request |
| `git merge upstream/main` | Merge upstream changes into local main |
| `git add .` | Stage all changes in current directory |
| `git clone` | Clone a remote repo |
| `git config --global user.name` | Set global username |
| `git-send-email` | Send patches via email |
| `git pull upstream` | Pull from upstream repository |
| `git commit` | Record changes to the repo |
| `git pull` | Fetch and merge from remote |
| `git remote -v` | Show remote URLs |
| `git-am` | Apply a series of patches from a mailbox |
| `git web` | (Custom command) |
| `git log` | Show commit logs |
| `git push` | Push changes to remote repo |
| `git remote rename` | Rename a remote |
| `git-daemon` | Serve repositories over the Git protocol |
| `git-instaweb` | Instantly browse your project in Git |
| `git reset` | Reset current HEAD |
| `git version` | Show Git version |
| `git remote add origin` | Add a new remote repository |
| `git-pull downstream` | (Custom or alias command) |
| `git branch` | Manage branches |
| `git diff` | Show changes between commits |
| `git-remote` | Manage remote repositories |
| `git remote add upstream` | Link to the original repo (upstream) |
| `git-rerere` | Reuse recorded resolution of conflicts |

---

## ✅ Conclusion

This module gives you a practical understanding of how different Git commands and roles come together in real-world collaborative projects.

