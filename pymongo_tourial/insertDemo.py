#!python3
# -*- coding: utf-8 -*-
import pymongo
import random
__author__ = 'wangjj'
__mtime__ = '2016113023:55'
client = pymongo.MongoClient('localhost', 27017)
ganji = client['ganji']
article_info = ganji['article_info']
for i in range(100):
    title = 'just a title {}'.format(str(i))
    desc = 'just a description {}'.format(str(i))
    scores = str(random.randint(1, 7))
    tag_1 = 'tag {}'.format(str(i))
    tag_2 = 'tag {}'.format(str(i + 1))
    tags = [tag_1, tag_2]
    # print(title, desc, scores, tags)
    data = {
        'title': title,
        'desc': desc,
        'scores': scores,
        'tags': tags
    }
    article_info.insert_one(data)
    print('done')
