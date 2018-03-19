#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Feb  8 19:55:19 2018

@author: davekensinger
"""
import sympy as sp

count = 0

for n in range(10000000,20000000):
    str_n = str(n)
    if str_n == str_n[::-1]:
        if not sp.isprime(n):
            print(n)
            count += 1
print(count)