#!/usr/bin/env python3
import numpy as np
import itertools

def main():
    N = int(input())
    A = list(input())
    B = list(input())
    small = []
    big = []
    for i in range(N):
        small.append(min(A[i],B[i]))
        big.append(max(A[i],B[i]))
    small = int("".join(small))
    big = int("".join(big))
    print(((small % 998244353) * (big % 998244353))% 998244353)




if __name__ == '__main__':
    main()