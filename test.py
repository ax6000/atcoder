import sys
def step1(menu):
	#number, stock, price
	orders = []
	for l in sys.stdin.readlines():
		if(l == ''):
			break
		S,T,D,N = l.split()
		T = int(T)
		D = int(D)
		N = int(N.rsplit()[0])
		set_order(menu,T,D,N)

def set_order(menu,T,D,N):
	if D in menu and menu[D][0] >= N:
		menu[D][0] = menu[D][0] - N
		for i in range(N):
			print('received order ' + str(T) +' '+ str(D))
	elif menu[D][0] < N:
		print('sold out '+ str(T))
	else:
		print('unexpected input')

def step2(K,menu):
	wait_table = []
	micros = []
	for l in sys.stdin.readlines():
		if(l == ''):
			break
		S = l.split()[0]
		if S == 'order':
			T,D,N = l.split()[1:]
			T = int(T)
			D = int(D)
			N = int(N.rsplit()[0])
			set_order(menu,T,D,N)
			if len(micros) < K:
				micros.append(D)
				print(str(D))
			else:
				wait_table.append(D)
				print('wait') 
		elif S == 'complete':
			D = int(l.split[1])
			if not (D in wait_table or D in micros):
				print('unexpected input')
				continue
			if len(wait_table) == 0:
				print('ok')
				micros.remove(D)
			else:
				print('ok' + str(wait_table.pop(0))
				micros.append(D)
		else:
			return

def main():
	step = int(input())
	if step == 1:
		M = int(input())
	else:
		M,K = map(int,input().split())
	menu = {}
	for i in range(M):
		ary = list(map(int,input().split()))
		menu[ary[0]] = ary[1:]

	if step == 1:
		step1(menu)
	elif step == 2:
		step2(K,menu)

if __name__ == '__main__':
	lines = []
	main()
