# -*- coding: utf-8 -*-
"""
Created on Sun Jan 10 16:58:00 2016

@author: davekensinger
"""

setA = {"hello", "hel", "lo"}
for item in setA:
    setB = setA.difference({item})
    for root in setB:
        if root.endswith(item):
            return True
    return False

    
