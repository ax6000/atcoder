#!/usr/bin/env python3
import numpy as np
import itertools

def main():
    S = list(input())
    T = list(input())
    s_len = len(S)
    t_len = len(T)
    dif_len = s_len - t_len
    # print(S,T,t_len)
    wildcard_s = [c == '?' for c in S]
    wildcard_t = [c == '?' for c in T]
    #x, current (0 = padding)
    # dp = [[False for _ in range(t_len+1)] for _ in range(t_len+1)]
    dp1 = [False for _ in range(t_len+1)]
    dp2 = [False for _ in range(t_len+1)]
    # dp[0][0] = True
    dp1[0] = True
    dp2[0] = True
    for i in range(t_len):
        dp1[i+1] = dp1[i] and (wildcard_t[i] or wildcard_s[i] or T[i] == S[i]) 
    for i in range(t_len):
        dp2[i+1] = dp2[i] and (wildcard_t[-i-1] or wildcard_s[-i-1] or T[-i-1] == S[-i-1]) 

    # for i in range(t_len):
    #     for j in range(t_len):
    #         if j <= i:
    #             dp[i+1][j+1] = dp[i][j] and (wildcard_t[j] or wildcard_s[j] or T[i] == S[j]) 
    #         else:
    #             dp[i+1][j+1] = dp[i][j] and (wildcard_t[i] or wildcard_s[dif_len+j-i] or T[i] == S[dif_len+j-i])
    for i in range(t_len+1):
        if dp1[i] and dp2[-i-1]:
            print("Yes")
        else:
            print("No")
    # print(dp1)
    # print(dp2)
    pass


if __name__ == '__main__':
    main()