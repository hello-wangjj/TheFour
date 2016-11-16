#!/usr/bin/env python
# -*- coding: utf-8 -*-
import pymongo
# import os
# print(os.getcwd())
# print(os.path.abspath('.'))
__author__ = 'wangjj'
__mtime__ = '20161115下午 11:02'
client = pymongo.MongoClient('localhost', 27017)
wangjj_mongo = client['wangjj_mongo']
sheet_tab = wangjj_mongo['sheet_tab']
path = './walden.txt'
with open(path, 'r') as f:
    lines = f.readlines()
    for index, line in enumerate(lines):
        data = {
            'index': index,
            'line': line,
            'words': len(line.split())
        }
# 插入
        sheet_tab.insert_one(data)
# 查询
# $lt/$lte/$gt/$gte/$ne，依次等价于</<=/>/>=/!=。（l表示less g表示greater e表示equal n表示not  ）
# for item in sheet_tab.find({'words':{'$lt':5}}):
#     print(item)
# for item in sheet_tab.find():
#     print(item['line'])
