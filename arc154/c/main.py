#!/usr/bin/env python3
import numpy as np
import itertools

def main():
    T = int(input())
    for _ in range(T):
        N = int(input())
        A = list(map(int,input().split()))
        A.append(A[0])
        B = list(map(int,input().split()))
        B.append(B[0])
        a_single = {}
        b_single = {}
        # b_loc = {}
        # for i in range(N-1,-1,-1):
        #     # a_single[A[i]] = i
        #     # b_single[B[i]] = i
        #     if B[i] in b_loc:
        #         b_loc[B[i]].append(i)
        #     else:
        #         b_loc[B[i]] = [i]
            
        #     if A[i] in b_loc:
        #         b_loc[A[i]].append(-i-1)
        #     else:
        #         b_loc[A[i]] = [-i-1]
        a_match = []
        for i in range(N):
            for j in range(N):
                if A[i] == B[j]:
                    match = [i,j]
                    a_match.append(match)
                    break
        it = itertools.permutations(a_match)
        flg = False
        for i in it:
            if len(i) == 0:
                # print("No")
                break
            flg = True
            covered = [-1,50001]
            for j in i:
                # print(j,covered)                
                if j[0] <= covered[0] or j[0]>=covered[1]:
                    flg = False
                    break
                if j[1] == j[0]:
                    pass
                if j[1] > j[0]:
                    covered[0] = max(covered[0],j[0])
                    covered[1] = min(covered[1],j[1])
                else:
                    covered[0] = max(covered[0],j[1])
                    # covered[1] = min(covered[1],j[1]) 
            if flg:
                break
        if flg:
            print("Yes")
        else:
            print("No")

                

        # print(l)


if __name__ == '__main__':
    main()