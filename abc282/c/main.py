#!/usr/bin/env python3
N = int(input())
S = input()
s2 = [] 

is_txt = False 
for i,c in enumerate(S):
    # print(is_txt)
    if c == "\"":
        is_txt = not is_txt
    if not is_txt and c == ',':
        s2.append('.')
    else:
        s2.append(c)
        
s3 = ''.join(s2)
print(s3)




