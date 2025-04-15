# 🖥️ Linux Terminal Tips - Tab Completion & Command History

## 🧠 Learning Objectives

After completing this reading, you will be able to:

- ✅ Use tab completion to autocomplete commands  
- ✅ Use command history to quickly navigate previous commands  

---

## 🔡 Tab Completion

Many shells support a feature called **tab completion**, which allows you to autocomplete a command you’re typing on the command line.

### Example Scenario:

Suppose you're in your home directory `~`, which contains:

- `Pictures`
- `Videos`
- `Documents`
- `Downloads`

And your `Documents` folder contains:

- `python-examples`

### 👉 Using Tab Completion

To navigate to the **Pictures** directory:

```bash
~ $ cd P  # Press Tab
```

The shell autocompletes to:

```bash
~ $ cd Pictures/
```

### 🔗 Tab Completion for Longer Paths

If you type:

```bash
~ $ cd Do  # Press Tab
```

Nothing happens because there’s more than one match: `Documents` and `Downloads`.

But if you type:

```bash
~ $ cd Doc  # Press Tab
```

It autocompletes to:

```bash
~ $ cd Documents/
```

Press Tab again, and it completes further:

```bash
~ $ cd Documents/python-examples/
```

---

## ⌨️ Command History

You can use the **Up Arrow** and **Down Arrow** keys to navigate through previous commands.

### Example:

Let’s say you ran the following:

```bash
~ $ cd ~/Documents/python-examples
~/Documents/python-examples $ python3 myprogram.py
Hello, World!
~/Documents/python-examples $ cd /
/ $
```

### 🔁 Rerunning the Last Command

Press the Up Arrow once:

```bash
/ $ cd /
```

### 🔙 Running a Previous Command from the Session

Press the Up Arrow three times:

```bash
/ $ cd ~/Documents/python-examples
```

Note: Output like `Hello, World!` is not part of the command history — only your typed commands are.

### 💡 Tip:

Pressed the Up Arrow too much? Use the **Down Arrow** to go forward again in history.

---

## ✅ Summary

You now know how to use handy shortcuts to improve your terminal productivity:

- 🔄 Use **Tab Completion** to autocomplete paths and commands  
- ⬆️⬇️ Use **Command History** with arrow keys to rerun previous commands  

---
