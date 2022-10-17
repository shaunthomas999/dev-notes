# Python 

## Project

* Manage dependencies via pyenv or virtual environment
    * https://packaging.python.org/en/latest/tutorials/installing-packages/#ensure-you-can-run-pip-from-the-command-line  

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

## Reference

* Official - https://docs.python-guide.org/starting/install3/osx/
* http://sourabhbajaj.com/mac-setup/Python/
