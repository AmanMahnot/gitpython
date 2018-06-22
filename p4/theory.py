# -*- coding: utf-8 -*-
"""
Created on Tue May 15 10:03:48 2018

@author: user
"""
'''python is a functional programming language'''
a = [1,2]
b = [1,2]
a is b
a==b
c=a 
a is c
# Functions
def func_name(a,b):
    return a+b
func_name(1,2)
#filter
def f(x):
    return x%3==0 or x%5==0
filter(f,range(2,24))
#map
def cube(x):
    return x*x*x
map(cube,range(1,11))
#lambda function
map(lambda x:x*x*x,range(1,11))
#reduce
def add(x,y):
    return x+y
reduce(add,range(1,11))





a=[1,2,3]
[x**2 for x in a]


a=['it','is','raining' ,'cats' ,'and' ,'dogs']
map(lambda x:len(x),a)