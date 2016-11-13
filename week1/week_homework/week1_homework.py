#!/usr/bin/env python
# -*- coding: utf-8 -*-
from bs4 import BeautifulSoup
import requests
import time
__author__ = 'wangjj'
__mtime__ = '20161112下午 1:49'
url = 'http://hz.58.com/pbdn/pn{}/'.format(str(1))
print(url)
headers = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 6.1; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/53.0.2785.116 Safari/537.36'
}
proxies={
    'hhtp':'http://124.88.67.17:82'
}
def get_page_links(url):
    global headers
    global proxies
    wb_data = requests.get(url, headers=headers,proxies=proxies)
    soup = BeautifulSoup(wb_data.text, 'lxml')
    links = soup.select('#infolist > div.infocon > table > tbody > tr > td.t > a')
    pad_urls=[]
    for link in links:
        pad_urls.append((link.get('href')).split('&')[0])
    print(pad_urls)
    # print(len(pad_urls))
    return pad_urls

# urls=get_page_links('http://hz.58.com/pbdn/pn1/')

sale_url='http://zhuanzhuan.58.com/detail/779703284254474243z.shtml?fullCate=5%2C38484%2C23094'
wb_data=requests.get(sale_url,headers=headers,proxies=proxies)
soup=BeautifulSoup(wb_data.text,'lxml')
category=soup.select('#nav > div > span:nth-of-type(4) > a')
print(category)
title=soup.select('div.box_left_top > h1')
print(title)
view=soup.select('div.box_left_top > p > span.look_time')
print(view)
price=soup.select('div.price_li > span > i')
print(price)
place=soup.select('div.palce_li > span > i')
print(place)
detail=soup.select('body > div.content > div > div.box_left > div:nth-of-type(3) > div > div > p')
print(detail)
print((soup.select('span.icon_png.sanjiao')[0]).find_next('p'))
images=soup.select('body > div.content > div > div.box_left > div:nth-of-type(5) > div > img')
print(images)
