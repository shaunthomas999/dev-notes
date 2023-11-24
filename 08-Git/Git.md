# Git

## Git credentials helper/manager

* Main - https://github.com/git-ecosystem/git-credential-manager
  * Install - https://github.com/git-ecosystem/git-credential-manager/blob/release/docs/install.md
* git config --global credential.helper store
* git config --global credential.helper cache
* git config --global credential.helper 'cache --timeout=600'

## Git submodules

* Init - `git submodule update --recursive --init`
  * Force init - `git submodule update --recursive --remote --init --force`
* Update in course of time - `git submodule update --recursive`
* `git submodule` - to see the submodule commit id that is in use
* When there is diff in submodule commit id, even after updating
  * `git restore src/main/openapi`
  * `git checkout -f --recurse-submodules`
* More ref: https://gist.github.com/gitaarik/8735255
