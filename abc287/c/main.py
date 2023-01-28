#!/usr/bin/env python3
import numpy as np
import itertools
import sys 
sys.setrecursionlimit(10**6)

def dfs(i,g,g_seen):
    g_seen[i] = True
    for n in g[i]:
        if not g_seen[n]:
            dfs(n,g,g_seen)


def main():
    N,M = map(int, input().split())
    G = [[] for _ in range(N)]
    for _ in range(M):
        u,v = map(int, input().split())
        u-=1
        v-=1
        G[u].append(v)
        G[v].append(u)
    single_count = 0
    flg = True
    cnt = 0
    g_seen = [False for _ in range(N)]
    for i in range(N):
        if not g_seen[i]:
            cnt +=1
            dfs(i,G,g_seen)

    if cnt != 1:
        flg = False
    else:
        for n in G:
            l = len(n)
            if l > 2:
                # print("sex")
                flg = False
                break
            elif l == 1:
                single_count += 1
        if single_count != 2:
            # print(single_count)
            flg = False
    # print(G,cnt,single_count)
    if flg:
        print("Yes")
    else:
        print("No")

if __name__ == '__main__':
    main()