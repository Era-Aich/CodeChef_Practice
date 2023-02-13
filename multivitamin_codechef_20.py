# -*- coding: utf-8 -*-
"""
Created on Mon Feb 13 09:06:39 2023

@author: asus
"""

t=int(input())
for i in range(0,t):
    x,y=map(int,input().split())
    if(y>=3*x):
        print("YES")
    else:
        print("NO")