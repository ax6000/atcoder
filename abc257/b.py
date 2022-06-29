n, k, q = map(int, input().split())
a = list(map(int, input().split()))
l = list(map(int, input().split()))

for i in l:
	if a[i-1] == n:
		continue
	if i == k:
		a[i-1] = a[i-1] + 1
	elif a[i] - a[i-1] > 1 :
		a[i-1] = a[i-1] + 1
print(*a)
