# -*- coding: utf-8 -*-
"""
Created on Fri May 18 14:05:10 2018

@author: user
"""


import facebook as fb
access_token = "EAACEdEose0cBAIBpr7g3ZC5blD5FfGlSms39ZCNiYXFFLvIFCvjXIylyKT5SGjZBM7lR0Bj4GQvZBFkiWyMLIrBNXZAhZCjpcWAlfsA1AvP5g35D22uojLsi6uOILQq73RWgyZBPIP9XjoDtVhWqpZCeKMH5IPcvDeXQ5wWAtk7rlixmLANwDQF4Q0xfaZCwh2B5fzIbmTZCpYlgZDZD"

status = "Hi"

graph = fb.GraphAPI(access_token)
post_id = graph.put_wall_post(status)

graph.put_photo(image=open('iiii.jpg', 'rb'),
                message='Look at this cool photo!')

