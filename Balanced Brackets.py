#!/bin/python

import sys


t = int(raw_input().strip())
for a0 in xrange(t):
    s = list(raw_input().strip())
    stack = []
    valid = True
    for i in s:
        if i == ')':
            if not stack or stack[-1] != '(':
                valid = False
                break
            else:
                stack.pop()
        elif i == ']':
            if not stack or stack[-1] != '[':
                valid = False
                break
            else:
                stack.pop()
        elif i == '}':
            if not stack or stack[-1] != '{':
                valid = False
                break
            else:
                stack.pop()
        else:
            stack += [i]
    print "YES" if (valid and not stack) else "NO"
