#!/usr/bin/env python3
import numpy as np
import itertools

def flip(A,a1,a2):
    try:
        tmp = A[a1]
        A[a1] = A[a2]
        A[a2] = tmp
    except IndexError:
        print(a1,a2)


def print_p(A,pos,W):
    for i,p in enumerate(pos):
        print(A[p[0]][p[1]],end="")
        if i % W == W-1:
            print()

def manual_flip(A,query,H,W):
    for q in query:
        a = q[0]-1
        b = q[1]-1
        R1 = [0,W*a+b]
        R2 = [q[0],W*q[0]-1]
        R3 = [W*q[0],W*(H-1)+b]
        R4 = [W*q[0]+q[1],W*H-1]
        print(len(A),R1,R2,R3,R4)
        for i in range(H*W):
            if i % W <= b:
                if i // W <= a:
                    flip(A,i,R1[1]-(i-R1[0]))
                else:
                    flip(A,i,R3[1]-(i-R3[0]))
            else:
                if i // W <= a:
                    flip(A,i,R2[1]-(i-R2[0]))
                else:
                    flip(A,i,R4[1]-(i-R4[0]))
        # b行目：ぎょうは

def main():
    H,W = map(int,input().split())
    A = [list(input()) for _ in range(H)]
    pos = []
    for i in range(H):
        for j in range(W):
            pos.append([i,j])  
    Q = int(input())
    query = [list(map(int,input().split())) for _ in range(Q)]
    manual_flip(pos,query,H,W)
    for i,p in enumerate(pos):
        print(A[p[0]][p[1]],end="")
        if i % W == W-1:
            print()
        

    pass


if __name__ == '__main__':
    main()