# -*- coding: utf-8 -*-
"""
Created on Wed Jun 20 11:26:00 2018

@author: user
"""

import urllib2
from bs4 import BeautifulSoup

#faridabad

wiki='https://weather.com/en-IN/weather/hourbyhour/l/bca765a438240d6c71df1563f9ac22192c726b678b65c9bc136c3c26d247c45a'
page =urllib2.urlopen(wiki)
soup=BeautifulSoup(page)
all_tables=soup.findAll('table')
right_table=soup.find('table',class_='twc-table')

a=[]
b=[]
c=[]
d=[]
e=[]
f=[]
g=[]
h=[]

for row in right_table.findAll("tr"):
    cells = row.findAll('td')
    
    if len(cells)==8:
        a.append(cells[0].find(text=True))
        b.append(cells[1].find(text=True))
        c.append(cells[2].find(text=True))
        d.append(cells[3].find(text=True))
        e.append(cells[4].find(text=True))
        f.append(cells[5].find(text=True))
        g.append(cells[6].find(text=True))
        h.append(cells[7].find(text=True))
         


import pandas as pd 
df=pd.DataFrame(b,columns=['Time'])
df['description_faridabad']=c
df['temp_faridabad']=d
df['Feels_faridabad']=e
df['Precip_faridabad']=f
df['Humidity_faridabad']=g
df['wind_faridabad']=h

print df
df.to_csv("weather-faridabad.csv")

#sonipat

wiki='https://weather.com/en-IN/weather/hourbyhour/l/325e75e3501954ffb0a6d9f5303eeae78ab19466f06ab598ef2eacf613cb9120'
page =urllib2.urlopen(wiki)
soup=BeautifulSoup(page)
all_tables=soup.findAll('table')
right_table=soup.find('table',class_='twc-table')

a=[]
b=[]
c=[]
d=[]
e=[]
f=[]
g=[]
h=[]

for row in right_table.findAll("tr"):
    cells = row.findAll('td')
    
    if len(cells)==8:
        a.append(cells[0].find(text=True))
        b.append(cells[1].find(text=True))
        c.append(cells[2].find(text=True))
        d.append(cells[3].find(text=True))
        e.append(cells[4].find(text=True))
        f.append(cells[5].find(text=True))
        g.append(cells[6].find(text=True))
        h.append(cells[7].find(text=True))
         


import pandas as pd 
df=pd.DataFrame(b,columns=['Time'])
df['description_sonipat']=c
df['temp_sonipat']=d
df['Feels_sonipat']=e
df['Precip_sonipat']=f
df['Humidity_sonipat']=g
df['wind_sonipat']=h

print df
df.to_csv("weather-sonipat.csv")

#ghaziabad

wiki='https://weather.com/en-IN/weather/hourbyhour/l/2dff223a88960859fd893b8ebf894765d5db05545f6cd80e428d81db4aab96c1'
page =urllib2.urlopen(wiki)
soup=BeautifulSoup(page)
all_tables=soup.findAll('table')
right_table=soup.find('table',class_='twc-table')

a=[]
b=[]
c=[]
d=[]
e=[]
f=[]
g=[]
h=[]

for row in right_table.findAll("tr"):
    cells = row.findAll('td')
    
    if len(cells)==8:
        a.append(cells[0].find(text=True))
        b.append(cells[1].find(text=True))
        c.append(cells[2].find(text=True))
        d.append(cells[3].find(text=True))
        e.append(cells[4].find(text=True))
        f.append(cells[5].find(text=True))
        g.append(cells[6].find(text=True))
        h.append(cells[7].find(text=True))
         


import pandas as pd 
df=pd.DataFrame(b,columns=['Time'])
df['description_ghaziabad']=c
df['temp_ghaziabad']=d
df['Feels_ghaziabad']=e
df['Precip_ghaziabad']=f
df['Humidity_ghaziabad']=g
df['wind_ghaziabad']=h

print df
df.to_csv("weather-ghaziabad.csv")

#delhi

wiki='https://weather.com/en-IN/weather/hourbyhour/l/fffd11657e1a23cfc2cdacc9de4282385d0422d0e8c44c7a6654e36aad4bf789'
page =urllib2.urlopen(wiki)
soup=BeautifulSoup(page)
all_tables=soup.findAll('table')
right_table=soup.find('table',class_='twc-table')

a=[]
b=[]
c=[]
d=[]
e=[]
f=[]
g=[]
h=[]

for row in right_table.findAll("tr"):
    cells = row.findAll('td')
    
    if len(cells)==8:
        a.append(cells[0].find(text=True))
        b.append(cells[1].find(text=True))
        c.append(cells[2].find(text=True))
        d.append(cells[3].find(text=True))
        e.append(cells[4].find(text=True))
        f.append(cells[5].find(text=True))
        g.append(cells[6].find(text=True))
        h.append(cells[7].find(text=True))
         


import pandas as pd 
df=pd.DataFrame(b,columns=['Time'])
df['description_delhi']=c
df['temp_delhi']=d
df['Feels_delhi']=e
df['Precip_delhi']=f
df['Humidity_delhi']=g
df['wind_delhi']=h

print df

df.to_csv("weather-delhi.csv")