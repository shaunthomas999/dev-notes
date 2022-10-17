# Python 

## Project

## Python Installation

### Homebrew method

* `brew install python`
* Upgrade dependencies after install `python3 -m pip install --upgrade pip setuptools wheel`

### Pyenv method

```shell
brew install pyenv
echo 'eval "$(pyenv init -)"' >> ~/.bash_profile
source ~/.bash_profile
pyenv install 3.7.0
pyenv global 3.7.0
pyenv rehash
```

## Usage
* `python3 --version`
* `python --version`

## Dependency Management

### virtualenv method
* Manage dependencies via pyenv or virtual environment
    * https://packaging.python.org/en/latest/tutorials/installing-packages/#ensure-you-can-run-pip-from-the-command-line
* https://learnpython.com/blog/how-to-use-virtualenv-python/
* Quick Commands
  * `pip install virtualenv` - Install
  * `virtualenv -p python3 envname` - Create virtual environment
  * `source envname/bin/activate` - Activate environment
  * `pip install` - Install packages
  * `deactivate` - Deactivate environment
  * `pip freeze > requirements.txt` - Create requirements.txt 

## Reference

* Official - https://docs.python-guide.org/starting/install3/osx/
* http://sourabhbajaj.com/mac-setup/Python/
