#!python3
# -*- coding: utf-8 -*-
import requests
from bs4 import BeautifulSoup
import pymongo
import time
__author__ = 'wangjj'
__mtime__ = '2016111820:20'
client = pymongo.MongoClient('localhost', 27017)
ceshi = client['ceshi']
shoujihao = ceshi['shoujihao']
base_url = 'http://hz.58.com/shoujihao/pn1/'
headers = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 6.1; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/53.0.2785.116 Safari/537.36'
}
#单页行为
wb_data = requests.get(base_url, headers=headers)
soup = BeautifulSoup(wb_data.text, 'lxml')
infos = soup.select('ul > li > a.t')
for info in infos:
    if info.find('span', 'jz-title'):
        pass
    else:
        number = info.find('strong', 'number')
        price = info.find('b', 'price') if info.find('b', 'price') else None
        link = (info.get('href')).split('?')[0]
        data = {
            'number': number,
            'price': price,
            'link': link
        }
        # print(data)
        shoujihao.insert_one(data)
print('done')
# 设计函数
def get_pages_within(pages):
    global headers
    for page in range(1, pages+1):
        time.sleep(2)
        wb_data=requests.get('http://hz.58.com/shoujihao/pn{}/'.format(str(page)), headers=headers)
        soup = BeautifulSoup(wb_data.text, 'lxml')
        infos = soup.select('ul > li > a.t')
        for info in infos:
            if info.find('span', 'jz-title'):
                pass
            else:
                number = info.find('strong', 'number')
                price = info.find('b', 'price') if info.find('b', 'price') else None
                link = (info.get('href')).split('?')[0]
                data = {
                    'number': number.get_text(),
                    'price': price.get_text(),
                    'link': link
                }
                # print(data)
                shoujihao.insert_one(data)
        print('done')
get_pages_within(3)



