#!python3
# -*- coding: utf-8 -*-
import requests
from bs4 import BeautifulSoup
import time
import random
import pymongo
__author__ = 'wangjj'
__mtime__ = '2016112221:18'

client = pymongo.MongoClient('localhost', 27017)
ganji = client['ganji']
url_list = ganji['url_list']
item_info = ganji['item_info']
proxy_list = [
    'http://124.88.67.63:80',
    # 'http://115.159.185.186:8088',
]
# 随机获取代理IP
proxy_ip = random.choice(proxy_list)
proxy = {
    'http': proxy_ip
}

headers = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 6.1; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/53.0.2785.116 Safari/537.36',
}
# spider1


def get_links_from(channel, page, who_sell='a1'):
    # http://hz.ganji.com/jiaju/   channel
    # http://hz.ganji.com/jiaju/a1o3/
    global headers
    global proxy
    if page != 0:
        page = 'o' + str(page)
    else:
        page = ''
    url = '{}{}{}/'.format(channel, who_sell, page)
    print(url)
    time.sleep(5)
    print(proxy)
    wb_data = requests.get(url, headers=headers)
    soup = BeautifulSoup(wb_data.text, 'lxml')
    if soup.find('div', 'noinfo'):
        print('pass')
        pass
    else:
        links = soup.select('tr.zzinfo > td.t > a.t')
        for link in links:
            item_link = link.get('href').split('?')[0]
            url_list.insert_one({'url': item_link})
            print(item_link)

# spider2


def get_item_info(url, data=None):
    global headers
    global proxy
    time.sleep(4)
    wb_data = requests.get(url, headers=headers)
    if wb_data.status_code == 404:
        pass
    else:
        print(url)
        soup = BeautifulSoup(wb_data.text, 'lxml')
        if soup.find('span', 'soldout_btn'):
            data = {
                'url': url,
                'title': 'sold_out',
                'status': 1
            }
            print(data)
            item_info.insert_one(data)
        else:
            data = {
                'title': soup.find(
                    'h1', 'info_titile').get_text(),
                'price': list(
                    soup.find(
                        'span', 'price_now').stripped_strings)[1],
                'place': list(
                    (soup.find(
                        'div', 'palce_li')).stripped_strings)[1],
                'url': url,
                'status': 0
            }
            print(data)
            item_info.insert_one(data)

if __name__ == '__main__':
    for i in range(5, 6):
        get_links_from('http://hz.ganji.com/jiaju/', i)
    # get_item_info('http://zhuanzhuan.ganji.com/detail/769043829245296644z.shtml')
