import numpy as np

n = int(input())
ary = np.empty((n,2))
for i in range(n):
	l_,r_ = map(int,input().split())
	ary[i,0] = l_
	ary[i,1] = r_


sorted_ary = ary[np.lexsort((ary[:,1],ary[:,0]))]
# print(ary)
# print(sorted_ary)
i = 0
# m = max(ary[:,1])
for i in range(n):
	if(i == 0):
		l = sorted_ary[0,0]
		r = sorted_ary[0,1]

	if(sorted_ary[i,0] > r):
		print(str(int(l))+' '+str(int(r)))
		l = sorted_ary[i,0]
		r = l+1
		# print(str(i)+"[0]:yes ",end="")
	# else:
		# print(str(i)+"[0]:no ",end="")

	if(sorted_ary[i,1] > r):
		r = sorted_ary[i,1]
		# print(str(i)+"[1]:yes")
	# else:
		# print(str(i)+"[1]:no")
	# print("l: "+str(int(l))+" r: "+str(int(r)))
print(str(int(l))+' '+str(int(r)))
