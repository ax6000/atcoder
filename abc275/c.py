import itertools
def is_square(p1,p2,p3,p4):
    d1_2 = manhattan(p1,p2) 
    d2_3 = manhattan(p2,p3)
    d3_4 = manhattan(p3,p4)
    d4_1 = manhattan(p4,p1)
    
    #[x,y]
    if d1_2[0] != d2_3[1] or d1_2[1] != -d2_3[0]:
        return False

    if d2_3[0] != d3_4[1] or d2_3[1] != -d3_4[0]:
        return False    
    
    if d3_4[0] != d4_1[1] or d3_4[1] != -d4_1[0]:
        return False   
    # print(p1,p2,p3,p4,d1_2,d2_3,d3_4,d4_1)
    return True

def manhattan(p1,p2):
    return(p2[0]-p1[0],p2[1]-p1[1])


s = []
for i in range(9):
    s.append(input())
a = []
pawnxy = []
for i in range(9):
    for j in range(9):
        if s[i][j] == "#":
            pawnxy.append((i,j))

comb = itertools.permutations(pawnxy,4)
ans = 0
for i in comb:
    # print(i)
    if is_square(*i):
        ans += 1
print(ans//4)
