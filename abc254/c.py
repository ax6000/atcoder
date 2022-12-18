from http.client import FOUND
import numpy as np
def is_ascending(ary):
    min = 0
    for n in ary:
        if(min > n):
            return 0
        min = n
    return min

n,k = map(int, input().split())
a = list(map(int, input().split()))
ascending = is_ascending(a)
doable = True
if not ascending:
    a_sorted = sorted(a,reverse=True)
    a_rank = list()
    rank = 0
    rank_prev = 0
    count = 1
    rank_ary = []
    a_rank.append(rank)
    for i in range(1,len(a_sorted)):
        if(a[i-1] < a[i]):
            rank = rank + count
            rank_ary.append(rank - rank_prev)
            rank_prev = rank
            count = 0
        a_rank.append(rank)
        count = count + 1
    a_ranked = []
    for p in a:
        for q in range(a):
            if p == a_sorted[q]:
                a_ranked.append(a_rank[q])
    ary = np.empty((k,0))
    for i in range(len(a_ranked)):
        ary[i%k].append(a_ranked[i])

    ary.sort()
    for rank in rank_ary:
        for i in range

    for i in range(len(a_sorted)):
        current_rank = a_rank[i]
        tmp_flg = False
        while(a_rank[i] == current_rank and i < len(a)):
            if(current_rank % k == a_rank[i] % k):
                tmp_flg == True
            i = i+1
        if not(tmp_flg):
            doable = False
            break
# if k >= n and not ascending:
#     doable = False
# elif k < n:
# seaching = a[n-k-1:]
# searching_min = is_ascending(seaching)
# if searching_min >  0:
#     if max(a[:n-k]) > searching_min:
#         doable = False
# else:
#     doable = False     

if(doable):
    print("Yes")
else:
    print("No")