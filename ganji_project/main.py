#!python3
# -*- coding: utf-8 -*-
from multiprocessing import Pool
from ganji_project import channel_extracter
from ganji_project import page_parsing
__author__ = 'wangjj'
__mtime__ = '2016112220:22'
db_urls = [item['url'] for item in page_parsing.url_list.find()]
index_urls = [item['url'] for item in page_parsing.item_info.find()]
x = set(db_urls)
y = set(index_urls)
rest_urls = x - y
rest_urls = list(rest_urls)


def get_all_links_from(channel):
    for i in range(0, 100):
        page_parsing.get_links_from(channel, i)


if __name__ == '__main__':
    pool = Pool()
    # pool.map(get_all_links_from, channel_extracter.channel_list.split())
    pool.map(page_parsing.get_item_info, rest_urls)
