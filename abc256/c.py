
h1,h2,h3,w1,w2,w3 =  map(int, input().split())

count = 0
for tl in range(1,31,1):
	for tc in range(1,31,1):
		for ml in range(1,31,1):
			for mc in range(1,31,1):
				tr = h1-tl-tc
				mr = h2-ml-mc
				bl = w1-tl-ml
				bc = w2-tc-mc
				br = h3- bl-bc
				br_w = w3-mr-tr
				if br==br_w and tr > 0 and mr > 0 and bl > 0 and bc > 0 and br > 0 and br > 0:
					count = count + 1
print(count)
