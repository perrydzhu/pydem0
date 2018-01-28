import random
import string
import binascii
from Crypto import Random
import os

s = "1111"

tmp = binascii.a2b_hex(s)
print(binascii.b2a_hex(tmp))

r = os.urandom(4)

h = binascii.b2a_hex(r)
u = binascii.b2a_uu(r)

print(h)
print(u)
print(binascii.b2a_qp(r))

print(''.join(random.sample(string.ascii_letters+string.digits, 8)))
