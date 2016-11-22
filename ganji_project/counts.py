#!python3
# -*- coding: utf-8 -*-
import time
from ganji_project import page_parsing
__author__ = 'wangjj'
__mtime__ = '2016112223:26'
while True:
    print(page_parsing.url_list.find().count())
    time.sleep(5)
