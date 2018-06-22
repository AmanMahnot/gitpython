# -*- coding: utf-8 -*-
"""
Created on Tue Jun 19 12:18:30 2018

@author: user
"""



 #Description:Car License plate detection of India
 #Author: Forsk Technologies
 #Version:1.1
 #Revision Date:27/08/2016


from havenondemand.hodclient import *
import json
import pandas as pd

client = HODClient("919648a7-194f-4a0f-9255-7c9314af6b31", "v1") #apikey

params = {'file': 'gb-plates.mp4', 'source_location': 'GB'} ##if using url

# for indian plates============'source_location': 'IN'

#params = {'file': 'E:/abcd.mp4', 'source_location': 'GB'} ## or if using a local file
response_async = client.post_request(params, 'recognizelicenseplates', async=True)
jobID = response_async['jobID']
#print jobID

## Wait some time afterwards for async call to process...
response = client.get_job_result(jobID)
print response

#dump data in a json file
with open('data.json', 'w') as outfile:
    json.dump(response, outfile)