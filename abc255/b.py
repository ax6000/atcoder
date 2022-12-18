
import math
import numpy as np
n,k = map(int, input().split())
a = list(map(int, input().split()))
x = []
y = []
for i in range(n):
   tmp_x,tmp_y = map(int, input().split())0
   x.append(tmp_x)
   y.append(tmp_y)

dists = np.zeros((n,n)) 

for p in range(n):
    for q in range(n):
        dists[p,q] = math.sqrt((x[p]-x[q])**2 + (y[p]-y[q])**2)

max_dists = np.zeros(n)
tmp = np.zeros((k,n))
for q in range(k):
    tmp[q,:] = dists[a[q]-1]
for p in range(n):
    max_dists[p] = min(tmp[:,p])
print(max(max_dists))
