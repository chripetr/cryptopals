#!/usr/bin/env python

##############################
# fixed XOR - set 1/ chall 2 #
##############################

from binascii import unhexlify as unhex
from binascii import hexlify as hexl

a = '1c0111001f010100061a024b53535009181c'
b = '686974207468652062756c6c277320657965'

def xor(a,b):
    return ''.join(chr(ord(i)^ord(j)) for i,j in zip(a,b))

xored = xor(unhex(a),unhex(b))
print '[RAW]: {}'.format(xored)
print '[HEX]: {}'.format(hexl(xored))
