# -*- coding: utf-8 -*-
"""
Created on Mon May 14 13:06:15 2018

@author: user
"""
string=raw_input("Enter string:").strip()
letters=0
digits=0
for i in string:
      if i.isdigit():
          digits+=1
      elif i.isalpha():
          letters+=1
print("The number of digits is:")
print(digits)
print("The number of letters is:")
print(letters)