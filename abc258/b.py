# import numpy as np
n  =int(input())
a = []
for i in range(n):
    tmp = list(input())
    a.append(tmp)

# print(a)
nw_ = 0

arr = []
direction = [(0,1),(1,1),(1,0),(1,-1),(0,-1),(-1,-1),(-1,0),(-1,1)]

for i in range(n):
    for j in range(n):
        for d in direction:
            vx = i
            vy = j
            s = a[i][j]
            for _ in range(n-1):
                vx = (vx+d[0])%n
                vy = (vy+d[1])%n
                s = s + a[vx][vy]
            arr.append(s)
arr.sort(reverse=True)
# print(arr)
print(arr[0])
