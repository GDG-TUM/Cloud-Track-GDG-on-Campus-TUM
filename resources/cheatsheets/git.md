[← Back to Cloud Track home](../../README.md)

# Git Cheat Sheet

```bash
git status                      # what changed
git add <file>                  # stage a file
git commit -m "feat: message"   # save a snapshot
git push origin <branch>        # upload
git pull                        # download and merge
git checkout -b <branch>        # new branch
git switch <branch>             # switch branch
git log --oneline               # history
git diff                        # unstaged changes
git restore <file>              # discard local changes to a file
git remote -v                   # show remotes
git fetch upstream && git rebase upstream/main   # sync a fork
```
**Commit types:** feat, fix, docs, style, refactor, test, chore.

[← All resources](../README.md)
