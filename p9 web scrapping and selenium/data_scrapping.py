# -*- coding: utf-8 -*-
"""
Created on Mon May 28 10:25:06 2018

@author: user
"""

import urllib2
from bs4 import BeautifulSoup
wiki='https://en.wikipedia.org/wiki/List_of_state_and_union_territory_capitals_in_India'
page =urllib2.urlopen(wiki)
soup=BeautifulSoup(page)
all_tables=soup.findAll('table')
right_table=soup.find('table',class_='wikitable sortable plainrowheaders')
a=[]
b=[]
c=[]
d=[]
e=[]
f=[]
g=[]

for row in right_table.findAll("tr"):
    cells = row.findAll('td')
    states=row.findAll('th')
    if len(cells)==6:
        a.append(cells[0].find(text=True))
        b.append(states[0].find(text=True))
        c.append(cells[1].find(text=True))
        d.append(cells[2].find(text=True))
        e.append(cells[3].find(text=True))
        f.append(cells[4].find(text=True))
        g.append(cells[5].find(text=True))
        
import pandas as pd
df=pd.DataFrame(a,columns=['number'])
df['qdqwd']=b
df['c']=c
df['d']=d
df['e']=e
df['f']=f
df['g']=g
print df