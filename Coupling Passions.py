import math
# Enter your code here. Read input from STDIN. Print output to STDOUT
def distance_between(point1, point2):
    EARTH_RADIUS = 6371
    point1_lat_in_radians  = math.radians( point1['latitude'] )
    point2_lat_in_radians  = math.radians( point2['latitude'] )
    point1_long_in_radians  = math.radians( point1['longitude'] )
    point2_long_in_radians  = math.radians( point2['longitude'] )

    return math.acos( math.sin( point1_lat_in_radians ) * math.sin( point2_lat_in_radians ) +
                 math.cos( point1_lat_in_radians ) * math.cos( point2_lat_in_radians ) *
                 math.cos( point2_long_in_radians - point1_long_in_radians) ) * EARTH_RADIUS

m = int(raw_input())
people = {}
locations = {}
interests = {}
for p in xrange(m):
    s = raw_input().split(' ')
    people[p] = s[1:]
    for i in s[1:]:
        interests[i] = 1
z = int(raw_input())
for l in xrange(z):
    s = raw_input().split(' ')
    locations[s[0]] = {'latitude': float(s[1]), 'longitude': float(s[2])}
    locations[s[0]]['passions'] = set()
    for ll in xrange(4, 4 + int(s[3])):
        locations[s[0]]['passions'].add(s[ll])
res = []
for l in locations:
    interest_set = set()
    for i in interests:
        if i in locations[l]['passions']:
            interest_set.add(i)
    res += [[l, interest_set]]
commons = 0
commons_list = []
for i in xrange(len(res)):
    for j in xrange(i+1, len(res)):
        temp = len(res[i][1] | res[j][1])
        if temp >= commons:
            commons = temp
            if res[i][0] < res[j][0]:
                commons_list += [[res[i][0], res[j][0], commons, distance_between(locations[res[i][0]], locations[res[j][0]])]]
            else:
                commons_list += [[res[j][0], res[i][0], commons, distance_between(locations[res[i][0]], locations[res[j][0]])]]
commons_list = sorted(commons_list, key = lambda x : (-x[2], x[3]))
print commons_list[0][0] + ' ' + commons_list[0][1]
