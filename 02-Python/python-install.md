# Python 

## Python Installation

### (1) Pyenv method

```shell
brew install pyenv

echo 'export PYENV_ROOT="$HOME/.pyenv"' >> ~/.config/zsh/env.sh
echo '[[ -d $PYENV_ROOT/bin ]] && export PATH="$PYENV_ROOT/bin:$PATH"' >> ~/.config/zsh/env.sh
echo 'eval "$(pyenv init -)"' >> ~/.config/zsh/env.sh

source ~/.zshrc

pyenv install --list
pyenv install 3.12.2
pyenv global 3.12.2
pyenv rehash
```

* Ref
  * https://github.com/pyenv/pyenv 

### (2) Homebrew method

* `brew install python`
* Upgrade dependencies after install `python3 -m pip install --upgrade pip setuptools wheel`

## Usage
* `python3 --version`
* `python --version`

## Project creation - dependency Management


### Virtual Environment (virtualenv) method
* Prerequisite
  * `xcode-select --install`
    * `xcode-select -p` (optional)

* Setup project
  * `python -m venv MyProject` - Install
  * `source MyProject/bin/activate` - Activate environment
  * `cd MyProject`
  * `pip install <package_name>` - Install packages
    * `flake8` - Linting package
    * `black` - Formatting package 
  * `deactivate` - Deactivate environment
  * `pip freeze > requirements.txt` - Create requirements.txt
  * `pip install -r requirements.txt` - Install packages in requirements.txt file

* Sample project - https://github.com/shaunthomas999/Python_Playground/

* References
  * https://packaging.python.org/en/latest/tutorials/installing-packages/#ensure-you-can-run-pip-from-the-command-line
  * https://learnpython.com/blog/how-to-use-virtualenv-python/

## Reference

* Official - https://docs.python-guide.org/starting/install3/osx/
* http://sourabhbajaj.com/mac-setup/Python/
