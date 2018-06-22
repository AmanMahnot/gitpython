# -*- coding: utf-8 -*-
"""
Created on Tue May 15 12:58:19 2018

@author: user
"""
def pattern(n):
    i = 0
    while i < n:
        j = i + 1
        print j*"*"
        i = i + 1
    '''while i > 1:
        j = i - 1
        print j*'*'
        i = i - 1
'''

num = input("Enter value of n: ")
pattern(num)