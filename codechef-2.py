# -*- coding: utf-8 -*-
"""
Created on Wed Jan 25 09:35:45 2023

@author: asus
"""

n=int(input("Enter the total input"))

print("Enter the input: ")
for i in range(n):
   x,y,a=map(int,input().split())
   if a>=x and a<y:
       print("YES")
   else:
        print("NO")
       
   
    