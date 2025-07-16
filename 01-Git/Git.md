# Git

## Git LFS (Large File Storage)
* https://git-lfs.com/
  * `brew install git-lfs`
  * `git lfs install`
  * `git lfs track "*.psd"`
  * `git add .gitattributes`
 * `git lfs migrate` - migrate existing files already checked-in
 * Supported in Github, Azure Devops etc.
 * Look at `.gitattributes` file in the folder for reference
 * See config - `git lfs env`
   * `git lfs version`
## Git credentials helper/manager

* Main - https://github.com/git-ecosystem/git-credential-manager
  * Install - https://github.com/git-ecosystem/git-credential-manager/blob/release/docs/install.md (macOS / Windows / Linux)
    * Windows - standalone - Git Credentials Manager - https://github.com/git-ecosystem/git-credential-manager/releases - Download latest version
* git config --global credential.helper store 
  * Stores credentials as plain text in `~/.git-credentials` 
* git config --global credential.helper cache
* git config --global credential.helper 'cache --timeout=600'

## Git submodules

### Add submodule
* `git submodule add <git_repository_url> <submodule_path>` - To add a git submodule
  - After add the submodule folder will be empty. The below command will load files into the submodules's folder
* `git submodule update --recursive --init`
  - Setup the submodule the first time
  - `git submodule update --recursive --init` - Simple
  - `git submodule update --recursive --init --force` - Force init
  - `git submodule update --recursive --remote --init --force` - Remote force init

### Update submodule
* Update in course of time
  * `git submodule update --recursive --remote`
  * `git submodule update --recursive --remote --force`
* `cd <submodule>`
* `<submodule>$> git checkout main`
* `<submodule>$> git pull`
    - Pull down the changes
    - Then go to parent git project
* `git add <submodule_path>`
* `git commit -m "Message about submodule commit"`

### View submodule
* `git submodule` - To know about which commit is in submodule
  
### Dealing with submodule differences in git
* When there is diff in submodule commit id, even after updating
  * `git restore <path_to_submodule_folder>`
    * E.g. - `git restore src/main/openapi`
  * `git checkout -f --recurse-submodules`
  * More ref: https://gist.github.com/gitaarik/8735255
* Other commands
  * `git submodule update --recursive --remote --force`
  * `git submodule update --recursive --remote --init --force` 

## git rebase

`git rebase -i HEAD~3` - Change git commit history of last 3 commits

## git reset

`git reset --mixed HEAD~` - Undo last commit and make the changes available locally

To revert effect to above command use `git reset HEAD@{1}`

![Git Reset Types](https://itknowledgeexchange.techtarget.com/coffee-talk/files/2023/08/git-reset.png)

* `--soft` - Reset from HEAD but not from staging index
* `--hard` - Reset from HEAD, staging index and working directory
* `--mixed` - Reset from HEAD and staging index but not from working directory (you can see the changes in the working directory)

## git branch

| Option | Desciption |
|:---:|:---:|
| `-a` | List local and remote branches |
| `-l` or `--list` | List local branches |
| `-d` | Delete merged local branch |
| `-D` | Delete local branch whether merged or not |
| `-vva` | Show all the details about branches |

`git branch -d|-D [branch-name]` - To delete a branch

## git config

* `git config user.email` - Get `user.email` git config property for current project
* `git config user.email shaunthomas999[at]gmail.com` - Set `user.email` git config property for current project
* `git config --global user.email` - Get global `user.email` git config property

* `git config -l` - See all configs

## git remote

* `git remote show origin` - See remote origin
* `git remote -v` - See all remotes locally
* `git remote rename origin old-origin` - Change origin - Manage 2 repos
* `git remote rm old-origin` - Remove a origin

## git reflog

* This contains history of all commands locally executed by the user. It gives the possibility to revert back changes whenever required. This even has things deleted from git repo.

## gitignore

* `git rm --cached -r .idea`

## git clone

* non-bare clone (normal clone) - `git clone`
* bare clone - `git clone --bare` - Copy a repo including all history, branches, tags etc.
* mirror clone - `git clone --mirror` - To keep a repo as a mirror to another repo
* References
  * https://docs.github.com/en/repositories/creating-and-managing-repositories/duplicating-a-repository#mirroring-a-repository-in-another-location
  * https://blog.tinned-software.net/git-and-multiple-remotes/

## git cherry-pick

* `git checkout -b <branch_name>` - Checkout a branch
* `git cherry-pick <commit-id>` - Cherry pick commit to the checked out branch
* `git cherry-pick -m 1 <commit-id>` - Cherry pick a merge commit. `-m 1` means first parent which is usually the commit in the branch

## Cheat sheets

* Github - [https://services.github.com/on-demand/downloads/github-git-cheat-sheet.pdf]()
* Gitlab - [https://about.gitlab.com/images/press/git-cheat-sheet.pdf]()
* Atlassian - [https://www.atlassian.com/git/tutorials/atlassian-git-cheatsheet]()
* git-tower -  [https://www.git-tower.com/blog/git-cheat-sheet/]() (Need to sign-up with email and they will send the cheatsheet download link via email)
