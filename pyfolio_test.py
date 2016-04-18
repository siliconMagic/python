# -*- coding: utf-8 -*-
"""
Created on Tue Mar  1 22:42:21 2016

@author: davekensinger
"""

import pyfolio as pf

rets = pf.utils.get_symbol_rets('DIS')

pf.create_returns_tear_sheet(rets[-756:])