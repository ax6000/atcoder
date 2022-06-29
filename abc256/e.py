
import numpy as np

def dfs (now):
	for i in tree[now]
		dfs(i)

n = int(input())
x = np.array(list(map(int, input().split())))
c = np.array(list(map(int, input().split())))

ary = {}
for a in x:
	ary[a] = 0
for i in range[n]:
	ary[x[i]] = ary[x[i]]+c[i]

ary_sorted = sorted(ary.items(), key=lambda x:x[1])



arg = np.argsort(x)
x_s = x[arg]
c_s = c[arg]


count = 0
