# -*- coding: utf-8 -*-
"""
Created on Tue May 22 12:01:47 2018

@author: user
"""

import re


string1 = "The winter is very COLD"
string2 = "winter is very COLD"
string3 = "The winter is very COLD, but summer is very HOT"

# re.compile converts regex pattern to variable,
# and makes it easier to reuse
regex = re.compile(r'[a-zA-Z]+ is very [a-zA-Z]+')


## Search 
# Gets the string from where the match is found
response = regex.findall(string2)
if response:
    # The groups contain the matched values.
    # It always returns the fully matched string
    print response
else:
    print "The regex pattern does not match."