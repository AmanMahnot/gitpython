# -*- coding: utf-8 -*-
"""
Created on Wed May 23 13:05:17 2018

@author: user
"""
import requests
l=[]
while True:
    more = raw_input("Want to enter more data? Y/N: ")
    if not more:
        break
    a = raw_input("Enter phone number : ")
    b = raw_input("Enter name : ")
    c = raw_input("Enter college name : ")
    d = raw_input("Enter branch : ")
    data = {
            "Phone_Number":a,
            "Name":b,
            "College_Name":c,
            "Branch":d
            }
    l.append(data)

send_url= "https://api.mlab.com/api/1/databases/my_database/collections/student?apiKey=GKJkrd5bruhHUyDQOFnG_4IpOJHuuCYl"
for i in l:
    send_req= requests.post(send_url,json = i)
    print send_req.text

search_phone = raw_input("Enter phone number to search: ")
re_url ="https://api.mlab.com/api/1/databases/my_database/collections/student?q={'Phone_Number': '"+search_phone+"'}&fo=true&apiKey=GKJkrd5bruhHUyDQOFnG_4IpOJHuuCYl"
re_req=requests.get(re_url)
print re_req.text
