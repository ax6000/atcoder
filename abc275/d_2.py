
DP = 100000
N = int(input())
dp = {}

def f(k):
    global dp
    if k in dp:
        return dp[k] 
    if k == 0:
        return 1
    ans = f(k//2) + f(k//3)
    if not k in dp:
        dp[k] = ans 
    return(ans)

print(f(N))