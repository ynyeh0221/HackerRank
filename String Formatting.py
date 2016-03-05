# Enter your code here. Read input from STDIN. Print output to STDOUT
n=int(raw_input())
length=len(bin(n))-2+1
for i in xrange(1,n+1):
    space=""
    space0=""
    space1=""
    space2=""
    for j in xrange(length-len(str(i))-1):
        space+=" "
    for j in xrange(length-len(oct(i))+1):
        space0+=" "
    for j in xrange(length-len(hex(i))+2):
        space1+=" "
    for j in xrange(length-len(bin(i))+2):
        space2+=" "
    s=space
    s+=str(i)+space0+oct(i)[1:]+space1+hex(i)[2:].upper()+space2+bin(i)[2:]
    print s
