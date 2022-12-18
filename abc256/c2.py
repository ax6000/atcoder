import numpy as np

n = int(input())
s = np.array(list(input()))
w = np.array(list(map(int,input().split())))

# a = []
# c = []
# for i in range(n):
#     if s[i] == '0':
#         c.append(w[i]) 
#     else:
#         a.append(w[i])

# dp = [0]*n
# w.sort()
# c.sort()
# a.sort()
arg = w.argsort()

s = s[arg]

w.sort()
print(*s)
cnt = 0
max_cnt = 0
for i in s:
    if i == '1':
        cnt = cnt + 1
max_cnt = cnt
# 0|000001010
# 
for i in s:
    if i == '0':
        cnt = cnt+1
    else:
        cnt = cnt -1
    max_cnt = max(cnt,max_cnt)

print(str(max_cnt))