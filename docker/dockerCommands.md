# Docker

## lazydocker

* Good GUI tool to visualize internals of Docker in a machine
* https://github.com/jesseduffield/lazydocker#usage

### Installation (run using Docker)
* Ref: https://github.com/jesseduffield/lazydocker#docker
* Add this alias to zsh > `alias lzd='docker run --rm -it -v /var/run/docker.sock:/var/run/docker.sock -v ~/config/lazydocker:/.config/jesseduffield/lazydocker lazyteam/lazydocker'`
