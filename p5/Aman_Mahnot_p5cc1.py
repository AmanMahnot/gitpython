# -*- coding: utf-8 -*-
"""
Created on Wed May 16 11:25:21 2018

@author: user
"""

for i in range(1,51):
    if i%3==0 and i%5==0:
        print "FizzBuzz"
    elif i%3==0:
        print "Fizz"
    elif i%5==0:
        print "Buzz"
    else:
        print i
