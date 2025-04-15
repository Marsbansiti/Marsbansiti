# 📁 Browsing Directories with the Linux Terminal

## 🧠 Learning Objectives

By the end of this tutorial, you will be able to:

- ✅ Describe what a Linux terminal is used for  
- ✅ Use the `pwd` and `ls` commands to browse directories in your Linux file system  

---

## 🖥️ The Linux Terminal

The **Linux terminal** (also called the **command line** or **command prompt**) is a user interface that allows you to interact with the **Linux shell** by typing commands.

When you open a terminal window, you'll see a line like this:

```
/home/project $
```

- The **blue text** (`/home/project`) shows your **current directory** (called the _present working directory_).
- The **dollar sign** (`$`) is the command prompt, waiting for your input.

You can type commands and press `Enter` to run them. Many commands will respond with output displayed right in the terminal.

---

## 🔍 Navigating Directories

### 📍 `pwd` – Print Working Directory

Use the `pwd` command to display your current directory:

```bash
pwd
```

**Example output:**

```
/home/project
```

This tells you where you are in the file system.

---

### 📂 `ls` – List Directory Contents

Use the `ls` command to view files and folders inside your current directory:

```bash
ls
```

If the directory is empty, `ls` returns nothing — no output, not even a blank line.

To list contents of another directory, add the path:

```bash
ls /home
```

**Example output:**

```
project  theia
```

These are two subdirectories inside `/home`.

---

## 🧭 Understanding Directory Paths

- `/home/project` → `project` is a subdirectory of `/home`.
- `/home/theia` → `theia` is another subdirectory of `/home`.

Your Linux file system starts at the **root directory**: `/` (slash), and branches out like a tree.

To explore it:

```bash
ls /
```

This shows top-level directories like `home`, `bin`, `etc`, etc.

---

## ✅ Summary

- 🖱️ The terminal lets you interact with the Linux shell by typing commands.
- 📌 `pwd` shows your current location in the file system.
- 📁 `ls` lists the contents of a directory.

---
