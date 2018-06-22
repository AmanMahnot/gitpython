# -*- coding: utf-8 -*-
"""
Created on Mon May 28 12:16:36 2018

@author: user
"""

import urllib2
from bs4 import BeautifulSoup
wiki='https://en.wikipedia.org/wiki/List_of_states_and_union_territories_of_India_by_area'
page =urllib2.urlopen(wiki)
soup=BeautifulSoup(page)
right_table=soup.find('table',class_='wikitable')
a=[]
b=[]


for row in right_table.findAll("tr"):
    cells = row.findAll('td')
    if len(cells)==7:
        a.append(cells[1].find(text=True))
        b.append(cells[4].find(text=True))
        
import pandas as pd
df=pd.DataFrame(a,columns=['State/Terr'])
df['National share(%)']=b
df=df.iloc[0:6,:]
print df


import matplotlib.pyplot as plt
labels = df.iloc[:,0]
sizes = df.iloc[:,-1]
e=[0.2,0,0,0,0,0]
ax1 = plt.subplot()
ax1.pie(sizes,e, labels=labels, autopct='%1.2f%%')
ax1.axis('equal')  # Equal aspect ratio ensures that pie is drawn as a circle.

plt.show()
