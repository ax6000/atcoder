
import numpy as np
n = int(input())
c = np.array(list(map(int,input().split())))

x = 0

arg = c.argsort()
c_ = c[arg]

max_index = 0
for i in range(9):
    if c_[i] == c_[0]:
        max_index = max(max_index,arg[i])
# m = n
# m = m-c[i-1]
# x = 10*x + i
# print(arg)
# print(c_)
divide = n // c_[0]
# print(divide)
ans = [max_index+1]*divide
# print(ans)
n_ = n - c_[0]*divide
min_value = min(c)
c_2 = c_ - c_[0]

j = 0
while(n_ >= c_2[0] and n_  > 0):
    if(j == divide):
        break
    max__ = 0
    for i in range(9):
        if c_2[i] <= n_:
            max__ = arg[i]+1 
    ans[j] = max__
    n_ = n_ - c_2[max__-1]
    j = j+1

mod = n % c_[0]
# print(max_index)

c_max = -1
for i in range(9):
    if c[i] <= mod+c_[0]:
        c_max = i+1

# if c_max == -1:
#     print(str(max_index+1)*divide)
# else:
#     print(str(c_max)+str(max_index+1)*divide)

for c in ans:
    print(c,end="")

print('')