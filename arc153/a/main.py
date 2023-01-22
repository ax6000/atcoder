#!/usr/bin/env python3
import numpy as np
import itertools

# 123456789
# 11xx557x7#
# 1xx57x#
# 
def digit_extract(n,i):
    return n  % (10**(i+1)) // (10**i)
  
def main():
    N = int(input())
    N -= 1
    zero = 110000000
    n_digit = [digit_extract(N,5-i) for i in range(6)]
    # print(n_digit)
    zero += n_digit[0] * (10**8)
    zero += n_digit[0] * (10**7)
    zero += n_digit[1] * (10**6)
    zero += n_digit[2] * (10**5)
    zero += n_digit[3] * (10**4)
    zero += n_digit[3] * (10**3)
    zero += n_digit[4] * (10**2)
    zero += n_digit[5] * (10**1)
    zero += n_digit[4] * (10**0)
    print(zero)
    pass


if __name__ == '__main__':
    main()