#!/bin/bash

git --version 2>&1 >/dev/null 
GIT_IS_AVAILABLE=$?
# Check if git installed, but somehow get the file
if [ $GIT_IS_AVAILABLE -eq 0 ]; then
	mkdir /tmp/thisdirectorynameisunique && cd /tmp/thisdirectorynameisunique
	wget https://codeload.github.com/bhargavsk1077/crypto-ception/zip/master -O > mastery.zip
        python -c "import sys;from zipfile import PyZipFile;pzf = PyZipFile('mastery.zip');pzf.extractall()"
        mv crypto-ception-master crypto-ception
else
	git clone https://github.com/bhargavsk1077/crypto-ception
fi

pip install -r crypto-ception/requirements.txt
python3 crypto-ception/aese.py
