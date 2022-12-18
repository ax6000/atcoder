#!/usr/bin/env python3

from scipy import special
from collections import defaultdict


class UnionFind():
    def __init__(self, n):
        self.n = n
        self.parents = [-1] * n

    def find(self, x):
        if self.parents[x] < 0:
            return x
        else:
            self.parents[x] = self.find(self.parents[x])
            return self.parents[x]

    def union(self, x, y):
        x = self.find(x)
        y = self.find(y)

        if x == y:
            return

        if self.parents[x] > self.parents[y]:
            x, y = y, x

        self.parents[x] += self.parents[y]
        self.parents[y] = x

    def size(self, x):
        return -self.parents[self.find(x)]

    def same(self, x, y):
        return self.find(x) == self.find(y)

    def members(self, x):
        root = self.find(x)
        return [i for i in range(self.n) if self.find(i) == root]

    def roots(self):
        return [i for i, x in enumerate(self.parents) if x < 0]

    def group_count(self):
        return len(self.roots())

    def all_group_members(self):
        group_members = defaultdict(list)
        for member in range(self.n):
            group_members[self.find(member)].append(member)
        return group_members

    def __str__(self):
        return '\n'.join(f'{r}: {m}' for r, m in self.all_group_members().items())


N,M = map(int,input().split())
# lines = [[False for _ in range(N)] for _ in range(N)]
query = []
uf = UnionFind(N*2)    
for _ in range(M):
    u_,v_ = map(int,input().split())
    #2の頂点を用意
    #各色で塗ることに対応
    #その最初の2つの頂点がsameなら２部グラフではない
    uf.union(u_-1,v_+N-1)
    uf.union(u_+N-1,v_-1)
    query.append([u_-1,v_-1])

# print(lines)
# print(uf)
# 連結でないとrootが分かれて存在
# 各連結部分において2部グラフか判定する
for r in uf.roots():
    # print(r)
    if r >=N:
        r -= N 
    if uf.same(r,r+N):
        print(0)
        quit()


ans = N*(N-1)//2

members = uf.all_group_members()
# print(members)
for l in members.values():
    cnt = len(l)
    for i in l:
        if i >= N:
            cnt -=1
    ans -= cnt * (cnt-1)/2


# print(ans,cntg2,cntg1)
# print(g1)
# print(g2)

# ans -= special.comb(cntg1,2) + special.comb(cntg2,2)

# print(ans)
# ans = cntg1*cntg2
for i in query:
    if not uf.same(i[0],i[1]):
        ans-=1

print(int(ans))