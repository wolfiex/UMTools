/usr/bin/expect <<EOD
spawn ~fcm/bin/mosrs-setup-gpg-agent
expect "Met Office Science Repository Service password:"
send "$1\n"
expect eof
EOD

