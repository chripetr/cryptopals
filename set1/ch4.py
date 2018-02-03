#!/usr/bin/env python

################################################
# Detect single-character XOR - set 1/ chall 4 #
################################################

from collections import defaultdict
from binascii import unhexlify as unhex
from string import printable

# we can use the hint and count only
# the 12 most common english letters: "ETAOIN SHRDLU"
freqs = {
    'e':13, 't':12, 'a':11, 'o':10,
    'i':9,  'n':8,  ' ':7,  's':6,
    'h':5,  'r':4,  'd':3,  'l':2, 'u':1}

def score(sentence):
    score = 0
    for x in sentence:
        if x.lower() in freqs: 
            score += freqs[x.lower()]
        elif x not in printable:
            score -= 1 # whatever here for non-printable chars
        else:
            pass
    return score

def xor(s,key):
    return ''.join(chr(ord(i)^ord(key)) for i in s)

with open('file.txt', 'r') as f:
    ciphers = f.read().splitlines()

results = defaultdict(list)

for key in printable:
    for cipher in ciphers:
        out = xor(unhex(cipher),key)
        results[score(out)].append((out,key))

outcome = max(results)
print '\n[result] {} [Max score] {} [key] {}\n'.format(results[outcome][0][0], outcome, results[outcome][0][1])
#_EOF