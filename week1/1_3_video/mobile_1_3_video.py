#!/usr/bin/env python
# -*- coding: utf-8 -*-
import requests
from bs4 import BeautifulSoup
__author__ = 'wangjj'
__mtime__ = '20161108下午 3:44'
headers={
    'User-Agent':'Mozilla/5.0 (iPhone; CPU iPhone OS 9_1 like Mac OS X) AppleWebKit/601.1.46 (KHTML, like Gecko) Version/9.0 Mobile/13B143 Safari/601.1'
}
url='http://www.tripadvisor.cn/Attractions-g60763-Activities-New_York_City_New_York.html#ATTRACTION_LIST'
mobile_data=requests.get(url,headers=headers)
soup=BeautifulSoup(mobile_data.text,'lxml')
images=soup.select('div.thumb.thumbLLR.soThumb > div.missing.lazyMiss')
for i in images:
    print(i.get('data-thumburl'))