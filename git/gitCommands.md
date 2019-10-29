# Git Commands

## git rebase

`git rebase -i HEAD~3` - Change git commit history of last 3 commits

## git reset

`git reset HEAD~` - Undo last commit and make the changes available locally

To revert effect to above command use `git reset HEAD@{1}`

## git branch

| Option | Desciption |
|:---:|:---:|
| `-a` | List local and remote branches |
| `-l` or `--list` | List local branches |
| `-d` | Delete merged local branch |
| `-D` | Delete local branch whether merged or not |

`git branch -d|-D [branch-name]` - To delete a branch

## git config

`git config user.email` - Get `user.email` git config property for current project
`git config user.email shaunthomas999[at]gmail.com` - Set `user.email` git config property for current project
`git config --global user.email` - Get global `user.email` git config property

## Cheat sheets

Github - [https://services.github.com/on-demand/downloads/github-git-cheat-sheet.pdf]()
Gitlab - [https://about.gitlab.com/images/press/git-cheat-sheet.pdf]()
Atlassian - [https://www.atlassian.com/git/tutorials/atlassian-git-cheatsheet]()
git-tower -  [https://www.git-tower.com/blog/git-cheat-sheet/]() (Need to sign-up with email and they will send the cheatsheet download link via email)
