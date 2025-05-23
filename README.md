# promptfile

A simple Python CLI tool to recursively print the contents of files in a directory, skipping files and directories that match configurable ignore patterns.

---

## 🧰 Features

* **Recursively walks through a directory**
* **Skips ignored files and folders** using glob patterns
* **Prints file paths and their contents**
* **Ignores common folders** like `node_modules`, `build`, `dist`, and dotfiles

---

## ⚙️ Installation (for development)

This setup uses **pipx** to globally install the tool in an isolated environment, similar to `npm install -g`.

### 1. Install pipx

If you don’t already have pipx:

```bash
brew install pipx
pipx ensurepath
```

Then **restart your terminal** or **source your shell profile**:

`source ~/.zprofile`  # or `~/.bash_profile` / `~/.zshrc` depending on your shell

### 2. Project structure

Your project should look like this:

```
promptfile/
├── setup.py
└── promptfile/
    ├── __init__.py
    └── __main__.py
```

### 3. Global install via pipx

From the project root:

```bash
pipx install --editable .
```

✅ This makes the `promptfile` command available globally from anywhere.

---

## 🚀 Usage

```bash
promptfile .
promptfile ./src
promptfile ../some-folder
```

The CLI prints file paths and their contents, skipping ignored files and directories as defined in `IGNORE_PATTERNS`.

---

## 🛠 Development Workflow

* Modify any code under the `promptfile/` package
* **No need to reinstall** — pipx in `--editable` mode uses your live source code

---

## 🔄 Reinstall / Refresh

If you need to reinstall (e.g., after renaming or structure changes):

```bash
pipx uninstall promptfile
pipx install --editable .
```

---

## ❌ Uninstall

```bash
pipx uninstall promptfile
```

This removes the global `promptfile` command and its virtual environment.

---

## 📌 Notes

* **Works with both relative and absolute paths**
* Uses `os.path.abspath()` under the hood
* Python 3.8+ recommended
* Customize the `IGNORE_PATTERNS` list in `__main__.py` as needed

---

## 🧪 Example

```bash
promptfile my_project
```

Prints all non-ignored files under `my_project`, showing both the path and the file content.