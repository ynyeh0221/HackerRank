[N, b] = map(int, raw_input().split())
in_b = [False for i in xrange(N)]
points = []
for i in xrange(N):
    points += [map(float, raw_input().split())]
    points[i][0] = int(points[i][0])
points = sorted(points, key = lambda x : x[0])
sorted_points = sorted(points, key = lambda x : x[3], reverse = True)
for i in xrange(b):
    in_b[sorted_points[i][0]-1] = True
to_use = b

while True:
    try:
        s = raw_input()
    except:
        break
    s = s.split()
    ty = s[0]
    ind = int(s[1])
    if ty == "F" or ty == "f":
        if in_b[ind-1] == True:
            print s[1] + " = (" + "%.3f" % round(points[ind-1][1],3) + "," + "%.3f" % round(points[ind-1][2],3) + "," + "%.3f" % round(points[ind-1][3],3) + ")"
        else:
            print "Point doesn't exist in the bucket."
    else:
        if in_b[ind-1] == True:
            if to_use >= N:
                print "No more points can be deleted."
            else:
                in_b[ind-1] = False
                in_b[sorted_points[to_use][0]-1] = True
                to_use += 1
                print "Point id "+ str(ind) +" removed."
        else:
            print "Point doesn't exist in the bucket."
