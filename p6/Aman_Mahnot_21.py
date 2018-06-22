# -*- coding: utf-8 -*-
"""
Created on Thu May 17 12:56:02 2018

@author: user
"""



import requests


data = {
        "Phone_Number":"9928049888",
        "Name":"Aman Mahnot",
        "College_Name":"SKIT",
        "Branch":"IT"
        }

send_url= "http://13.127.155.43/api_v0.1/sending"
send_req= requests.post(send_url,json = data)
print send_req.text
re_url ="http://13.127.155.43/api_v0.1/receiving"
re_url +="?Phone_Number=9928049888"
re_req=requests.get(re_url)
print re_req.text


