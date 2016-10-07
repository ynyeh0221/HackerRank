import sys
s_len = int(raw_input().strip())
s = raw_input().strip()
dic = {}
d = []
res = 0
for i in xrange(len(s)):
    if s[i] not in dic:
        dic[s[i]] = []
        d += [s[i]]
    dic[s[i]] += [i]
for i in xrange(len(d)):
    for j in xrange(i+1, len(d)):
        if abs(len(dic[d[i]]) - len(dic[d[j]])) > 1:
            continue
        count = 1
        newseq = [dic[d[i]][0], dic[d[j]][0]]
        length = min(len(dic[d[i]]), len(dic[d[j]]))
        if len(dic[d[j]]) > length:
            continue
        for k in xrange(1, length):
            if dic[d[i]][k] < newseq[-1]:
                break
            newseq += [dic[d[i]][k]]
            if dic[d[j]][k] < newseq[-1]:
                break
            newseq += [dic[d[j]][k]]
            count += 1
        if count == length:
            res = max(res, len(dic[d[i]]) + len(dic[d[j]]))
print res
