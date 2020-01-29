# -*- coding: utf-8 -*-
"""
Created on Mon Jan 27 19:04:39 2020

@author: Administrator
"""

def numpat(n):
    num = 1
    for i in range(0, n):
        num = 1
        for j in range(0, i+1):
            print(num, end=" ")
            num = num + 1
        print("\r")
        
n=5
numpat(n)
