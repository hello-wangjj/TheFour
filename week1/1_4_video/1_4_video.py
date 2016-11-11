#!/usr/bin/env python
# -*- coding: utf-8 -*-
from bs4 import BeautifulSoup
import requests
import time
__author__ = 'wangjj'
__mtime__ = '20161110下午 11:41'
base_url = 'https://knewone.com/discover?page='
headers = {
    'user-agent': 'Mozilla/5.0 (Windows NT 6.1; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/53.0.2785.116 Safari/537.36',
    'x-csrf-token':'6t5ntfRxAFtT/UE4ns73a8+DqJvzhtUYVe2sqJ1Ed82BblIhYDPTC4k8lSh5AteAKFx5JL8zIz0VZfiVw9YBsA==',
    'x-requested-with':'XMLHttpRequest'
}


def get_page_info(url, data=None):
    global headers
    wb_data = requests.get(url, headers=headers)
    soup = BeautifulSoup(wb_data.text, 'lxml')
    images = soup.select('header.cover > a > img')
    titles = soup.select('section.content > h4 > a')
    links = soup.select('section.content > h4 > a')
    if data is None:
        for image, title, link in zip(images, titles, links):
            data = {
                'image': image.get('src'),
                'title': title.get_text(),
                'link': link.get('href')
            }
            print(data)


def get_more_page(start, end):
    for one in range(start, end):
        get_page_info(base_url + str(one))
        time.sleep(2)
if __name__ == '__main__':
    get_more_page(1, 3)