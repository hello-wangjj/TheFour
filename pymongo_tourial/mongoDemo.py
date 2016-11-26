#!python3
# -*- coding: utf-8 -*-
import pymongo
__author__ = 'wangjj'
__mtime__ = '2016112520:27'
client = pymongo.MongoClient('localhost', 27017)
ganji = client['ganji']
print(ganji.collection_names())
item_info = ganji['item_info']
print(item_info.find_one())
print(item_info.find_one({'status': 1}))
'''
db.Account.update({"UserName":"libing"},{"$set":{"Email":"libing@126.com","Password":"123"}})
'''
