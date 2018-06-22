# -*- coding: utf-8 -*-
"""
Created on Mon May 28 12:27:40 2018

@author: user
"""

# Example 01: Liner Relationship

import matplotlib.pyplot as plt

xs = [1,2,3,4,5]
ys = [1,2,3,4,5]

plt.plot(xs, ys)


xs = [1,2,3,4,5]
ys = [1,4,9,16,25]

plt.plot(xs, ys)


#Example o2 - Polynomial Relationship
import matplotlib.pyplot as plt

xs = [1,2,3,4,5, 6,7,8,9,10]
ys = [x**2 for x in xs]




plt.plot(xs, ys)
plt.xlabel("x-axis")



plt.ylabel("y-axis")


plt.title("Matplotlib Example")


plt.savefig("quad.png")

plt.show()

# Example 03

import numpy as np
import matplotlib.pyplot as plt

x = np.arange(0, 5, 0.1)
y = np.sin(x)
plt.plot(x, y)



#Plot function can take any number of arguments

import numpy as np 
import matplotlib.pyplot as plt 
# evenly sampled time at .2 intervals 
t = np.arange(0., 5., 0.2) 
# red dashes, blue squares and green triangles 
plt.plot(t, t, 'r--', t, t**2, 'bs', t, t**3, 'g^') 
plt.axis([0, 6, 0, 150]) # x and y range of axis 
plt.show() 


#---------------------------------------------------------------------------
# Pie chart, where the slices will be ordered and plotted counter-clockwise:
labels = 'CSE', 'ECE', 'IT', 'EE'
sizes = [15, 30, 25, 10]


ax1 = plt.subplot()
ax1.pie(sizes, labels=labels, autopct='%1.2f%%')
ax1.axis('equal')  # Equal aspect ratio ensures that pie is drawn as a circle.

plt.show()


#--------------------------------------
#Splitinggup The Dataset

# Data Preprocessing Template

# Importing the libraries
import numpy as np
import matplotlib.pyplot as plt
import pandas as pd

# Importing the dataset
dataset = pd.read_csv('Data.csv')
X = dataset.iloc[:, :-1].values
y = dataset.iloc[:, 3].values



# Splitting the dataset into the Training set and Test set
from sklearn.cross_validation import train_test_split
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size = 0.2, random_state = 0)