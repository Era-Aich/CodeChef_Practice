# -*- coding: utf-8 -*-
"""
Created on Mon Feb 13 08:47:35 2023

@author: asus
"""

t=int(input())


for i in range(0,t):
    x,y=map(int,input().split())
    if(x*3)>=(y*2):
        print(y*2)
    else:
        print(x*3)