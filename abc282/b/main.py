#!/usr/bin/env python3

N,M = map(int,input().split())
S = [input() for _ in range(N)]
ans = 0
for i in range(N):
    q = S[i]
    for j in range(0,i):
        q2 = S[j]
        flg = True
        if i == j:
            continue
        for m in range(M):
            if q[m] == 'x' and q2[m] == 'x':
                flg = False
                break
        if flg:
            ans += 1
print(ans)