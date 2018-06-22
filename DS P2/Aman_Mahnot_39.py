# -*- coding: utf-8 -*-
"""
Created on Fri May 25 12:19:45 2018

@author: user
"""
#Answer 1
import numpy as np
arr = np.random.randint(5,15, size = (40))
#with numpy
print np.argmax(np.bincount(arr))
#without numpy

