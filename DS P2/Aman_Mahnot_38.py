# -*- coding: utf-8 -*-
"""
Created on Fri May 25 12:08:03 2018

@author: user
"""

import numpy as np
import matplotlib.pyplot as plt
data = np.random.normal(150.0,20.0,1000)
plt.hist(data,100)
plt.show()
print "standard deviation is:",data.std()
print "variance is",data.var()