#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Aug  4 00:22:13 2020

@author: hrishi
"""


from bs4 import BeautifulSoup
from urllib.request import urlopen
import requests
import time


#Get current time
t = time.localtime()
current_time = time.strftime("%H:%M:%S", t)
print(current_time)


i=0



link="https://www.mygov.in/covid-19"
res=requests.get(link)
bs4obj =BeautifulSoup(res.text ,features="html.parser")
list1=bs4obj.find_all("span",{"class":"st_name"})
list2=bs4obj.find_all("span",{"class":"st_number"})
list5=[]
list6=[]
list3=[]
list4=[]
list7=bs4obj.find_all("span",attrs={"class":'icount'})
list8=bs4obj.find_all("div",attrs={"class":'color-red up-arrow'})
list9=bs4obj.find_all("div",attrs={"class":'color-green up-arrow'})
for foo in bs4obj.find_all('div', attrs={'class': 'tick-confirmed'}):
    bar = foo.find('small')
    list3.append(bar.text)
for foo in bs4obj.find_all('div', attrs={'class': 'tick-active'}):
    bar = foo.find('small')
    list4.append(bar.text)
for foo in bs4obj.find_all('div', attrs={'class': 'tick-discharged'}):
    bar = foo.find('small')
    list5.append(bar.text)
for foo in bs4obj.find_all('div', attrs={'class': 'tick-death'}):
    bar = foo.find('small')
    list6.append(bar.text)


for (state,number,confirmed,active,discharge,death) in zip(list1,list2,list3,list4,list5,list6):
     print("      STATE/UNION TERRITORY   "+state.get_text()+"\nTotal cases="+number.get_text()+"\nConfirmed cases="+confirmed+"\nActive cases="+active+"\nDischarge cases="+discharge+"\nDeath cases="+death)

b=0

print("\nTotal cases in India:")
for a in list7:
    print(a.get_text())
