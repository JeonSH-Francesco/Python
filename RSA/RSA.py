#https://pycryptodome.readthedocs.io/en/latest/src/public_key/rsa.html
#https://pycryptodome.readthedocs.io/en/latest/src/cipher/oaep.html
#https://pycryptodome.readthedocs.io/en/latest/src/examples.html
#https://pycryptodome.readthedocs.io/en/latest/src/signature/pkcs1_v1_5.html

import base64
import crypto
import sys
sys.modules['Crypto'] = crypto
from Crypto.PublicKey import RSA
from Crypto.Cipher import PKCS1_OAEP
from Crypto.Signature import pkcs1_15
from Crypto.Hash import SHA256
 
 
class RSACipher:

	def __init__(self, bits):
		self.key = RSA.generate(bits)

	def encrypt(self, msg):
		cipher = PKCS1_OAEP.new(self.key)
		return cipher.encrypt(msg.encode())
	
	def decrypt(self, ct):
		cipher = PKCS1_OAEP.new(self.key)
		return cipher.decrypt(ct)

	def sign(self, msg):
		h = SHA256.new(msg.encode())
		sig = pkcs1_15.new(self.key).sign(h)
		return (h, sig)

	def verify(self, h, signature):
		try:
			pkcs1_15.new(self.key).verify(h, signature)
			return True
		except (ValueError, TypeError):
			return False

	def extractKey(self):
		privatekey = self.key.export_key()
		file_out = open("private.pem", "wb")
		file_out.write(privatekey)
		file_out.close()

		publickey = self.key.publickey().export_key()
		file_out = open("public.pem", "wb")
		file_out.write(publickey)
		file_out.close()
     
 
 
msg = 'Hello'
rsa = RSACipher(2048)
ct = rsa.encrypt(msg) 
pt = rsa.decrypt(ct) 

print('msg : ' + msg)
print('ct : ' + str(base64.b64encode(ct)))
print('pt : ' + str(pt))

(h, sig) = rsa.sign(msg)
isValid = rsa.verify(h, sig)

print('msg : ' + msg)
print('hash : ' + str(h.hexdigest()))
print('sig : ' + str(base64.b64encode(sig)))
print('isValid : ' + str(isValid))


rsa.extractKey()
