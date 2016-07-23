#! /Users/davekensinger/anaconda/bin/python3
# -*- coding: utf-8 -*-
"""
Created on Sun Jul 17 22:09:38 2016

@author: davekensinger
"""

import sys
from PIL import Image

for f in sys.stdin:
    print(f)
    im = Image.open(f)
    w, h = im.size
    w = w / 300 * 2.54
    h = h / 300 * 2.54
    im.thumbnail((256, 256))
    im.save("/__" + f + " ({0:.2f} x {1:.2f} cm)".format(w, h) + ".jpeg", "JPEG")

