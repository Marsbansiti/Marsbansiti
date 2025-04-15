# 🧪 Linux Terminal Exercises

---

## 📁 Exercise 1 - Browsing Directories (`ls`)

### 🔹 1.1 Viewing files in the current working directory
```bash
ls
```
Your default directory `/home/project` may be empty, so this command might return nothing.

---

### 🔹 1.2 Viewing files and directories within any directory
```bash
ls [PATH TO DIRECTORY]
ls /
```
This displays contents of the root directory `/`.

#### Common Subdirectories:
| Directory | Contains |
|-----------|----------|
| /bin      | System binaries |
| /sbin     | Admin binaries |
| /usr      | User programs |
| /home     | User home directories |
| /media    | Removable media |

```bash
ls /bin
```
Note: The `ls` command itself is located at `/bin/ls`.

---

## 📂 Exercise 2 - Navigating Directories (`cd`)

### 🔹 Navigation Symbols

| Symbol | Meaning |
|--------|---------|
| `~`    | Home directory |
| `/`    | Root directory |
| `.`    | Current directory |
| `..`   | Parent directory |

### 🔹 2.1 Change to your home directory
```bash
cd ~
```

### 🔹 2.2 Change to the parent directory
```bash
cd ..
```

### 🔹 2.3 Change to the root directory
```bash
cd /
```

### 🔹 2.4 Change to a child directory
```bash
cd bin
cd ./bin
```
Note: `.` refers to the current directory.

### 🔹 2.5 Change back to your home directory
```bash
cd ../home/theia
cd ~
```

### 🔹 2.6 Change to your project directory
```bash
cd ../project
```

---

## ⌨️ Exercise 3 - Tab Completion & Command History

### 🔹 3.1 Scrolling through your command history
Use `↑` and `↓` keys to navigate previously entered commands.

Repeat previous commands without retyping them.

### 🔹 3.2 Using Tab Completion
```bash
cd /bi  # Press Tab => cd /bin
cd /b   # Press Tab twice => bin/ boot/
```

Tab completion helps:
- Autocomplete paths
- Discover available files/directories

```bash
ls /home  # Press Tab twice
ls /home/theia  # Tab to autocomplete deeper
ls /home/theia/dsdriver/bin
```

---

## 🧠 Practice Exercises

### ✅ 1. List contents of the root directory
```bash
ls /
```

### ✅ 2. Change to home directory
```bash
cd ~
```

### ✅ 3. Verify current directory
```bash
pwd
```

### ✅ 4. Use tab completion to go to `/bin`
```bash
cd /b  # Press Tab twice, then type 'i' and Tab again
```

### ✅ 5. Use command history to return home
Use `↑` until you see:
```bash
cd ~
```

---

Future labs will explore more advanced command-line options. For now, you've built a solid foundation using `ls`, `cd`, command history, and tab completion in Linux!

