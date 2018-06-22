# -*- coding: utf-8 -*-
"""
Created on Thu May 17 11:13:16 2018

@author: user
"""

import string

def is_pangram ():
    gram = raw_input("enter the string")
    gram = gram.lower()
    
    gram_list_old = sorted([c for c in gram if c != ' '])
    gram_list = []
    for c in gram_list_old:
        if c not in gram_list:
            gram_list.append(c)
    if gram_list == list(string.ascii_lowercase):
        print ("PANGRAM")
    else:
        print ("NOT PANGRAM")
is_pangram()

