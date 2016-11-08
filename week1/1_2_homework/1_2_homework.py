#!/usr/bin/env python
# -*- coding: utf-8 -*-
from bs4 import BeautifulSoup
import re
__author__ = 'wangjj'
__mtime__ = '20161106下午 4:46'


'''
body > div:nth-child(2) > div > div.col-md-9 > div:nth-child(2) > div:nth-child(3) > div > img
body > div:nth-child(2) > div > div.col-md-9 > div:nth-child(2) > div:nth-child(3) > div > div.caption > h4.pull-right
body > div:nth-child(2) > div > div.col-md-9 > div:nth-child(2) > div:nth-child(3) > div > div.caption > h4:nth-child(2) > a
body > div:nth-child(2) > div > div.col-md-9 > div:nth-child(2) > div:nth-child(3) > div > div.ratings > p:nth-child(2) > span:nth-child(1)
body > div:nth-child(2) > div > div.col-md-9 > div:nth-child(2) > div:nth-child(2) > div > div.ratings > p:nth-child(2) > span:nth-child(1)
body > div:nth-child(2) > div > div.col-md-9 > div:nth-child(2) > div:nth-child(3) > div > div.ratings > p:nth-child(2) > span:nth-child(2)
body > div:nth-child(2) > div > div.col-md-9 > div:nth-child(2) > div:nth-child(2) > div > div.ratings > p:nth-child(2) > span:nth-child(2)
body > div:nth-child(2) > div > div.col-md-9 > div:nth-child(2) > div:nth-child(1) > div > div.ratings > p:nth-child(2) > span:nth-child(5)
body > div:nth-child(2) > div > div.col-md-9 > div:nth-child(2) > div:nth-child(3) > div > div.ratings > p.pull-right
'''

with open('./1_2_homework_required/index.html', 'r') as html:
    soup = BeautifulSoup(html, 'lxml')
    # print(soup)
    images = soup.select(
        'body > div > div > div.col-md-9 > div > div > div > img')
    # print(images)
    prices = soup.select(
        'body > div > div > div.col-md-9 > div > div > div > div.caption > h4.pull-right')
    titles = soup.select(
        'body > div > div > div.col-md-9 > div > div > div > div.caption > h4 > a')
    stars = soup.find_all('div', class_='ratings')
    marks = soup.select(
        'body > div > div > div.col-md-9 > div > div > div > div.ratings > p.pull-right')
    # print(stars)
    # 为了从父节点开始取,此处保留:nth-of-type(2),观察网页,多取几个星星的selector,就发现规律了
    all_star=soup.select('body > div > div > div.col-md-9 > div > div > div > div.ratings > p:nth-of-type(2)')
    print(all_star)

pattern = re.compile(r'<span class="glyphicon glyphicon-star"></span>')
datas = []
for image, price, title, star, mark in zip(
        images, prices, titles, stars, marks):
    sta = len(star.find_all('span', class_='glyphicon glyphicon-star'))
    data = {
        'title': title.get_text(),
        'price': price.get_text(),
        'star': sta,
        'mark': mark.get_text(),
        'image': image.get('src')
    }
    datas.append(data)
print(datas)
