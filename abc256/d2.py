import numpy as np

n = int(input())
x = [0]*n
y = [0]*n
p = [0]*n
for i in range(n):
    x_,y_,p_ = map(int,input().split())
    x[i] = x_
    y[i] = y_
    p[i] = p_

dp = np.zeros((n,2))
