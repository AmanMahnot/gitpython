# -*- coding: utf-8 -*-
"""
Created on Sun May 27 16:18:26 2018

@author: Peeyush Goyal
"""

import requests
from pymongo import MongoClient
import re

client=MongoClient("localhost",27017)

Number=raw_input("enter number")
Message=raw_input("enter Message")

if re.match(r'^\d{10}$',Number):
    URL="https://api.mlab.com/api/1/databases/message/collections/SMS?apiKey=WK7iJqbZsfGO_vBz4aA53ZrKUgw-bfb3"
    URL2="https://smsapi.engineeringtgr.com/send/?Mobile=8562030963&Password=123456789&Key=peeyuHdxN6WbgO4yVQD7u&Message="+Message+"&To="+Number
    data={
          "Number":Number,
          "Message":Message
          }
    p=requests.post(url = URL,json=data)
    e=requests.post(url=URL2)
    print e.text
    print p.text
else:
    print "enter valid mobile number"

