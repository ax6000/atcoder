#!/usr/bin/env python3
import numpy as np
import itertools

def is_equal(a,b):
    an = [0 for _ in range(26)]
    bn = [0 for _ in range(26)]
    for i in range(N):
        an[ord(a[i])-ord('a')]+=1
        bn[ord(b[i])-ord('a')]+=1
    return an == bn

def main():
    global N 
    N = int(input())
    S = list(input())
    T = list(input())
    if not is_equal(S,T):
        print(-1)
        return
    flg = True
    target = N-1
    point = N-1
    len = 0
    while target >= 0 and point >= 0:
        while T[target] != S[point] and target > 0:
            target-=1
        if T[target] != S[point]:
            break
        point -=1
        target -=1 
        len +=1
    print(N-len)
if __name__ == '__main__':
    main()