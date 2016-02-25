import calendar
from datetime import datetime
N=int(input())
for i in range(N):
    j1=input().split()   
    j2=input().split()
    s1=j1[0]+":"+j1[1]+":"+j1[2]+":"+j1[3]+":"+j1[4]+":"+j1[5]
    s2=j2[0]+":"+j2[1]+":"+j2[2]+":"+j2[3]+":"+j2[4]+":"+j2[5]
    FMT='%a:%d:%b:%Y:%H:%M:%S:%z'
    tdelta=datetime.strptime(s2, FMT) - datetime.strptime(s1, FMT)
    print (int(abs(tdelta.total_seconds())))
