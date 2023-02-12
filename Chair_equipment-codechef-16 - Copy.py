# -*- coding: utf-8 -*-
"""
Created on Sun Feb 12 22:42:33 2023

@author: asus
"""

def chair(m,n):
    if(m>n):
        z=m-n
        return z
    else:
        return 0
    
t=int(input())
for i in range(0,t):
    m,n=map(int,input().split())
    x=chair(m,n)
    print(x)