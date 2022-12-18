import math

def xd (t,A,B):
    if t == -1:
        return -1
    else:
        return B*t+ (A/math.sqrt(1+t))
A,B=map(int,input().split())

log_t = (math.log(A)-math.log(B*2))
flg = log_t < 0
log_t *= 2.0
log_t /= 3.0
t1 = math.ceil(math.exp(log_t))-1 
t2 = math.floor(math.exp(log_t))-1
t11 = xd(t1,A,B)
t22 = xd(t2,A,B)
if t11 == -1:
    t11 = t22
elif t22 == -1:
    t22 = t11

print('%.10f' % min(t11,t22))

# t^3/2 = A/2B

# log(t) = 2/3(log(B)-log(A)