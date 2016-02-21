# -*- coding: utf-8 -*-
"""
Created on Mon Feb  1 14:43:30 2016

@author: davekensinger
"""

import pandas as pd
import numpy as np
import pprint as pp

xlsx = pd.ExcelFile("/Users/davekensinger/Downloads/automate_online-materials/censuspopdata.xlsx")
sheet1 = xlsx.parse(0)

pivot_census = pd.pivot_table(sheet1, index=["State", "County"], values=["POP2010"], aggfunc=[np.sum, len])

pp.pprint(pivot_census)