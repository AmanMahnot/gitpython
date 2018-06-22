# -*- coding: utf-8 -*-
"""
Created on Fri May 18 11:24:31 2018

@author: user
"""


import oauth2
import time
import urllib2
import json
url1 = "https://api.twitter.com/1.1/search/tweets.json" 
params = {
        "oauth_version": "1.0",
        "oauth_nonce": oauth2.generate_nonce(),
        "oauth_timestamp": int(time.time())
    }
consumer = oauth2.Consumer(key="1xICz7Jnx2v5l2g7UpWTIX6Qy", secret="Se54Yeg2z9lKVE6txRVjrrZYvrvSavIJq6ivTt8B3ceINHRL1C")
token = oauth2.Token(key="997355542745001984-TJpqb01UnBlWVInUMc9OKO4sjbzbQRG",
                     secret="t4Ir4JFmZYVWHHsMYIHoFRz2VJanZRLmhF7hfqYWb3mkF")

params["oauth_consumer_key"] = consumer.key

params["oauth_token"] = token.key

params["q"] = "Jaipur"

req = oauth2.Request(method="GET", url=url1, parameters=params)
signature_method = oauth2.SignatureMethod_HMAC_SHA1() 
req.sign_request(signature_method, consumer, token)

url = req.to_url()
response = urllib2.Request(url)
data = json.load(urllib2.urlopen(response))



filename = params["q"]      
f = open(filename + "_File.txt", "w")
json.dump(data["statuses"], f)
f.close()