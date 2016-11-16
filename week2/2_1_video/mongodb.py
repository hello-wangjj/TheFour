#!/usr/bin/env python
# -*- coding: utf-8 -*-
import pymongo
__author__ = 'wangjj'
__mtime__ = '20161115下午 11:02'
client=pymongo.MongoClient('localhost',27017)
wangjj_mongo=client['wangjj_mongo']
sheet_lines=wangjj_mongo['sheet_lines']


