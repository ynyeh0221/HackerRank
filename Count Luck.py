def dfs(i, j, m, path, visited):
    global finalpath
    if i < 0 or i >= len(m) or j < 0 or j >= len(m[0]) or visited[i][j] or m[i][j] == 'X':
        return
    if m[i][j] == '*':
        finalpath = path[:]
        return
    visited[i][j] = True
    pass_dir = 0
    if i-1 >= 0 and m[i-1][j] != 'X' and not visited[i-1][j]:
        pass_dir += 1
    if i+1 < len(m) and m[i+1][j] != 'X' and not visited[i+1][j]:
        pass_dir += 1
    if j-1 >= 0 and m[i][j-1] != 'X' and not visited[i][j-1]:
        pass_dir += 1
    if j+1 < len(m[0]) and m[i][j+1] != 'X' and not visited[i][j+1]:
        pass_dir += 1
    wave = 0
    if pass_dir > 1:
        wave = 1
    dfs(i-1, j, m, path + [wave], visited)
    dfs(i+1, j, m, path + [wave], visited)
    dfs(i, j-1, m, path + [wave], visited)
    dfs(i, j+1, m, path + [wave], visited)
    visited[i][j] = False

T = int(raw_input())
for t in xrange(T):
    [M,N] = map(int, raw_input().split())
    m = []
    si = sj = 0
    for i in xrange(M):
        m += [raw_input()]
        if 'M' in m[i]:
            si = i
            sj = m[i].index('M')
    K = int(raw_input())
    visited = []
    for i in xrange(M):
        visited += [[]]
        for j in xrange(N):
            visited[i] += [False]
    global finalpath
    finalpath = []
    dfs(si, sj, m, [], visited)
    if sum(finalpath) == K:
        print 'Impressed'
    else:
        print 'Oops!'
