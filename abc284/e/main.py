#!/usr/bin/env python3
import sys
sys.setrecursionlimit(10**6)

def reset(g):
    for i in range(len(g)):
        g[i] = False

from collections import deque
count = 0
def bfs(u,g,g_seen):
    queue = deque([u])
    count = 0
    while queue or count <= 1000000:
        v = queue.popleft()
        for i in g[v]:
            if not g_seen[i]:
                count +=1
                queue.append(i)
    return count
        
def dfs(i):
    if cnt >= 1000000:
        return
    count += 1
    # print(i+1,end="")
    g_seen[i] = True
    for n in g[i]:
        if not g_seen[n]:
           dfs(n)
    g_seen[i] = False
    # return cnt
N,M = map(int,input().split())
g = [[] for _ in range(N)]
for _ in range(M):
    u,v = map(int,input().split())
    u -=1
    v -=1
    g[u].append(v)
    g[v].append(u)
cnt = 0
g_seen = [False for _ in range(N)]
dfs(0)
# print(g)
print(min(count,10**6))