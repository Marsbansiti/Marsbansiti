# Git-Practice

## Step 1: Create a New Branch

```bash
git branch feature-add-color
```

## Step 2: Make `feature-add-color` the Active Branch

```bash
git checkout feature-add-color
```

## Step 3: Add a CSS Rule

In your CSS file, add the following rule:

```css
.red {
    background-color: red;
}
```

## Step 4: Stage the Change

```bash
git add -A
```

## Step 5: Commit the Change

```bash
git commit -m 'adding red color feature'
```

## Step 6: Merge `feature-add-color` into `main`

```bash
git checkout main
git merge feature-add-color
```

## Step 7: Delete the `feature-add-color` Branch

```bash
git branch -d feature-add-color
```

## Step 8: Push Changes to `origin`

```bash
git push origin main
```

## Step 9: Create a Pull Request

Use the GitHub UI to create a new pull request for this feature in the upstream repository.

---

## Summary

In this lab, you have learned how to fork an upstream repository into your own account and then clone it locally in the lab environment. You then learned how to synchronize changes in your local repository with remote GitHub repositories using pull requests.
