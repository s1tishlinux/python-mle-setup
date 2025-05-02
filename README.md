# Assignment 1.3: Setting Up Python Development Environment in VS Code - Tools and Git Workflow

This repository demonstrates the setup of essential Python tools (`pylint`, `flake8`, `black`, and `isort`) for Machine Learning Engineering (MLE) development along with best practices for Git workflows. The goal is to prepare for MLE (Machine Learning Engineer) tasks by using modern development standards.

## Tools Included
- **isort**: 
- **flake8**: A linting tool for enforcing style guide compliance.
- **black**: An automatic code formatter that ensures consistent Python code.
- **pylint**: A tool for identifying programming errors, enforcing a coding standard, and offering suggestions for improvement.
---

## Prerequisites

### 1. Install Git
```bash

git init  #initialize git
git --version

```
If Git is missing:
- Linux: `sudo apt install git`
- macOS: `brew install git`
- Windows: Install Git Bash.

---

### 2. Configure Git
```bash
git config --global user.name "Your Name"
git config --global user.email "your.email@example.com"
```

---

### 3. Generate SSH Key Pair
```bash
ssh-keygen -t ed25519 -C "your.email@example.com"
```
- Press Enter to accept the default file location.
- Copy your SSH public key:
  ```bash
  cat ~/.ssh/id_ed25519.pub
  ```
- Add the key to GitHub:
  - GitHub → Settings → SSH and GPG keys → New SSH key → Paste and save.

---

### 4. Test SSH Connection
```bash
ssh -T git@github.com
```
Expected output:
```
Hi yourname! You've successfully authenticated...
```

---

## Repository Setup Steps

### 1. Create New Repository on GitHub
- Repository name: `python-mle-setup`
- Copy the SSH clone URL.

---

### 2. Clone Repository Locally
```bash
cd ~/your-workspace-folder/
git clone git@github.com:yourname/python-mle-setup.git
cd python-mle-setup
```

---

### 3. Create a New Branch
```bash
git checkout -b setup/python-tools
```

---

### 4. Set Up Python Tools
```bash
python3 -m venv venv
source venv/bin/activate    # Windows: venv\Scripts\activate
pip install pylint flake8 black isort
pip freeze > requirements.txt
```
### 4. Set Up Python Tools using Conda
```bash
conda create -n mle-env python=3.10 -y
conda activate mle-env
pip install pylint flake8 black isort
pip freeze > requirements.txt
```
---

### 5. Git Commit and Tag
```bash
git add .
git commit -m "Initial setup: added Python formatting and linting tools"
git tag v0.1-setup
```

---

### 6. Push to GitHub
```bash
git push origin setup/python-tools
git push origin v0.1-setup
```

---

## Final Folder Structure
```
python-mle-setup/
│
├── venv/                  # virtual environment
├── requirements.txt       # tools and dependencies
└── README.md              # this file
```

---

## Additional Practice (Optional)
- Create `.flake8` file to configure linting rules.
- Create a simple `hello.py` file and test formatting using `black` and `flake8`.

---

**Tags:** `v0.1-setup`  
**Branch:** `setup/python-tools`



### 7. Code Style Checks
 
-- **Flake8**:

flake8 is used to enforce PEP 8 compliance and other coding conventions.

Run flake8 to check your code for style violations:
```bash
flake8 bad_code.py
```
To configure flake8, you can modify the .flake8 file.

- **Black**:

black is used to format your code automatically. To apply black formatting:
```bash
black bad_code.py
```
To configure black, you can modify the pyproject.toml file.

-- **Pylint**:

pylint is a static code analysis tool that helps identify potential errors in your code. To run pylint, execute:

```bash
pylint bad_code.py
```
The configuration for pylint is managed through the .pylintrc file.

### 7. Committing and Pushing Changes

To commit your changes:
```bash
git add .
git commit -m "Your commit message"
```

### 8. To push your changes to the repository:
```bash
git push origin setup/python-tools

```
### 9. Reference documentation
https://black.readthedocs.io/en/stable/guides/using_black_with_other_tools.html


A⸻

# Assignment 1.4: Setting Up Python Development Environment in VS Code

This assignment helps learners set up a Python development environment using **Visual Studio Code**. It includes setting up user-level and workspace-level configurations for formatting, linting, and import sorting tools like **black**, **flake8**, and **isort**.

## 📁 Folder Structure

```
my-python-project/
├── .venv/                # Virtual environment
├── .vscode/
│   └── settings.json     # Workspace-level VS Code settings
├── .gitignore
├── README.md             # This file
├── test_code.py          # Sample code file for formatting test
└── requirements.txt
```

---

## ✅ Prerequisites

* Python 3.7 or later installed on your machine
* Visual Studio Code installed
* VS Code Python Extension installed

---

## 🧱 Step-by-Step Instructions

### 1. Create and Activate a Virtual Environment

```bash
# Create a folder for your project
mkdir my-python-project
cd my-python-project

# Create virtual environment (adjust for Windows)
python -m venv .venv

# Activate virtual environment
# Windows:
.venv\Scripts\activate
# macOS/Linux:
source .venv/bin/activate
```

### 2. Install Required Python Tools

```bash
pip install black isort flake8

# Optionally freeze dependencies
pip freeze > requirements.txt
```

---

### 3. Configure Workspace-Level Settings in VS Code

Create a `.vscode/settings.json` file:

```json
{
  "python.pythonPath": ".venv/bin/python",  // or ".venv\\Scripts\\python.exe" on Windows
  "editor.formatOnSave": true,
  "editor.codeActionsOnSave": {
    "source.organizeImports": true
  },
  "python.formatting.provider": "black",
  "python.linting.enabled": true,
  "python.linting.flake8Enabled": true,
  "python.sortImports.args": ["--profile", "black"],
  "editor.tabSize": 4,
  "files.trimTrailingWhitespace": true
}
```

### 4. (Optional) User-Level Settings

VS Code > `Ctrl + Shift + P` > Preferences: Open User Settings (JSON)

```json
{
  "editor.tabSize": 4,
  "editor.formatOnSave": true,
  "files.trimTrailingWhitespace": true
}
```

These are global settings for all VS Code projects.

---

## ⚙️ Custom Tool Configurations
📂 Optional Configuration Files (Advanced)

For portability outside VS Code (e.g., CI/CD, team sharing):

### `.flake8`

```ini
[flake8]
max-line-length = 88
```

### `pyproject.toml` for `black` and `isort`

```toml
[tool.black]
line-length = 88

[tool.isort]
profile = "black"
```

---

## 🧪 Testing the Setup

### 1. Sample `test_code.py` before formatting

```python
import os,sys

def sample_function():    print(   "Hello World")
```

### 2. On Save: After `black`, `isort`, and `flake8`

```python
import os
import sys

def sample_function():
    print("Hello World")
```

You should see formatted code, sorted imports, and linting messages (if any).

---

## 🔍 How to Verify Everything is Working

1. Open the folder in VS Code.
2. Make changes to Python file and save.
3. Check if:

   * Imports are sorted
   * Formatting is applied
   * No trailing whitespaces
   * Linting errors (e.g. from `flake8`) are shown in the Problems tab

---

## 📌 Notes on User vs Workspace Settings

| Feature         | User-Level Setting                  | Workspace Setting               |
| --------------- | ----------------------------------- | ------------------------------- |
| Scope           | Applies to all projects             | Applies only to current project |
| Location        | Global User Settings (JSON)         | `.vscode/settings.json`         |
| Recommended For | Common defaults across all projects | Project-specific configurations |

🌍 User Settings vs Workspace Settings

Feature	User Settings 		(Ctrl + , → User)		Workspace Settings (.vscode/settings.json)
Affects all projects			✅			❌
Affects only this project		❌			✅
Good for global defaults		✅			❌
Good for per-project config		❌			✅

Use **workspace settings** when:

* Your team/project has specific coding standards
* You want consistent behavior across machines

Use **user settings** for personal preferences like font size, default format on save, etc.

💡 Tip: Prefer workspace settings for tool-specific settings like flake8, black, and pythonPath.

---

## 🎯 Summary

* Created a virtual environment
* Installed `black`, `flake8`, and `isort`
* Configured workspace settings
* Differentiated between user and workspace settings
* Verified formatting and linting works as expected

✅ You're now ready to start writing clean, consistent Python code in VS Code!
---
⸻
