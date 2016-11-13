#!/usr/bin/env python
# -*- coding: utf-8 -*-
from bs4 import BeautifulSoup
import requests
import urllib.request
import os
__author__ = 'wangjj'
__mtime__ = '20161111下午 3:54'
headers = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 6.1; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/53.0.2785.116 Safari/537.36',
}
path = '../week1/1_4_homework/image/'
url = 'http://weheartit.com/inspirations/taylorswift?scrolling=true&page=2'
proxies = {"http": "http://124.88.67.63:80"}


def get_ima_url(url):
    global headers
    global proxies
    img_urls = []
    wb_data = requests.get(url, headers=headers, proxies=proxies)
    soup = BeautifulSoup(wb_data.text, 'lxml')
    images = soup.select('img.entry-thumbnail')
    for image in images:
        img_urls.append(image.get('src'))
    print(len(img_urls))
    print(img_urls)
    return img_urls


def download_imgs(url):
    # 'http://data.whicdn.com/images/160617448/superthumb.jpg'
    global path
    if not os.path.isdir(path):
        os.mkdir(path)

    urllib.request.urlretrieve(
        url, path + url.split('/')[-2] + url.split('/')[-1])
    print('done')

if __name__ == '__main__':
    # get_ima_url(url)
    download_imgs('http://img2.tuicool.com/YZzaqmI.png')
