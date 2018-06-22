# -*- coding: utf-8 -*-
"""
Created on Wed May 16 14:40:26 2018

@author: user
"""

def brick(small, big, target):
    if target == 5:
        if big >= 1 or small >= 5:
            return True
        else:
            return False
    elif target < 5:
        if small >= target:
            return True
        else:
            return False
    elif target > 5:
        if target<(big*5):
           req_big = target/5
           rem = target - (req_big*5)
        else:
            rem = target - (big*5)
        if small >= rem:
            return True
        else:
            return False
        
#main script
val = input("Enter number of small brick, large brick & target: ")
val_list = list(val)
print brick(val_list[0], val_list[1], val_list[2])