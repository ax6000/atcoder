#!/usr/bin/env python3
import numpy as np
import itertools

def main():
    N,M = map(int, input().split())
    S = [input()[3:] for _ in range(N)]
    T = [input() for _ in range(M)]
    cnt = 0
    for s in S:
        for t in T:
            if s == t:
                cnt +=1
                break
    print(cnt)
    pass


if __name__ == '__main__':
    main()