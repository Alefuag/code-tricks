### Git


- `git reset --hard origin/master` : discard local changes and sync with head of repo
- `git rev-parse --abbrev-ref HEAD` : get current branch name
- `git config --global credential.helper store` : set up git to store credentials

- `git -C custom_dir command`: execute git command taking `custom_dir` as project root

---

- `git worktree`
- git aliases
- `git fetch -p && for branch in $(git branch -vv | grep ': gone]' | awk '{print $1}'); do git branch -D $branch; done` : delete local branches that are deleted on remote

