#!/usr/bin/env python

################################################
# Implement repeating-key XOR - set 1/ chall 5 #
################################################

from binascii import hexlify as hexl

def xor(s,k):
    return ''.join(chr(ord(i)^ord(j)) for i,j in zip(s,k))

text = """Burning 'em, if you ain't quick and nimble
I go crazy when I hear a cymbal"""

key = 'ICE'
repeated_KEY = (key * ((len(text)/len(key))+1))[:len(text)]

# we print the result in hex...
print hexl(xor(text,repeated_KEY))