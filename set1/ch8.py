#!/usr/bin/env python
# -*- coding: utf-8 -*-

###########################################
# Detect AES in ECB mode - set 1/ chall 8 #
###########################################

from binascii import hexlify as hexl
from binascii import unhexlify as unhex

def findPatterns(cipher, BLOCKSIZE=16):
    """find number of repeated 16-byte-blocks"""
    patterns = {}
    for i in range(len(cipher)):
        block = cipher[i:i+BLOCKSIZE]
        try:
            patterns[block] += 1
        except KeyError:
            patterns[block] = 0
    return sum(patterns.values())

with open('file4.txt','r') as f:
    ciphers = map(unhex, f.read().splitlines())

paterns = {i:findPatterns(cipher) for i,cipher in enumerate(ciphers)}

# +1 due to zero index...
line = max(paterns, key=paterns.get)
print '[LINE {}]: {}'.format(line+1, hexl(ciphers[line]))
#_EOF