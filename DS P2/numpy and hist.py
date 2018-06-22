# -*- coding: utf-8 -*-
"""
Created on Fri May 25 12:05:56 2018

@author: user
"""

import numpy as np


x = np.array([[1, 2, 3], [4, 5, 6]])

print type(x)
print x.shape
print x.dtype


#-----------------------------------------------------------------------------
# Numpy supports all data types likes bool, integer, float, complex etc.
# They are defined by the numpy.dtype class 

import numpy as np 

x = np.float32(1.0) 
print x 

y = np.int_([1,2,4]) 
print y 


z = np.arange(10, dtype=np.uint8)


print z
print z.dtype


#----------------------------------------------------------------------------
"""
There are a couple of mechanisms for creating arrays in NumPy:
 a. Conversion from other Python structures (e.g., lists, tuples).
 b. Built-in NumPy array creation (e.g., arange, ones, zeros, etc.).
 c. Reading arrays from disk, either from standard or custom formats 
     (e.g. reading in from a CSV file).
"""

import numpy as np
# Converting an python list to ndarray
x = np.array([2,3,1,0])
print x
# Converting an python tuple to ndarray
x = np.array((01, 02,03))
print x

# ndarray builtin functions
# create array from scratch

# zeros(shape) -- creates an array filled with 0 values with the specified 
#                  shape. The default dtype is float64.
x = np.zeros((2, 3))
print x


# ones(shape) -- creates an array filled with 1 values. 

x = np.ones((2,3), dtype=np.int8 )
print x

# arange() -- creates arrays with regularly incrementing values.

print np.arange(10) 

#-----------------------------------------------------------------------
# linspace() -- creates arrays with a specified number of elements, 
#and spaced equally between the specified beginning and end values.

x = np.linspace(1., 4., 10)
print x





#random.random(shape) – creates arrays with random floats over the interval [0,1].
print np.random.random((2,3)) 



# Printing Arrays
import numpy as np 
a = np.arange(9) 
print a 

#reshaping it another shape
b = a.reshape(3,3) 
print b 

#another example of reshaping
c = np.arange(8).reshape(2,2,2) 
print c 

#-------------------------------------------------------------------------
"""
Arrays Operations - Basic operations apply element-wise. 
The result is a new array with the resultant elements.
Operations like *= and += will modify the existing array.
"""
a = np.arange(5) 
b = np.arange(5) 

a = [0,1,2,3,4]
b = [0,1,2,3,4]

zip(a,b)

print a+b 

print a-b 

print a**2 

print a>3 

print 10*np.sin(a) 



print a*b 

#--------------------------------------------------------------------
#Linear Algebra functions are also available

# Matrices
A = np.mat('1.0 2.0; 3.0 4.0') 
print A
print type(A) 

print A.T # transpose 

X = np.mat('5.0 7.0') 
Y = X.T
 
print A*Y # matrix multiplication 

print A.I # inverse 
print np.linalg.solve(A, Y) # solving linear equation 

#----------------------------------------
#How to check for library version
import numpy as np
print np.__version__

#---------------------------------------
# -*- coding: utf-8 -*-

"""
Mean, Median, Mode, and introducing NumPy

Mean vs. Median

Let's create some fake income data, centered around 27,000 
with a normal distribution and standard deviation of 15,000, with 10,000 data points. 
Then, compute the mean (average)
    
"""

import numpy as np

incomes = np.random.normal(27000, 15000, 10000)
np.mean(incomes)

#We can segment the income data into 50 buckets, and plot it as a histogram:

import matplotlib.pyplot as plt
plt.hist(incomes, 20)
plt.show()

#Computing Median
np.median(incomes)

#Computing Mean

np.mean(incomes)



#Adding Bill Gates into the mix. Darn income inequality!(Outliers)

incomes = np.append(incomes, [1000000000])

#Median Remains Almost SAME
np.median(incomes)


#Mean Changes distinctly

np.mean(incomes)

#---------------------------------------
#Standard Deviation

import numpy as np
import matplotlib.pyplot as plt

incomes = np.random.normal(100.0, 50.0, 10000)
#incomes = np.random.normal(27000.0, 15000.0, 10000)
plt.hist(incomes, 50)
plt.show()

print incomes.std()
print incomes.var()
#The standard deviation is the square root of the variance.