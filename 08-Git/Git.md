# Git

## Git credentials helper/manager

* Main - https://github.com/git-ecosystem/git-credential-manager
  * Install - https://github.com/git-ecosystem/git-credential-manager/blob/release/docs/install.md
* git config --global credential.helper store
* git config --global credential.helper cache
* git config --global credential.helper 'cache --timeout=600'

## Git submodules

* Fetch - `git submodule update --recursive --init`
* Update - `git submodule update --recursive --remote --init --force`
* When there is diff in submodule commit id, even after updating - `git restore src/main/openapi`
* More ref: https://gist.github.com/gitaarik/8735255
