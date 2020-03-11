from Crypto.PublicKey import RSA


key = RSA.generate(2048)
#private_key = key.export_key()
private_key = key.exportKey('PEM')
file_out = open("private.pem", "wb")
file_out.write(private_key)

public_key = key.publickey().exportKey('PEM')
file_out = open("receiver.pem", "wb")
file_out.write(public_key)
