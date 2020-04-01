# crypto-ception
A ransomware implementation using python , aes and rsa encryption

aese.py - python script which encrypts all files from the current working diretory , makes a readme file and places the encrypted keys inside

aesd.py - python script which decrypts all files (when placed in the directory in which the readme folder created by aese.py is present)

rsa.py - program to generate rsa-2048 key pair which can be hardcoded in the encryption and decryption scripts

WARNING : the executable file 'aese' is programmed to encrypt everything from the home directory of the user. so do not try this without a virtual machine to test it on.
