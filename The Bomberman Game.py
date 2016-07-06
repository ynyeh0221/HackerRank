# 37.33 points, fail on testcase 4 and 6

# Enter your code here. Read input from STDIN. Print output to STDOUT
def detonate(pre_state, R, C):
    temp = [['O' for k in xrange(C)] for l in xrange(R)]
    for i in xrange(R):
        for j in xrange(C):
            if pre_state[i][j] == 'O':
                temp[i][j] = '.'
                if i-1 >= 0:
                    temp[i-1][j] = '.'
                if i+1 < R:
                    temp[i+1][j] = '.'
                if j-1 >= 0:
                    temp[i][j-1] = '.'
                if j+1 < C:
                    temp[i][j+1] = '.'
    return temp

s = raw_input().split(' ')
R = int(s[0])
C = int(s[1])
N = int(s[2])
grid = []
allb = [''.join(['O' for k in xrange(C)]) for l in xrange(R)] # Each grid has a bomber
allnb = [''.join(['O' for k in xrange(C)]) for l in xrange(R)] # Each grid doesn't have a bomber
dic = {} # record grid states
for i in xrange(R):
    grid += [list(raw_input())]
if N == 0 or N == 1:
    for i in [''.join(i) for i in grid]:
        print i
elif N == 2:
    for i in allb:
        print i
else:
    pre_state = grid[:]
    dic[tuple([''.join(i) for i in pre_state])] = 1
    remain_time = 0 # the remaining time when a existed state is encountered
    ans_type = 0
    for t in xrange(1, N-1, 2):
        pre_state = detonate(pre_state, R, C)
        temp2 = [''.join(i) for i in pre_state]
        if tuple(temp2) in dic:
            remain_time = N-2-t
            if temp2 == allnb:
                ans_type = 1
            break
        dic[tuple(temp2)] = 1
    if ans_type == 1:
        if remain_time % 4 == 0:
            for i in allnb:
                print i
        else:
            for i in allb:
                print i
    else:
        if remain_time % 4 == 0:
            for i in pre_state:
                print ''.join(i)
        elif remain_time % 4 == 1 or remain_time % 4 == 3:
            for i in allb:
                print i
        else:
            for i in detonate(pre_state, R, C):
                print ''.join(i)
