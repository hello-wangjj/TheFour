#!python3
# -*- coding: utf-8 -*-
from bs4 import BeautifulSoup
import requests
import time
import pymongo
__author__ = 'wangjj'
__mtime__ = '2016111722:29'
client = pymongo.MongoClient('localhost', 27017)
ceshi = client['ceshi']
url_list = ceshi['url_list']
item_info = ceshi['item_info']
headers = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 6.1; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/53.0.2785.116 Safari/537.36'
}


def get_links_from(channel, pages, who_sells=0):
    # http://hz.58.com/shouji/0/pn2/
    global headers
    list_view = '{}{}/pn{}'.format(channel, str(who_sells), str(pages))
    wb_data = requests.get(list_view, headers=headers)
    time.sleep(1)
    soup = BeautifulSoup(wb_data.text, 'lxml')
    if soup.find('td', 't'):
        for link in soup.select('td.t a.t'):
            item_link = (link.get('href')).split('?')[0]
            url_list.insert_one({'url': item_link})
            print(item_link)
    else:
        pass


def get_item_info(url):
    global headers
    wb_data = requests.get(url, headers=headers)
    soup = BeautifulSoup(wb_data.text, 'lxml')
    sold_out = soup.find('span', 'soldout_btn')
    if sold_out:
        pass
    else:
        title = soup.select('div.box_left_top > h1')[0].get_text()
        category = (soup.select('div.breadCrumb')[0]).stripped_strings
        price = soup.select('span.price_now > i')[0].get_text()
        place = soup.select('div.palce_li > span > i')[0].get_text()
        item_info.insert_one({'category': list(
            category), 'title': title, 'price': price, 'place': place, 'url': url})
        print({'category': list(category), 'title': title,
               'price': price, 'place': place, 'url': url})

if __name__ == '__main__':
    # get_links_from('http://hz.58.com/tongxunyw/', '2')
    get_item_info('http://zhuanzhuan.58.com/detail/795538562757083140z.shtml')
