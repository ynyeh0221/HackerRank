#!/bin/python

import sys


s = raw_input().strip()
res = 0
if len(s) > 0:
    res = 1
for i in xrange(1, len(s)):
    if ord(s[i]) >= ord('A') and ord(s[i]) <= ord('Z'):
        res += 1
print res 
