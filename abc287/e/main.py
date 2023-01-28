#!/usr/bin/env python3
import numpy as np
import itertools
import sys 
sys.setrecursionlimit(10**6)

def pair_search(ary):
    for a in ary:
        if len(a) >=2:
            return True
    return False 

def sort_a(n,ary,result):
    alp = [[] for _ in range(26)]
    # print(alp)
    for i in ary:
        # print(S[i][n])-ord('a'))
        try:
            alp[ord(S[i][n])-ord('a')].append(i)
        except IndexError:
            result[i] = n 
            continue
    # print(n,alp)
    for i in alp:
        if len(i)>= 2:
            sort_a(n+1,i,result)
        elif len(i) == 1:
            result[i[0]] = n

def main():
    global N
    global S 
    N = int(input())
    S = [list(input()) for _ in range(N)]
    # lcp = [[0 for _ in range(N)] for _ in range(N)]
    alp = [[] for _ in range(26)]
    for i in range(N):
        alp[ord(S[i][0])-ord('a')].append(i)
    result = [0 for i in range(N)]
    # print(0,alp)
    for i in alp:
        if len(i)>= 2:
            sort_a(1,i,result)
        elif len(i)==1: 
            result[i[0]] = 0
    for i in range(N):
        print(result[i])
    pass


if __name__ == '__main__':
    main()