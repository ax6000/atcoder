import math

n,x = map(float,input().split())
print(chr(ord('A')+math.ceil(x/n)-1))
