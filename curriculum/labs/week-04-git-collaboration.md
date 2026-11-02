# Week 4 Lab: Git and collaborative engineering

[← Practical labs](README.md) · [← Week 4 guide](../weeks/week-04.md)

## Mission
Create a repository, make meaningful commits, branch, push and open a pull request. Practise a review cycle without pushing directly to the shared default branch.

**Time:** 60–90 minutes · **Cost:** Free · **Prerequisites:** Git and a GitHub account

## Part A — Verify and configure Git

```bash
git --version
git config --global user.name
git config --global user.email
```

If values are missing, configure the name and an email address you are comfortable associating with commits:

```bash
git config --global user.name "Your Name"
git config --global user.email "your-verified-github-email@example.com"
```

Do not paste passwords or tokens into Git configuration.

## Part B — Create a local repository

```bash
mkdir -p ~/cloud-track/week-04-collaboration
cd ~/cloud-track/week-04-collaboration
git init
printf '# Week 4 Git Lab\n\nLearning Git collaboration.\n' > README.md
mkdir notes
printf 'A commit records a snapshot of tracked changes.\n' > notes/git-basics.md
git status
git add README.md notes/git-basics.md
git status
git commit -m "docs: add initial Git learning notes"
git log --oneline
```

Expected: one commit on your current branch. Git may name the initial branch `master` or `main`, depending on configuration.

## Part C — Create a feature branch

```bash
git switch -c docs/add-workflow-notes
printf '\n## Safe workflow\n\nWork on a branch and open a pull request.\n' >> README.md
git diff
git status
git add README.md
git commit -m "docs: explain the pull request workflow"
git log --oneline --decorate -3
```

Explain the difference between the working tree, staging area and commit history.

## Part D — Publish to GitHub

1. Create an empty repository on GitHub named `cloud-track-git-lab`.
2. Do not initialize it with a README, licence or gitignore because you already have local history.
3. Follow GitHub's instructions to add the remote. The commands will look like:

```bash
git remote add origin https://github.com/YOUR-USERNAME/cloud-track-git-lab.git
git remote -v
git push -u origin docs/add-workflow-notes
```

Replace the placeholder with your own repository URL. If using SSH, confirm your SSH key is configured before pushing.

## Part E — Open a pull request

1. Open your repository on GitHub.
2. Select the prompt to compare and open a pull request for `docs/add-workflow-notes`.
3. Base: your default branch. Compare: `docs/add-workflow-notes`.
4. Describe what changed, why it changed and how you checked it.
5. Request a peer review if working in a group.

A pull request is a proposal for review; it is not the same thing as a commit or a merge.

## Part F — Review and improve

Ask a peer to check:
- Is the change focused and understandable?
- Are filenames and headings clear?
- Does the documentation contain secrets or personal data?
- Can another member reproduce the steps?

Make one requested improvement locally, commit it and push the same branch. The pull request updates automatically.

## Core challenge
Add `notes/commands.md` with five Git commands and a plain-English explanation for each. Commit and push the change. Add the file to the existing pull request.

## Intermediate stretch
Create a deliberate merge conflict in a disposable practice repository by editing the same line on two branches. Merge one branch, then resolve the conflict manually. Inspect `git status`, the conflict markers and the final diff. Do not practise conflict resolution in a production repository.

## Common commands

| Command | Purpose |
|---|---|
| `git status` | Show working-tree and staging state |
| `git diff` | Inspect unstaged changes |
| `git diff --staged` | Inspect staged changes |
| `git switch -c name` | Create and switch to a branch |
| `git log --oneline` | Inspect concise history |
| `git remote -v` | Inspect configured remotes |
| `git push -u origin branch` | Publish branch and set upstream |

## Troubleshooting
- **`src refspec ... does not match any`:** check the branch name with `git branch --show-current` and ensure at least one commit exists.
- **Push rejected (non-fast-forward):** stop and inspect the remote history. Do not force-push shared branches. Fetch and integrate the remote changes deliberately.
- **Authentication failed:** use GitHub's supported browser/device flow, credential manager or SSH setup. Never use your account password as a Git HTTPS password.
- **Wrong author identity:** correct local/global Git config for future commits; ask the facilitator before rewriting published history.
- **Merge conflict:** edit the marked file, remove conflict markers, run checks, stage and commit the resolution.

## Evidence
Submit the pull-request URL and `week-04-evidence.md` containing:
- Repository and branch names.
- Commit history.
- Pull request summary.
- One peer-review comment and how you responded.
- One Git problem and how you diagnosed it.

Never include access tokens or credential files in the repository.

## Cleanup
Keep the repository as portfolio evidence. If you created a test token at any point, revoke it immediately; this lab does not require one.
