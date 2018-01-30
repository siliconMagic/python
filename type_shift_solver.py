#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Jan 23 11:16:05 2018

@author: davekensinger
"""
import itertools as it

DICT = '/usr/share/dict/words'

letter_rack = ['vlok','air','nirj','ayu']

dictionary = [word.strip() for word in open(DICT).readlines() if len(word) == len(letter_rack)+1]

combinations = [blob for blob in it.product(*letter_rack)]

for blob in combinations:
    word = "".join(blob)
    if word in dictionary:
        print(word)
    
#print(["".join(word) for word in combinations if "".join(word) in dictionary])