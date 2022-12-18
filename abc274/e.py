import math
import itertools
def dist(src, dst):
    distance =math.sqrt(math.pow(src[0]- dst[0],2)+math.pow(src[1]- dst[1],2))
    return distance

t = [[0,0]]
N,M = map(int,input().split())
for _ in range(N):
    t.append(list(map(int,input().split())))
c = []
for _ in range(M):
    t.append(list(map(int,input().split())))


map_ = []
for i in range(len(t)):
    tmp = []
    for j in range(len(t)):
        if i == j:
            tmp.append(0)
        elif j < i:
            tmp.append(map_[j][i])
        else:
            tmp.append(dist(t[i],t[j]))
    map_.append(tmp)

query = [i+1 for i in range(N)]
query_c = [i+1+N for i in range(M)]
min_ = 1000000000
for i in range(M+1):
    comb = itertools.combinations(query_c,i)
    for c in comb:
        for lst in itertools.permutations(query+list(c)):
            # print(query+list(c))
            t = 0
            q_old = 0
            boost = 1
            for q in lst:
                t += map_[q_old][q]/boost
                if q > N:
                    boost *= 2
                q_old = q
            t += map_[q_old][0]/boost       
            min_ = min(min_,t)
print(min_)