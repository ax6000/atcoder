#!/usr/bin/env python3

import math
T = int(input())
for _ in range(T):
    N = int(input())
    left = 2
    right = int(math.sqrt(N))+1
    for mid in range(left,right+1):
        if N % mid == 0:
            if N // mid % mid == 0:
                print(mid,N//mid//mid)
            else:
                print(int(math.sqrt(N//mid)),mid)
            break

