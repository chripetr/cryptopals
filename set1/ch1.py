#!/usr/bin/env python

##########################################
# Convert hex to base64 - set 1/ chall 1 #
##########################################

from base64 import b64encode as enc
from base64 import b64decode as dec
from binascii import unhexlify as unhex

msg = '49276d206b696c6c696e6720796f757220627261696e206c696b65206120706f69736f6e6f7573206d757368726f6f6d'

print enc(unhex(msg))

# bonus part
print dec(enc(msg.decode('hex')))