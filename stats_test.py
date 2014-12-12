# -*- coding: utf-8 -*-
"""
Created on Thu Nov  6 10:00:12 2014

@author: davekensinger
"""

import statsmodels as sm

def stats(n,m):
    '''n is a list of integers, m is a float
    returns sd of n raised to the m'''
    
    return sm.sdev(n)**m
    
print(stats([2,3,4,5],2))
