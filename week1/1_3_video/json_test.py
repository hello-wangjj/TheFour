#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json
__author__ = 'wangjj'
__mtime__ = '20161108上午 12:11'
with open('a.json','r') as f:
    json_str=json.loads(f.read())
keys=json_str['store']['modules.common.entity.JSONAddress'].keys()
addresses=json_str['store']['modules.common.entity.JSONAddress']
images=json_str['store']['modules.unimplemented.entity.AccommodationSizedThumbnail']
descs=json_str['store']['modules.common.entity.JSONAttraction']
print(addresses,images,descs,keys,sep='\n-----\n')
for i in keys:
    # print(addresses[i],images[i],descs[i],sep='\n-------\n')

    data={
        'name':descs[i]['name'],
        'description':descs[i]['description'],
        'images':'http:'+images[i]['url'],
        'address':str(addresses[i].get('line4'))+str(addresses[i].get('line3'))+str(addresses[i].get('line2'))+str(addresses[i].get('line1')),
        'type':descs[i]['types'],
        'catecory':descs[i]['category']
    }
    print(data)