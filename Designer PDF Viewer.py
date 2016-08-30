#!/bin/python

import sys


h = map(int,raw_input().strip().split(' '))
word = raw_input().strip()
height = []
for i in word:
    height += [h[ord(i) - ord('a')]]
print len(word) * max(height)
