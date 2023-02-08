# -*- coding: utf-8 -*-
"""
Created on Wed Feb  8 11:29:35 2023

@author: asus
"""

T=int(input())

for i in range (T):
    x,y=map(int,input().split())
    if x==y or x<y:
        print (x)
    else:
        print (y)