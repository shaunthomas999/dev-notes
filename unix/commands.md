# Commands

## Shell

## Change shell

* `echo $0` - Check which shell is running now
* `chsh -s /bin/bash` - To set bash as default shell for `current (logged-in)` user
* `sudo chsh -s /bin/bash` - To set bash as default shell for `root` user

Close and open terminal again to see the effect. Note: shell should be in `/etc/shells` list for this to work

* `/bin/bash` - Run bash shell temporarily in open terminal session
* `/bin/zsh` - Run zsh temporarily in open terminal session

## File System

### ls

* `ls -lh` - To see human readable logical space usage
* `ls - ks` - To see physical space usage

### du

* `du -h` - To see disk space usage (physical)
