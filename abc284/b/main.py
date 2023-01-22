#!/usr/bin/env python3
T = int(input())
for _ in range(T):
    N = int(input())
    A = list(map(int,input().split()))
    a = 0
    for i in A:
        if i % 2 == 1:
            a += 1
    print(a)