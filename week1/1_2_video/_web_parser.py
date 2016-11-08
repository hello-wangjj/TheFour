#!/usr/bin/env python
# -*- coding: utf-8 -*-
from bs4 import BeautifulSoup
__author__ = 'wangjj'
__mtime__ = '20161105上午 12:20'

info = []
with open('./web/new_index.html', 'r') as f:
    soup = BeautifulSoup(f, 'lxml')
    # print(soup)
    images = soup.select('body > div.main-content > ul > li > img')
    titles = soup.select(
        'body > div.main-content > ul > li > div.article-info > h3 > a')
    descs = soup.select(
        'div.main-content > ul > li > div.article-info > p.description')
    rates = soup.select('body > div.main-content > ul > li > div.rate > span')
    cates = soup.select(
        'body > div.main-content > ul > li > div.article-info > p.meta-info')
    print(images, titles, descs, rates, cates, sep='\n---------------\n')

for title, image, desc, rate, cate in zip(titles, images, descs, rates, cates):
    data = {
        'title': title.get_text(),
        'desc': desc.get_text(),
        'rate': rate.get_text(),
        # 'cate':cate.get_text(),
        'cate': list(cate.stripped_strings),
        'image': image.get('src')
    }
    print(data)
    info.append(data)
for i in info:
    if float(i['rate']) >= 4:
        print(i['title'], i['desc'], i['cate'], sep='*')
        print('***********')


'''
    body > div.main-content > ul > li:nth-child(1) > img
    body > div.main-content > ul > li:nth-child(1) > div.article-info > h3 > a
    body > div.main-content > ul > li:nth-child(1) > div.article-info > p.meta-info > span:nth-child(1)
    body > div.main-content > ul > li:nth-child(1) > div.article-info > p.description
    body > div.main-content > ul > li:nth-child(1) > div.rate > span
'''
