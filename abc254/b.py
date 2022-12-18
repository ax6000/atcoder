import numpy as np

n = int(input())
ary = np.zeros((30,31))
for i in range(n):
    ary[i,0] = 1
    ary[i,i] = 1
    for j in range(1,i,1):
        ary[i,j] = ary[i-1,j-1]+ ary[i-1,j]

for i in range(30):
    if(ary[i,0] == 0):
        break
    for j in range(30):
        if(ary[i,j] >= 1):
            print(int(ary[i,j]),end='')
        if(ary[i,j+1] != 0):
            print(' ',end='')
        else:
            print()
            break