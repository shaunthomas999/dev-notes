# Node.js

## Node.js installation

### NVM

#### Option-1: Download and install
* It is recommended to install Node.js using package manager such as `nvm` to manage different versions.
* Install nvm using script - `curl -o- https://raw.githubusercontent.com/nvm-sh/nvm/v0.39.1/install.sh | bash`
* Above script will make some entries in .bash_profile file. So you need to close and open the terminal again.
* To see all the versions - `nvm ls-remote`
* Reference
  * Installation instructions, go to https://github.com/creationix/nvm#install-script

```sh
export NVM_DIR="$HOME/.nvm"
[ -s "$NVM_DIR/nvm.sh" ] && \. "$NVM_DIR/nvm.sh"  # This loads nvm
#[ -s "$NVM_DIR/bash_completion" ] && \. "$NVM_DIR/bash_completion"  # This loads nvm bash_completion
```

#### Option-2: brew install
* `brew install nvm`

```sh
export NVM_DIR=~/.nvm
source $(brew --prefix nvm)/nvm.sh
```

## NPM
* NPM external registry - `npm set registry <registry_url>`
