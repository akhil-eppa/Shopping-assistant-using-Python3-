# -*- coding: utf-8 -*-
"""
Created on Mon Dec 31 11:21:02 2018

@author: Akhil
"""
'''
import requests
res = requests.get('https://www.team-bhp.com/forum/introduce-yourself/205183-hello-world.html')
print(res.text[0:250])
'''

import bs4,requests

res = requests.get('https://www.team-bhp.com/')
res.raise_for_status()
f=open("source.txt","w")
f.write(res.text)
f.close()
f1=open("source.txt","r")


noStarchSoup = bs4.BeautifulSoup(f1)
elems=noStarchSoup.select('em')
print(elems[0].getText())
f1.close()



'''
exampleFile=open("example.html")
exampleSoup=bs4.BeautifulSoup(exampleFile)
elems=exampleSoup.select("#author")
print(elems[0].getText())
print(str(elems[0]))
'''