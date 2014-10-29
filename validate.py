# -*- coding: utf-8 -*-
"""
Created on Wed Oct  8 08:52:09 2014

@author: davekensinger
"""

def validate(n):
    '''n is an positive integer of up to 16 digits'''
    
    lst = [int(d) for d in str(n)][::-1]
    double = []
    for i,x in enumerate(lst):
        if i % 2:
            if x*2 > 9: d = x*2 - 9
            else: d = x*2
            double.append(d)
        else:
            double.append(x)
    return (sum(double) % 10 == 0)
    
print(validate(54212933543239))