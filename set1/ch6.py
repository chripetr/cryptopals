#!/usr/bin/env python
# -*- coding: utf-8 -*-

############################################
# Break repeating-key XOR - set 1/ chall 6 #
############################################

from numpy import float64
from base64 import b64decode
from string import printable
from itertools import izip_longest

FREQS = {
    'e':13, 't':12, 'a':11, 'o':10,
    'i':9,  'n':8,  ' ':7,  's':6,
    'h':5,  'r':4,  'd':3,  'l':2, 'u':1}

def hamming(a,b):
    return ''.join(bin(ord(i)^ord(j)) for i,j in zip(a,b)).count('1')

def string_score(text):
    score = 0
    for word in text:
        if word.lower() in FREQS: 
            score += FREQS[word.lower()]
    return score

def xor(s,key):
    return ''.join(chr(ord(i)^ord(key)) for i in s)

def normDistance(k):
    # I chose bigger slices for more accurate results
    return float64(hamming(cipher[:k*10],cipher[k*10:2*10*k]))/float64(k)

def getPlainText(text,key):
    """breaks repeated key XOR when key is known"""
    rk = (key * ((len(text)/len(key))+1))[:len(text)]
    return ''.join(chr(ord(i)^ord(j)) for i,j in zip(text,rk))

with open('file2.txt', 'r') as f: cipher = b64decode(f.read())

keysizes = {i:normDistance(i) for i in range(2,41)}
candidates = sorted(keysizes, key=keysizes.get)[:3]
print candidates

# now lets break the cipher-text in keysize blocks...
for ksz in candidates:
    blocks = [cipher[i:i+ksz] for i in range(0,len(cipher),ksz)]
    tr_blocks = map(lambda i: ''.join(list(i)), list(izip_longest(*blocks, fillvalue='0')))

    # apply single-byte XOR cipher to every block...
    best = []
    for blck in tr_blocks:
        results = {string_score(xor(blck,key)):key for key in printable}
        best.append(results[max(results)]) # get the best key...

    BestKey = ''.join(best)
    print '[+] Key with keysize {} --> {}'.format(ksz, BestKey)
    print getPlainText(cipher,BestKey)
    print '\n\n'
#_EOF