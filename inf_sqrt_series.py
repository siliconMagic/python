#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Feb 22 10:56:45 2018

@author: davekensinger
"""

def inf_sqrt(n):
    total = 0
    for integer in range(n+1):
#        print(integer)
        result = 0
        for n in range(40):
            result = integer + result**0.5
#            print(result)
#        print(integer, result)
        if result%1 < 0.000001:
            print(integer, result**0.5)
            total += 1
    print(total)