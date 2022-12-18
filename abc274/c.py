N = int(input())
A = list(map(int,input().split()))
dp = [0]*(2*N+1)
for i,a in enumerate(A):
    i +=1
    dp[i*2-1] = dp[a-1]+1
    dp[2*i] = dp[a-1]+1

for v in dp:
    print(v)