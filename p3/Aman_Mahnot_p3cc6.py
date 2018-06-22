# -*- coding: utf-8 -*-
"""
Created on Mon May 14 17:11:17 2018

@author: user
"""
ipstr = raw_input("Enter list of numbers: ")

list1 = ipstr.split(',')

i = 0
while i < len(list1):
    list1[i] = int(list1[i])
    i += 1
    
summ = 0
i = 0
while i < len(list1):
    if list1[i] == 13 or list1[i-1] == 13:
        i += 1
        continue
    else:
        summ += list1[i]
    i += 1
    
print summ
