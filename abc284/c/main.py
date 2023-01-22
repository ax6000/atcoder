#!/usr/bin/env python3

def dfs(i,g,g_seen):
    g_seen[i] = True
    for n in g[i]:
        if not g_seen[n]:
            dfs(n,g,g_seen)


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
for i in range(N):
    if not g[i]:
        cnt +=1
        dfs(i,g,g_seen)
print(cnt)