N = int(raw_input())
mails = []
for i in xrange(N):
    s = raw_input()
    if len(s.split('.')) != 2:
        continue
    ss = s.split('@')
    if len(ss) != 2:
        continue
    ss = [ss[0]] + ss[1].split('.')
    valid = True
    for c in ss[0]:
        if not (c.isalnum() or c == '-' or c == '_'):
            valid = False
            break
    if not valid or len(ss[0]) == 0 or not ss[1].isalnum() or len(ss[2]) > 3:
        continue    
    mails += [s]
print sorted(mails)
