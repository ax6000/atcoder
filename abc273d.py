H,W,rs,cs = map(int,input().split())
# print("done")
N  = int(input())
grid = [[0 for _ in range(W)] for _ in range(H)]
# for row in grid:
    # print(*row,sep='')
# print("done")
for _ in range(N):
    rn,cn = map(int,input().split())
    grid[rn-1][cn-1] = 1

Q = int(input())

y = rs-1
x = cs-1
for _ in range(Q):
    di,li = input().split()
    li = int(li)
    
    if di =='U':
        dx = 0
        dy = -1
    elif di == 'D':
        dx = 0
        dy = 1
    elif di == 'L':
        dx = -1
        dy = 0
    elif di == 'R':
        dx = 1
        dy = 0

    movex = dx != 0

    if movex:
        if dx < 0:
            d = 0
            for i in range(x,-1,-1):
                #find last 1
                if grid[y][i] == 1:
                    d = x-i-1
                    break
                if i == 0:
                    d = x
            # print(d)
        else:
            d = 0
            for i in range(x,W):
                if grid[y][i] == 1:
                    d = i-x-1
                    break
                if i == W-1:
                    d = W-1-x
    else:
        if dy < 0:

            d = 0
            for i in range(y,-1,-1):
                #find last 1
                if grid[i][x] == 1:
                    d = y-i-1
                    break
                if i == 0:
                    d = y
        else:
            d = 0
            for i in range(y,H):
                if grid[i][y] == 1:
                    d = i-y-1
                    break
                if i == H-1:
                    d = H-1-y
    d = min(li,d)
    x += d*dx
    y += d*dy 
    print(y+1,x+1)
