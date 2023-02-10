# -*- coding: utf-8 -*-
"""
Created on Fri Feb 10 19:35:36 2023

@author: asus
"""



t  = int(input())
for i in range(t):
    x, n =map(int,input().split())
    print(int((x/10)*n))