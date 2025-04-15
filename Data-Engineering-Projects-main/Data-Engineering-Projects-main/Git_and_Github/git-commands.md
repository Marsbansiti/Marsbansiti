
# 🌟 Git Commands Overview

Welcome to the **Overview of Git Commands**! 🚀

In this guide, you'll examine some basic Git commands and their functions and applications. Git commands are used for various purposes such as **tracking and saving changes**, and **sharing your changes with others**.

While many of these activities can be done through a **web interface**, using the **Command-Line Interface (CLI)** gives you more control and power. Let’s walk through an example scenario together. 🌈

---

## 📁 Scenario: Adding a New HTML File

Imagine you're a web developer who wants to add a new HTML file to enhance the features of a web application — but you also want to experiment **without disturbing the main code**.

---

## 🧰 CLI & Git Commands Used

| Command | Purpose |
|--------|---------|
| `mkdir` | Create a new directory |
| `cd` | Navigate to a directory |
| `git init` | Initialize a Git repository |
| `git add` | Stage changes |
| `git commit -m` | Commit staged changes |
| `git log` | View commit history |
| `git branch` | Create/manage branches |
| `git checkout` | Switch branches |
| `git merge` | Merge branches |
| `git status` | View current status |

---

## 🔨 Step-by-Step Walkthrough

### 1. Create and Enter a New Directory

```bash
mkdir MyRepository
cd MyRepository
```

- `mkdir`: Creates a new directory.
- `cd`: Changes the current directory to the one specified.

---

### 2. Initialize a Git Repository

```bash
git init
```

- `git init`: Sets up the necessary Git configuration to begin tracking changes.

---

### 3. Create a New HTML File

```bash
echo "<h1>Welcome</h1>" > index.html
```

---

### 4. Add File to Staging Area

```bash
git add index.html
```

- `git add`: Moves the file from the working directory to the staging area.

---

### 5. Commit the File

```bash
git commit -m "Created a new HTML file"
```

- `git commit -m`: Records the change with a descriptive message.

---

### 6. View Commit History

```bash
git log
```

- `git log`: Displays a list of all commits made to the repository.

---

### 7. Create a Branch

```bash
git branch code_list
```

- `git branch`: Creates a new branch. Here, it's named `code_list`.

---

### 8. Switch to the New Branch

```bash
git checkout code_list
```

- `git checkout`: Switches to the specified branch.

---

### 9. Edit the HTML File

```bash
echo "<p>This is new content</p>" >> index.html
```

---

### 10. Stage and Commit the Change

```bash
git add index.html
git commit -m "Updated index.html file in branch"
```

---

### 11. View the New Commit in Branch

```bash
git log
```

---

### 12. Check the Status of Files

```bash
git status
```

- `git status`: Shows current changes that are staged, unstaged, or untracked.

---

### 13. Merge Branch with Main

```bash
git checkout main
git merge code_list
```

- `git merge`: Combines changes from the branch into the main branch.

---

## ✅ Summary

You learned how to:

- Create and manage Git repositories
- Track changes using `git add` and `git commit`
- View history with `git log`
- Use branches for experimentation
- Merge changes back into the main code

---

> 🔁 Always remember to test in a branch and merge after verification!  
> 🧠 Use meaningful commit messages to keep track of your work history.


