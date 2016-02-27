import fileinput
X, Y, Z, N = map(int, fileinput.input())
nums=[[x, y, z] for x in range(X+1) for y in range(Y+1) for z in range(Z+1) if x + y + z != N]
print nums
