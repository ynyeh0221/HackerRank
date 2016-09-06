#!/bin/python

import sys


s = raw_input().strip()
n = long(raw_input().strip())
n_of_a = 0
for i in s:
    if i == 'a':
        n_of_a += 1
res = n_of_a * (n / len(s))
for i in s[:n % len(s)]:
    if i == 'a':
        res += 1
print res
