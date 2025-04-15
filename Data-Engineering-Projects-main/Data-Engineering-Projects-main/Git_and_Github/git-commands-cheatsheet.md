# Git Commands and Managing GitHub Projects

## 🧭 Getting Started with Git and GitHub

### Module 2 Cheat Sheet: Git Commands and Managing GitHub Projects

| Command | Description | Code Example |
|---------|-------------|--------------|
| `git add` | Moves changes to the staging area | `git add sample.md` |
| `git add .` | Stages all changed files | `git add .` |
| `git am` | Applies patches emailed to the repo | `git am < patchfile.patch` |
| `git branch` | Creates an isolated environment | `git branch <new-branch>` |
| `git checkout` | Switches between branches | `git checkout <existing-branch>` |
| `git checkout main` | Switches to main branch | `git checkout main` |
| `git clone` | Clones a remote repo | `git clone <repository-url>` |
| `git commit` | Commits staged changes | `git commit -m "Your commit message here"` |
| `git config --global user.email` | Sets global email config | `git config --global user.email "your.email@example.com"` |
| `git config --global user.name` | Sets global username config | `git config --global user.name "Your Name"` |
| `git daemon` | Enables anonymous download | `git daemon --reuseaddr --verbose` |
| `git diff` | Shows changes between versions | `git diff example.txt` |
| `git fetch` | Transfers changes from remote to local | `git fetch <options> <remote> <branch>` |
| `git fetch upstream/master` | Grabs upstream branches | `git fetch upstream master:upstream-master` |
| `git format-patch` | Prepares email submission | `git format-patch -n <number_of_commits>` |
| `git http-backend` | Server-side Git-over-HTTP | `git clone --bare /path/to/repos/myrepo.git`<br>`cd myrepo.git`<br>`git update-server-info` |
| `git init` | Initializes a new repository | `git init <directory>` |
| `git instaweb` | Sets up web front-end | `git instaweb -p 8080` |
| `git log` | Shows project history | `git log -p filename` |
| `git merge` | Merges branches | `git merge feature_branch` |
| `git merge upstream/master` | Merges upstream changes | `git merge upstream/master` |
| `git pull` | Fetches and merges from remote | `git pull origin main` |
| `git pull downstream` | Pulls from downstream repo | `git pull downstream main` |
| `git pull upstream` | Pulls from upstream repo | `git pull upstream main` |
| `git push` | Pushes commits to remote | `git push origin your_branch_name` |
| `git remote` | Manages remote repositories | `git remote add upstream https://github.com/original/repo.git` |
| `git remote add origin` | Adds origin remote | `git remote add origin https://github.com/yourusername/your-repo.git` |
| `git remote add upstream` | Adds upstream remote | `git remote add upstream https://github.com/original/repo.git` |
| `git remote rename` | Renames a remote | `git remote rename origin new-origin` |
| `git remote -v` | Lists remotes | `git remote -v` |
| `git request-pull` | Summarizes changes for pull | `git request-pull origin/main your-branch`<br>`git request-pull <base> <head> <repository>` |
| `git rerere` | Reuses resolved conflicts | `git rerere`<br>`git rerere diff` |
| `git reset` | Undoes local changes | `git reset HEAD~1` |
| `git revert` | Undoes commits | `git revert HEAD` |
| `git send-email` | Sends patches via email | `git send-email --to=recipient@example.com path/to/patchfile.patch`<br>`git send-email --to recipient@example.com patches/*.patch` |
| `git shell` | Restricted shell for shared repo | `sudo usermod -s /usr/bin/git-shell gituser` |
| `git status` | Shows current status | `git status` |
| `git version` | Displays Git version | `git --version` |
| `git web` | Web front-end to Git | `git instaweb --port=8080` |

---

📘 Use this cheat sheet as a quick reference while working with Git and GitHub projects.

