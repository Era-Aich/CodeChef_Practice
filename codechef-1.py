# -*- coding: utf-8 -*-
"""
Created on Sat Jan 21 16:52:30 2023

@author: asus
"""
n=int(input("Enter the total input"))
for i in range(n):
    x,y=map(int,input().split())
    if x>=10:
        print("Yes")
    else:
        print("NO")