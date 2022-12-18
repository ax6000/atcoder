x,a,d,n = map(int, input().split())
tmp = a + (d*(n-1))
s_max = int(max(a,tmp))
s_min = int(min(a,tmp))
if x<= s_min:
    print(int(s_min-x))
elif x >= s_max :
    print(int(x-s_max))
else:
    if(d == 0):
        print(0)
    else: 
        dif_a = a%d 
        dif_x = x%d
        print(int(min((x-s_min)%d,d-(x-s_min)%d)))
