# -*- coding: utf-8 -*-
"""
Created on Thu May 17 10:57:26 2018

@author: user
"""
def reverse():
    a = raw_input("enter the string: ")
    i = 0
    c = 0
    z=[]
    while i<len(a):
        i += 1
        c -= 1
        z.append(a[c])
    
    print ''.join(z)
reverse()

#print a[::-1]