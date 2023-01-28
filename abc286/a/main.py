#!/usr/bin/env python3
import numpy as np
import itertools

def main():
    N = int( input())
    half = N //2
    cnt = 0
    for i in range(N):
        if input() == "For":
            cnt += 1
    if cnt > half:
        print("Yes")
    else:
        print("No")
    pass


if __name__ == '__main__':
    main()