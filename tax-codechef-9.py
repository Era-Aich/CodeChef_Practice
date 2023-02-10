# -*- coding: utf-8 -*-
"""
Created on Fri Feb 10 20:04:49 2023

@author: asus
"""
'''
T=int(input())
for i in range(0,T):
    total=int(input())
    if(total<=100):
        print(total)
    else:
        total=total-10
        print(total)
'''

def tax(total):
    
    if(total<=100):
        return total
    else:
        total=total-10
        return total
        
t=int(input())
for i in range (0,t):
    total=int(input())
    
    y= tax(total)
    print(y)