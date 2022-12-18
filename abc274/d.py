import itertools
def search(l:list,p:int):
    plus2 = -sum(l)
    # print("plus2 = %d" % plus2)
    for i in range(N):
        comb = itertools.combinations(l,i)
        for c in comb:
            # print(c)
            tmp = plus2
            for v in c:
                tmp += v+v
            if tmp == p:
                return True 
    return False


N,x,y = map(int,input().split())
A = list(map(int,input().split()))
flg_x = False
flg_y = False
A_x =[]
A_y = []
for i,v in enumerate(A):
    if i % 2 == 0:
        A_x.append(v)
    else:
        A_y.append(v)
x -= A_x[0]
flg_x = search(A_x[1:],x)
flg_y = search(A_y,y)
# print(flg_x)
# print(flg_y)
if flg_x and flg_y :
    print("Yes")
else:
    print("No")