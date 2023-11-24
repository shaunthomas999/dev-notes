# Git

## Git credentials helper/manager

* Main - https://github.com/git-ecosystem/git-credential-manager
  * Install - https://github.com/git-ecosystem/git-credential-manager/blob/release/docs/install.md
* git config --global credential.helper store
* git config --global credential.helper cache
* git config --global credential.helper 'cache --timeout=600'

## Git submodules

### Add
* `git submodule add <git_repository_url> <submodule_path>` - To add a git submodule
  - After add the submodule folder will be empty. The below command will load files into the submodules's folder
* `git submodule update --recursive --init`
  - Setup the submodule the first time
  - `git submodule update --init` - Simple
  - `git submodule update --recursive --remote --init --force` - Force init

### Update
* Update in course of time - `git submodule update --recursive --init`
* `cd <submodule>`
* `<submodule>$> git checkout master`
* `<submodule>$> git pull`
    - Pull down the changes
    - Then go to parent git project
* `git add <submodule_path>`
* `git commit -m "Message about submodule commit"`

### View
* `git submodule` - To know about which commit is in submodule
  
### Others
* When there is diff in submodule commit id, even after updating
  * `git restore src/main/openapi`
  * `git checkout -f --recurse-submodules`
* More ref: https://gist.github.com/gitaarik/8735255





