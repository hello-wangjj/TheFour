#!python3
# -*- coding: utf-8 -*-
import time
from page_parsing import url_list
__author__ = 'wangjj'
__mtime__ = '2016112216:48'
while True:
    print(url_list.find().count())
    time.sleep(5)