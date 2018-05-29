#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Apr 11 18:00:22 2018

@author: davekensinger
"""

from itertools import permutations

for p in permutations('123456789'):
    s  = ''.join(p)
    l = list(s)
    [A,B,C,D,E,F,G,H,P] = l
    if int(A+B) - int(C+D) == int(E+F) and int(E+F)+int(G+H) == int(P+P+P):
        print(int(A)+int(B)+int(C)+int(D))
        