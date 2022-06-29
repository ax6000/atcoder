# N, M = map(int, input().split())
# G = [[] for i in range(N)]
from queue import Queue

n = int(input())
x = np.array(list(map(int, input().split())))
c = np.array(list(map(int, input().split())))

ary = [0] * n

for i in range[n]:
	ary[x[i]-1] = ary[x[i]-1]+c[i]

ary_s = sorted(ary)

# 各頂点が何手目に探索されたか
# -1 は「まだ探索されていない」ことを表す
dist = [-1] * N

# todo リストを表すキュー
que = Queue()

# 頂点 0 を始点とする
dist[0] = 0
que.put(0)

score = 0
# キューが空になるまで探索する
while not que.empty():
    # キューから頂点を取り出す
    v = que.get()

    # 頂点 v から 1 手で行ける頂点 next_v を探索
    for i in range(n):
        # 頂点 next_v が探索済みであれば何もしない
        if dist[i] != -1:
            continue

        # 頂点 next_v を探索する
        dist[i] = dist[v] + 1
        que.put(i)     
        score = score + ary_s[i] 

