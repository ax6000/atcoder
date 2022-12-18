N,M,K = map(int,input().split())
# remaining cell : dice
dp = [[-1]*M]*N 
for i in range(N):
    for j in range(M):
        count = i+1 - (j+1)
        if count < 0:
            count = -count
        dp[i][j] = count

dp_p = [[[-1]*2]*M]*N
