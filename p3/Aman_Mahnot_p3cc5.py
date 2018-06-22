# -*- coding: utf-8 -*-
"""
Created on Mon May 14 17:10:36 2018

@author: user
"""

ipstr = raw_input("Enter list of numbers: ")

list1 = ipstr.split(',')

i = 0
while i < len(list1):
    list1[i] = int(list1[i])
    i += 1

smallest = min(list1)
largest = max(list1)

summ = 0        
for i in list1:
  summ += i

avg = (summ-smallest-largest)/(len(list1)-2)  

print avg