# Linux - Unix Commands

## Shell

* `fc` - Update last executed command
* `<command> | tee <file_name>` - Execute command and print output to stdout as well as file_name
  * https://www.geeksforgeeks.org/tee-command-linux-example/ 

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

### tree

* `tree .` # prints all the subdirectories.
* `tree -L 4` # prints up to 4 directories.
* `tree -I 'test* |docs|bin|lib'` # ignores the directories - test docs bin lib.
* `tree -P '.sh' --prune` # lists all the .sh files and --prune will remove empty directories from getting printed.

### grep

In the output of first command look for line containing `ls` and without containing `al`. Here `-v` reverse the normal grep functionality.

```bash
history | grep ls | grep -v al
```

### test

* Used to test an expression - `test 100 -lt 99 && echo "Yes." || echo "No."` - This will print "No." bcz expression is false.
* Used to check existence of files and more - `test -e test-security-gateway.log; echo $?` - This will print 0 if the file exists.

Ref: [](https://www.computerhope.com/unix/test.htm)

### rcp

Copy files from one computer to another

### scp

* Copy files securely from one computer to another (secure, encrypted)
* `scp <file_to_copy> <machine_to_copy_file-to>:<location_inside_machine_to_copy_file_to>`
  * E.g., `scp something.jar sys01.net:`
  * If location is not specified in target machine, then the file will be copied to `$HOME` directory

### rsync

Advanced copying tool

## Processes

### find process

* `ps aux | grep <keyword>`
* `ps -ef | grep <keyword>`

### kill

* `kill -9 <PID>` - Here 9 is the signal number which is `KILL` signal (see below for desc.).
  * Same as `kill -KILL <PID>` and `kill -SIGKILL <PID>` 
* `kill <PID>` - `TERM` signal is send as that's the default

#### signal types

* `TERM` - an application will be able to terminate, i.e. properly run a shutdown routine
* `KILL` - the applications is stopped and killed immediately (which could lead to data loss or raising apport to report a presumed crash in some cases)

## Network

### lsof

* list open files
* `lsof -i :<port_number>` - Give details of which application/process is consuming the port
* `lsof -nP +c 15 | grep LISTEN` - Show list of all consumed ports in a machine
  * https://wilsonmar.github.io/ports-open/
* `lsof -h` - Show list of all command line options

## Network

### Get IP address

* `ipconfig getifaddr en1` - on LAN
* `ipconfig getifaddr en0` - on WiFi
* `curl ifconfig.me` - public IP address

## Cheatsheets

* https://cheatography.com/davechild/cheat-sheets/linux-command-line/
