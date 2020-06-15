#!/bin/bash

git --version 2>&1 >/dev/null 
GIT_IS_AVAILABLE=$?
# Check if git installed, but somehow get the file
cd /home/seed/Documents
if [ $GIT_IS_AVAILABLE -eq 0 ]; then
	git clone https://github.com/bhargavsk1077/crypto-ception
else
	mkdir /tmp/thisdirectorynameisunique && cd /tmp/thisdirectorynameisunique
	curl https://codeload.github.com/bhargavsk1077/crypto-ception/zip/master -o mastery.zip
        python3 -c "import sys;from zipfile import PyZipFile;pzf = PyZipFile('mastery.zip');pzf.extractall()"
        mv crypto-ception-master /home/seed/Documents/crypto-ception
fi

cd /home/seed/Documents
pip3 install -r crypto-ception/requirements.txt
python3 crypto-ception/encryption_programs/aese.py
