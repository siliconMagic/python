# -*- coding: utf-8 -*-
"""
Created on Wed Jan 27 20:42:33 2016

@author: davekensinger
"""

from openpyxl import load_workbook

wb2 = load_workbook('/Users/davekensinger/Desktop/pubhub_titles.xlsx')
print(wb2.get_sheet_names())
