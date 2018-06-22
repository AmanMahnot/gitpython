# -*- coding: utf-8 -*-
"""
Created on Wed May 16 10:32:12 2018

@author: user
"""

#file handling
#opening a file
fp = open("abc.txt")
#reading a file
fp.read()
#single line
fp.seek(0,0)
fp.readline()
#closing a file
fp.close()
#file pointer to any location
fp.seek(a,b)
b=0#starting
b=1#current
b=2#end
#file to list
fp.readlines()
#writing a file 
fp = open ("abc.txt")
fp.write("adusygad")
fp.close()




#compress a file or string
import zlib
s="jjsncjncjenjcnejncjne ehb cjhebnj  cenccnbejc e ce cj "
len(s)
t=zlib.compress(s)
#decompress
zlib.decompress(t)


#open a url
import urllib2
f=urllib2.urlopen("http.....")
#read a url source
f.read(100)



#image processing
from PIL import Image

# Open the image and create it's instance
img = Image.open("Sample.jpg")
#img.show()


#image filters
from PIL import ImageFilter
img.filter(ImageFilter.BLUR).show()
img.mode