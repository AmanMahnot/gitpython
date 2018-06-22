# -*- coding: utf-8 -*-
"""
Created on Tue May 15 11:22:33 2018

@author: user
"""



def print1():
    
    print "sum is=",sum1(list1)
    print "mul is=",reduce(mul,list1)
    print "largest is=",largest(list1)
    print "smallest is=",smallest(list1)
    print "sorted list is=",sort1(list1)
    print "without duplicates the list is=",remove_duplicates(list1)



def sum1(list1):
    x =0
    for i in list1:
        x= x + i
    return x

def mul(x,y):
    return x*y

def largest(list1):
    return max(list1)

def smallest(list1):
    return min(list1)  

def sort1(list1):
    list1.sort()
    return list1

def remove_duplicates(list1):
    lis=list(set(list1))
    return lis
    

#print script
a=input("enter the list")
list1=list(a)
print1()