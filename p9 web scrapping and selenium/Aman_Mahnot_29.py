# -*- coding: utf-8 -*-
"""
Created on Tue May 22 10:01:24 2018

@author: user
"""
import re
l=[]
i=0
while True:
    a=raw_input("enter the numbers to check float number :")
    if not a:
        break
    l.append(a)
    regex = re.compile(r'^[+-]?[0-9]*\.[0-9]+$')
    response = regex.match(a)
    if response:
        print "True"
    else:
        print "False"