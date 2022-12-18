def bit(l,s):
    for i,c in enumerate(s):
        if c == '#':
            l[i] = l[i] | 0b1
            l[i] = l[i] << 1

H,W = map(int,input().split())
S = [0b0 for i in range(W)]
T = [0b0 for i in range(W)]


for i in range(H):
    s = input()
    bit(S,s)
for i in range(H):
    s = input()
    bit(T,s)
for i in range(W):
    S[i] = S[i]>>1
    T[i] = T[i]>>1
flg = True
# 4*10^5 sum 1/2n^2
S.sort()
T.sort()
# l= [i for i in range(W)]
for i in range(W):
    if S[i] != T[i]:
        flg = False
        break

#  length = len(l)
# while(len(l) > 0 and flg):
#     print(l)
#     target = l[0]
#     dest = -1
#     for j,i in enumerate(l):
#         if S[target] == T[i]:
#             if T[target] == S[i]:
#                 dest = i
#                 l.remove(target)
#                 l.remove(dest)
#                 break
#     print(k)
    # if dest == -1:
    #     flg = False
    # length = len(l)
            
# print(S)
# print(T)
if flg:
    print("Yes")
else:
    print("No")

