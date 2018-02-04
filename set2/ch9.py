#!/usr/bin/env python


#############################################
# Implement PKCS#7 padding - set 2/ chall 9 #
#############################################

def PKCS7padding(string, PADDING=16):
	"""padding must be less than 256"""
    if len(string)<PADDING<=256:
        diff = PADDING-(len(string)%PADDING)
    else:
        diff = 0
    return '{0}{1}'.format(string,chr(diff)*diff)

key = "YELLOW SUBMARINE"
padded = PKCS7padding(key,20)
print '[PADDED] {} [LENGTH] {}'.format(padded,len(padded))
#_EOF