n,q,x = map(int,input().split())
w = list(map(int,input().split()))
k = [int(input())for _ in range(q)]
w_sum = []

for i in range(n):
    if i == 0:
        w_sum.append(w[i])
    else:
        w_sum.append(w_sum[i-1] + w[i])
dp = []
division = x // w_sum[-1]
if(division > 0):
    x = x % w_sum[-1]

for i in range(n):
    count = division*n
    tmp_sum = 0
    tmp_count = 0
    j = i
    while tmp_sum < x:
        tmp_sum  =tmp_sum+ w[j%n]
        j = j+1
    count  = count + j-i
    dp.append(count)
    
print(dp)
for q in k:
    print(dp[q%n])