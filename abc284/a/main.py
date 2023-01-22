#!/usr/bin/env python3

N  =int(input())
l = [input() for i in range(N)]
for i in range(N):
    print(l[-(i+1)])