# Enter your code here. Read input from STDIN. Print output to STDOUT
import sys

def delta(i, j, x, y):
    if i == x:
        if j + 1 == y:
            if board[i][j] == 'R':
                return 0
            else:
                return 1
        else:
            if board[i][j] == 'L':
                return 0
            else:
                return 1
    else:
        if i + 1 == x:
            if board[i][j] == 'D':
                return 0
            else:
                return 1
        else:
            if board[i][j] == 'U':
                return 0
            else:
                return 1
            
s = raw_input().split(' ')
N = int(s[0])
M = int(s[1])
K = int(s[2])
x, y = 0, 0
board = []
for i in xrange(N):
    temp = raw_input()
    board += [temp]
    if '*' in temp:
        x, y = len(board)-1, temp.index('*')
T = [[[sys.maxint for j in xrange(M)] for i in xrange(N)] for k in xrange(K+1)]
for k in range(K + 1):
    for i in range(N):
        for j in range(M):
            if k == 0:
                if i == 0 and j == 0:
                    T[k][i][j] = 0
            else:
                res = sys.maxint
                if i > 0:
                    res = min(res, T[k - 1][i - 1][j] + delta(i-1,j,i,j))
                if i + 1 < N:                     
                    res = min(res, T[k - 1][i + 1][j] + delta(i+1,j,i,j))
                if j > 0:
                    res = min(res, T[k - 1][i][j - 1] + delta(i,j-1,i,j))
                if j + 1 < M:
                    res = min(res, T[k - 1][i][j + 1] + delta(i,j+1,i,j))
                T[k][i][j] = min(res, T[k - 1][i][j])
print -1 if T[K][x][y] == sys.maxint else T[K][x][y]
