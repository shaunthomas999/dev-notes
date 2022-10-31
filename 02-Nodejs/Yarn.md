# Yarn 

## Installation

* For installing yarn we will use Homebrew, but we will ask it to remove the node version it will automatically install, while leaving yarn in place.
  * `brew install yarn`
  * `brew uninstall node --ignore-dependencies`
* This will actually break Homebrew, but we will fix it immediately, assuming you have just one version installed of NodeJS through nvm,
  * `ln -s ~/.nvm/versions/node/ /usr/local/Cellar/`

## Reference
* Mac installation - https://yarnpkg.com/en/docs/install#mac-stable
