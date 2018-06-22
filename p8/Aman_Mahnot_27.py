# -*- coding: utf-8 -*-
"""
Created on Mon May 21 11:49:28 2018

@author: user
"""
l=[]
#k=[]
while True:
    s=raw_input("enter the number")
    if not s:
        break
    l = s.split()
    
    if all(int(num)>0 for num in l):
        if any(num==num[::-1] for num in l):
            print True
        else:print False
    else:
        print False


'''
for i in l: 
    k.append(i[::-1])
i=0
flag = 0   
while i<len(l) and i>0:
    if k[i]==l[i]:
        print "true"
        flag =1 
        break
    i+=1
if flag ==0:
    print 'false'
    
'''
    


