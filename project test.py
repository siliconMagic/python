# -*- coding: utf-8 -*-
"""
Created on Sat Feb 21 19:55:58 2015

@author: davekensinger
"""

import itertools

L = ['A', 'B', 'C', 'D', 'E', 'F', 'G']
for hand in itertools.combinations(L,4):
    print(hand)
