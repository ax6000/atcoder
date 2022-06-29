n = int(input())
a = list(map(int, input().split()))
p = 0

ary = []
ary.append(0)
for i in range(n):
	for j in range(len(ary)):
		ary[j] = ary[j] + a[i]
		if(ary[j] >= 4 and ary[j] <= 8):
			ary[j] = 100
			p = p+1
	ary.append(0)
print(p)
