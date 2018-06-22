# -*- coding: utf-8 -*-
"""
Created on Fri May 18 13:37:08 2018

@author: user
"""

import facebook as fb
access_token = "EAACEdEose0cBAIBpr7g3ZC5blD5FfGlSms39ZCNiYXFFLvIFCvjXIylyKT5SGjZBM7lR0Bj4GQvZBFkiWyMLIrBNXZAhZCjpcWAlfsA1AvP5g35D22uojLsi6uOILQq73RWgyZBPIP9XjoDtVhWqpZCeKMH5IPcvDeXQ5wWAtk7rlixmLANwDQF4Q0xfaZCwh2B5fzIbmTZCpYlgZDZD"

#status = "Hi"

graph = fb.GraphAPI(access_token)
#post_id = graph.put_wall_post(status)
# Upload an image with a caption.
graph.put_photo(image=open('iiii.jpg', 'rb'),
                message='Look at this cool photo!')

# Upload a photo to an album.
'''graph.put_photo(image=open("img.jpg", 'rb'),
                album_path=album_id + "/photos")

# Upload a profile photo for a Page.
graph.put_photo(image=open("img.jpg", 'rb'),
                album_path=page_id + "/picture")