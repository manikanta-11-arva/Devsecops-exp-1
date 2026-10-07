# DevSecMLOps Lab Experiments

## Experiment 1: Setting up Git, GitHub and Python Environment

### Step 1: Check Git installation
```bash
git --version
```

### Step 2: Configure Git identity
```bash
git config --global user.name "ML Student"
git config --global user.email "student@woxsen.edu.in"
```

### Step 3: Create project folder
```bash
mkdir ml-project
cd ml-project
```

### Step 4: Initialize Git
```bash
git init
```

### Step 5: Create Python virtual environment
```bash
python -m venv venv
```

On macOS/Linux, activate it with:
```bash
source venv/bin/activate
```

On Windows PowerShell:
```powershell
venv\Scripts\Activate.ps1
```

If PowerShell blocks activation, run:
```powershell
Set-ExecutionPolicy -Scope CurrentUser RemoteSigned
```

Then activate again:
```powershell
venv\Scripts\Activate.ps1
```

### Step 6: Create requirements.txt
```txt
pandas
scikit-learn
mlflow
joblib
```

### Step 7: Install requirements
```bash
pip install -r requirements.txt
```

### Step 8: Create .gitignore
```txt
venv/
__pycache__/
*.pyc
data/
mlruns/
```

### Step 9: Create hello_ml.py
```python
import sys
import sklearn
import pandas as pd

def check_environment():
    print("Python executable :", sys.executable)
    print("Python version :", sys.version.split()[0])
    print("scikit-learn :", sklearn.__version__)
    print("pandas :", pd.__version__)
    print("ML environment is ready!")

if __name__ == "__main__":
    check_environment()
```

### Step 10: Run the script
```bash
python hello_ml.py
```

Expected output:
```text
Python executable : ...
Python version : ...
scikit-learn : ...
pandas : ...
ML environment is ready!
```

### Step 11: Check Git status
```bash
git status
```

### Step 12: Stage the files
```bash
git add requirements.txt .gitignore hello_ml.py
```

### Step 13: Commit
```bash
git commit -m "Initial commit: project setup and environment check"
```

### Step 14: Show commit log
```bash
git log --oneline
```

### Step 15: Optional GitHub push
If the repo exists:
```bash
git remote add origin https://github.com/<USERNAME>/ml-project.git
git branch -M main
git push -u origin main
```

If no GitHub repo exists yet:
1. Create a new repository on GitHub.
2. Copy the URL.
3. Run:
```bash
git remote add origin <your_repo_url>
git branch -M main
git push -u origin main
```

---

## Experiment 2: Version Control for ML Projects

### Step 1: Check current branch
```bash
git branch
```

### Step 2: Create feature branch
```bash
git checkout -b feature/train-model
```

### Step 3: Create train.py
```python
from sklearn.datasets import load_iris
from sklearn.tree import DecisionTreeClassifier
from sklearn.model_selection import train_test_split
from sklearn.metrics import accuracy_score, precision_score, recall_score


def main():
    # Load the Iris dataset
    X, y = load_iris(return_X_y=True)

    # Split the dataset into training and testing data
    X_train, X_test, y_train, y_test = train_test_split(
        X,
        y,
        test_size=0.2,
        random_state=42,
        stratify=y
    )

    # Create and train the Decision Tree model
    model = DecisionTreeClassifier(
        max_depth=3,
        random_state=42
    )

    model.fit(X_train, y_train)

    # Make predictions
    y_pred = model.predict(X_test)

    # Calculate metrics
    acc = accuracy_score(y_test, y_pred)
    prec = precision_score(y_test, y_pred, average="macro")
    rec = recall_score(y_test, y_pred, average="macro")

    print(f"Accuracy : {acc:.2f}")
    print(f"Precision: {prec:.2f}")
    print(f"Recall   : {rec:.2f}")


if __name__ == "__main__":
    main()
```

### Step 4: Run the model
```bash
python train.py
```

Expected output:
```text
Accuracy : 0.97
Precision: 0.97
Recall   : 0.97
```

### Step 5: Check Git status
```bash
git status
```

### Step 6: Stage train.py
```bash
git add train.py
```

### Step 7: Commit the experiment
```bash
git commit -m "Add decision tree training script"
```

### Step 8: Switch back to main/master
Check actual branch name:
```bash
git branch
```

If repo uses main:
```bash
git checkout main
```

If repo uses master:
```bash
git checkout master
```

### Step 9: Merge the feature branch
```bash
git merge feature/train-model
```

### Step 10: Display Git history
```bash
git log --oneline --graph --all
```

### Step 11: Display branches
```bash
git branch
```

### Final verification
```bash
python train.py
git status
git log --oneline --graph --all
```

---

## Viva Questions and Answers

### Experiment 1
1. Why use a virtual environment for an ML project?
   - It keeps dependencies isolated and prevents conflicts.

2. What is the difference between Git and GitHub?
   - Git is local version control; GitHub is an online hosting service.

3. What is the purpose of .gitignore?
   - It prevents unnecessary files from being tracked in Git.

4. What does git commit store?
   - It stores a snapshot of the project changes.

### Experiment 2
1. Why create a branch for each experiment?
   - It keeps experiments independent and avoids affecting the main code.

2. What is a fast-forward merge?
   - It happens when the main branch has no new commits and the feature branch can simply move ahead.

3. How do you view branch history graphically?
   - Use `git log --oneline --graph --all`.

4. What is a merge conflict?
   - It occurs when two branches modify the same code in different ways and Git cannot merge automatically.
