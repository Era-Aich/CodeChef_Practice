# -*- coding: utf-8 -*-
"""
Created on Sat Feb 18 23:35:06 2023

@author: asus
"""

t=int(input())
for i in range(0,t):
    x,y=map(int,input().split())
    z=2*x
    k=5*y
    if(z>k):
       print("Chocolate")
    elif(k==z):
        print("Either")
    else:
        print("Candy")
        