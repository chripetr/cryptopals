#!/usr/bin/env python


####################################
# AES in ECB mode - set 1/ chall 7 #
####################################

from base64 import b64decode
from Crypto.Cipher import AES

key = 'YELLOW SUBMARINE'

with open('file3.txt', 'r') as f:
    cipher = b64decode(f.read())

def decryptAES_ECB(cipher):
    aes = AES.new(key, AES.MODE_ECB)
    return aes.decrypt(cipher)

print decryptAES_ECB(cipher)
#_EOF