# -*- coding: utf-8 -*-
"""
Created on Wed Jan 25 09:35:45 2023

@author: asus
"""

t=int(input(""))

print(" ")
for i in range(t):
   X,Y,A=map(int,input().split())
   if A>=X and A<Y:
       print("YES")
   else:
        print("NO")
       
   
    