# -*- coding: utf-8 -*-
"""
Created on Sun May 27 21:54:59 2018

@author: user
"""
'''
http://sms.dataoxytech.com/index.php/smsapi/httpapi/?uname=amanmahnot&password=12312393&receiver=9928049888&route=PA&msgtype=1&sender=default&sms=hello
https://mlab.com/databases/bbbb/collections/mobile
GKJkrd5bruhHUyDQOFnG_4IpOJHuuCYl
'''
import requests

send_url= "http://sms.dataoxytech.com/index.php/smsapi/httpapi/?uname=amanmahnot&password=12312393&receiver=9680455964&route=PA&msgtype=1&sender=default&sms=sbcjhbasjbas"

send_req= requests.post(send_url)
print send_req.text