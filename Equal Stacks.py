# Enter your code here. Read input from STDIN. Print output to STDOUT
s = raw_input()
s = map(int, s.split(' '))
num_of_c1, num_of_c2, num_of_c3 = s[0], s[1], s[2]
s = raw_input()
s1 = map(int, s.split(' '))
s = raw_input()
s2 = map(int, s.split(' '))
s = raw_input()
s3 = map(int, s.split(' '))
h1, h2, h3 = sum(s1), sum(s2), sum(s3)
if h1 == h2 and h2 == h3:
    print h1
else:
    ind1 = ind2 = ind3 = 0
    res = 0
    while h1 > 0 and h2 > 0 and h3 > 0:
        if h1 == h2 and h2 == h3:
            res = h1
            break
        if h1 != min(h1, h2, h3):
            h1 -= s1[ind1]
            ind1 += 1
        if h2 != min(h1, h2, h3):
            h2 -= s2[ind2]
            ind2 += 1
        if h3 != min(h1, h2, h3):
            h3 -= s3[ind3]
            ind3 += 1
    print res
