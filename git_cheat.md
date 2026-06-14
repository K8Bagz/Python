# Git Cheat Sheet

cd my-project

git status

git branch

git pull

git fetch

git log --oneline

git diff

git add .

git add filename.py

git commit -m "Describe your changes"

git push

git switch main

git switch feature-name

git switch -c feature-name

git branch

git branch -r

git remote -v

git stash

git stash pop

git restore filename.py

git restore --staged filename.py

## Setup

```bash
# Set username and email
git config --global user.name "Your Name"
git config --global user.email "you@example.com"

# View configuration
git config --list
```

---

## Create & Clone Repositories

```bash
# Initialize a new repository
git init

# Clone an existing repository
git clone <repository-url>

# Clone into a specific folder
git clone <repository-url> <folder-name>
```

---

## Check Status & History

```bash
# Check repository status
git status

# View commit history
git log

# Compact history
git log --oneline

# Show changes
git diff

# Show staged changes
git diff --staged
```

---

## Staging & Committing

```bash
# Stage a file
git add file.txt

# Stage all changes
git add .

# Commit staged changes
git commit -m "Commit message"

# Stage and commit tracked files
git commit -am "Commit message"
```

---

## Branching

```bash
# List branches
git branch

# Create a branch
git branch feature-branch

# Switch branch
git checkout feature-branch

# Create and switch
git checkout -b feature-branch

# Modern switch command
git switch feature-branch

# Create and switch (modern)
git switch -c feature-branch

# Delete branch
git branch -d feature-branch
```

---

## Merging

```bash
# Merge branch into current branch
git merge feature-branch

# Abort a merge
git merge --abort
```

---

## Remote Repositories

```bash
# Show remotes
git remote -v

# Add remote
git remote add origin <repository-url>

# Push branch
git push origin main

# Push and set upstream
git push -u origin main

# Fetch changes
git fetch

# Pull changes
git pull
```

---

## Undo Changes

```bash
# Unstage a file
git restore --staged file.txt

# Discard working directory changes
git restore file.txt

# Undo last commit (keep changes)
git reset --soft HEAD~1

# Undo last commit (discard changes)
git reset --hard HEAD~1

# Revert a commit safely
git revert <commit-hash>
```

---

## Stashing

```bash
# Save current changes
git stash

# List stashes
git stash list

# Restore latest stash
git stash pop

# Restore without removing stash
git stash apply
```

---

## Tags

```bash
# Create tag
git tag v1.0.0

# List tags
git tag

# Push tag
git push origin v1.0.0

# Push all tags
git push --tags
```

---

## Common Workflow

```bash
git clone <repo>
git checkout -b feature-x
# Make changes
git add .
git commit -m "Add feature X"
git push -u origin feature-x
```

---

## Useful Shortcuts

| Task             | Command                           |
| ---------------- | --------------------------------- |
| Status           | `git status`                      |
| Stage all        | `git add .`                       |
| Commit           | `git commit -m "msg"`             |
| Pull             | `git pull`                        |
| Push             | `git push`                        |
| New branch       | `git switch -c branch-name`       |
| Switch branch    | `git switch branch-name`          |
| Merge branch     | `git merge branch-name`           |
| View history     | `git log --oneline --graph --all` |
| Undo last commit | `git reset --soft HEAD~1`         |
