import re

ptn = r'\w+'

s = 'abc'

m = re.match(ptn, s)
if m:
    print(m.group())
    print("match")
else:
    print("not match")



