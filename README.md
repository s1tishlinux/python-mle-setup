# Python MLE Setup: Tools and Git Workflow

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
⸻
