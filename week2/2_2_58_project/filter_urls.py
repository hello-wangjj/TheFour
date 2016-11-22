#!python3
# -*- coding: utf-8 -*-
from multiprocessing import Pool
from page_parsing import get_item_info, get_links_from, url_list, item_info
__author__ = 'wangjj'
__mtime__ = '2016112218:32'
db_urls = [item['url'] for item in url_list.find()]
index_urls = [item['url'] for item in item_info.find()]
x = set(db_urls)
y = set(db_urls)
rest_urls = x - y
