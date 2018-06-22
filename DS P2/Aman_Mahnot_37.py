# -*- coding: utf-8 -*-
"""
Created on Fri May 25 11:41:44 2018

@author: user
"""

import numpy as np
import matplotlib.pyplot as plt
incomes = np.random.normal(100.0,20.0,10000)


#np.min(incomes)
#np.max(incomes)


print np.mean(incomes)
print np.median(incomes)
plt.hist(incomes,100)
plt.show()
incomes = np.append(incomes,[100000000])


print np.mean(incomes)
print np.median(incomes)
plt.hist(incomes,100)
plt.show()