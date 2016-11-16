#!/usr/bin/env python
# -*- coding: utf-8 -*-
import requests
from bs4 import BeautifulSoup
import pymongo
__author__ = 'wangjj'
__mtime__ = '2016111622:09'
client = pymongo.MongoClient('localhost', 27017)
xiaozhu = client['xiaozhu']
bnb_info = xiaozhu['bnb_info']

# 单页 测试
# 多页的下次写
headers = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 6.1; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/53.0.2785.116 Safari/537.36'
}
def get_page_info():
    global headers
    base_url = 'http://bj.xiaozhu.com/search-duanzufang-p1-0/'
    wb_data = requests.get(base_url, headers=headers)
    soup = BeautifulSoup(wb_data.text, 'lxml')
    prices = soup.select('span.result_price > i')
    titles = soup.select('span.result_title')
    urls = soup.select('#page_list > ul > li > a')
    for price,title,url in zip(prices,titles,urls):
        data={
            'title':title.get_text(),
            'price':int(price.get_text()),
            'url':url.get('href')
        }
        bnb_info.insert_one(data)
    print('done')

for i in bnb_info.find():
    if i['price']>400:
        print(i)
