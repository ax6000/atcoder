N = int(input())
ans = 0
queue = []
queue.append(N//2)
queue.append(N//3)
for 
dp = {}


def f(k):
    if k == 0:
        return 1
    return(f(k//2)+f(k//3))
print(f(1000000000000000000))
same = 0
while(len(queue) != 0):
    for i in range(len(queue)):
        tmp = queue.pop()
        if tmp in dp:
            t_2 = dp[tmp][0]
            t_3 = dp[tmp][1]
        else: 
            t_2 = tmp // 2
            t_3 = tmp // 3
            dp[tmp] = (t_2,t_3)

        if t_2 == 0:
            ans += 1
        else:
            queue.append(t_2)
        if t_3 == 0:
            ans += 1
        else:
            queue.append(t_3)
print(ans)
