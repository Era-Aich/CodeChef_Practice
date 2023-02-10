# -*- coding: utf-8 -*-
"""
Created on Fri Feb 10 19:59:10 2023

@author: asus
"""

T=int(input())

for i in range(0,T):
    x,y=map(int,input().split())
    z=y-x
    
    print(z)