n,x = map(int,input().split())
t = []
for i in range(n):
    tmp = tuple(map(int,input().split()))
    t.append(tmp)

# saitan a(k) (x-k)*t[k][1] + sum(t[l][0]+t[l][1]) 
sum_ = []
sum_once = []

for i in range(n):
    if i == x:
        break 
    if i == 0:
        sum_once.append(t[i][0]+t[i][1])
    else:
        sum_once.append(sum_once[i-1] + t[i][0]+t[i][1])
    
    remaining = x-(i+1)
    sum_.append(sum_once[i]+ t[i][1]*remaining)

# print(sum_)
sum_.sort()
print(sum_[0])
