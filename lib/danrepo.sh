#!/usr/bin/expect -f
set timeout -1
spawn /bin/bash
send "source /home/d04/fcm/bin/mosrs-setup-gpg-agent\n"
expect "Met Office Science Repository Service password:"
send "$1\n"
interact

# place in bash_profie as bashrc loads each time a new shell is opened. 
# original command uses . file  instead of source file - these are equivalent


