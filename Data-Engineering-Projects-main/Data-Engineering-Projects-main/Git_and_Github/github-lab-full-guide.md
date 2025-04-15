# GitHub Lab Exercise: Full Workflow Guide

---

## 🔐 Step 1: Generate a Personal Access Token (PAT)

1. Go to [GitHub.com](https://github.com) and log in.
2. Follow the lab instructions under **"Generate GitHub personal access token"**.
3. Copy the generated token. This will be used in place of a password in future steps.

---

## 🍴 Step 2: Fork the Repository

1. Navigate to the source (upstream) repository.
2. Click **Fork** and choose your GitHub account.
3. The forked repository is now your **origin**.

---

## 📥 Step 3: Clone the Forked Repository

1. Open your forked repository on GitHub.
2. Click the **Code** button and copy the **HTTPS URL**.
3. In your terminal, run:

```bash
export ORIGIN=<your repository HTTPS URL>
git clone $ORIGIN
```

---

## 🔍 Step 4: Explore the Cloned Repository

- Use the file explorer to navigate through the project files.
- Open and inspect files like `style.css`.

---

## 🌿 Step 5: Create the `feature-circle-500` Branch

```bash
cd gkpbt-css-circle
git checkout -b feature-circle-500
git branch
```

---

## 🎨 Step 6: Make Code Changes

Edit `style.css` to update the circle's size to 500x500 pixels.

Check the changes:

```bash
git status
git diff ./style.css
```

---

## 💾 Step 7: Add and Commit Your Changes

```bash
git add .
git config --global user.email "email@example.com"
git config --global user.name "Your Name"
git commit -m "Changing the height and the width of the circle"
```

---

## 🔀 Step 8: Merge `feature-circle-500` into `main`

```bash
git checkout main
git merge feature-circle-500
git log --oneline
```

Press `q` to exit the git log view.

---

## 🧹 Step 9: Delete the Branch

```bash
git branch -d feature-circle-500
git branch
```

---

## 🚀 Step 10: Push Changes to GitHub

```bash
git push origin main
```

> You may be asked to enter your GitHub username and **PAT** as your password.

---

## 📬 Step 11: Create a Pull Request

1. Go to your forked repository.
2. Click **Contribute > Open pull request**.
3. Confirm the comparison between your `main` and upstream's `main`.
4. Click **Create pull request**.
5. Confirm your commit message is used as the PR title.
6. Click **Create pull request** again.

> Your pull request may be auto-processed and closed by lab automation.

---

## ✅ Final Notes

- This guide walked you through the full GitHub collaboration flow:
  - Forking
  - Cloning
  - Branching
  - Committing
  - Merging
  - Pushing
  - Pull Requests

Great job!
