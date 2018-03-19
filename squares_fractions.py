#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Feb  9 17:12:24 2018

@author: davekensinger
"""
bucket = range(1,30)
candidates = [(a,b,c,d) for a in bucket for b in bucket for c in bucket for d in bucket if 1/a + 1/b + 1/c + 1/d == 1 and len(set([a,b,c,d])) == 4]
numbers = [a**2 + b**2 + c**2 + d**2 for a,b,c,d in candidates]
print(min(numbers))