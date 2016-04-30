# Enter your code here. Read input from STDIN. Print output to STDOUT
T=int(raw_input())
for i in xrange(T):
    N=int(raw_input())
    fline=map(int,list(raw_input()))
    sline=map(int,list(raw_input()))
    flatten=[0]*(N*2)
    for j in xrange(N):
        flatten[2*j]=fline[j]
        flatten[2*j+1]=sline[j]

    for j in xrange(len(flatten)-1):
        if flatten[j]==0 and flatten[j+1]==0:
            flatten[j]=1
            flatten[j+1]=1
        elif j+2<len(flatten) and flatten[j]==0 and flatten[j+1]==1 and flatten[j+2]==0:
            flatten[j]=1
            flatten[j+2]=1
    check=0
    for i in flatten:
        if i==1:
            check+=1
    if check==len(flatten):
        print "YES"
    else:
        print "NO"
