N = int(raw_input())
stack = []
maxx = 0
for i in xrange(N):
    s = map(int, raw_input().split())
    if s[0] == 1:
        stack += [s[1]]
        if stack[-1] > maxx:
            maxx = stack[-1]
    elif s[0] == 2:
        if maxx == stack[-1]:
            stack.pop()
            if stack:
                maxx = max(stack)
            else:
                maxx = 0
        else:
            stack.pop()
    else:
        print maxx
