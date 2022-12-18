n,q = map(int,input().split())
s = input()
query = []
for i in range(q):
    tmp = tuple(map(int,input().split()))
    query.append(tmp)
# s_r = s[::-1]
# print(s_r)
count = 0
for q_ in query:
    if q_[0] == 1:
        count = count + q_[1]
    else:
        mod = count % n
        if mod == 0: 
            print(s[q_[1]%n-1])
        # print(str(count)+' '+str(count // n % 2))
        # if count // n % 2 == 1:
            # completely reversed
        # elif q_[1]% n  <= mod:
        #     s = s[-mod:]
        #     print(s[q_[1]%n-1])
        else:
            print(s[q_[1]-mod-1])
        # else:
        #     if q_[1] <= mod:
        #         s_r = s_r[-mod:]
        #         print(s_r)
        #         print(s_r[q_[1]-1])
        #     else:
        #         print(s[q_[1]-mod-1])