#!/usr/bin/env python
# -*- coding: utf-8 -*-
from bs4 import BeautifulSoup
import requests
__author__ = 'wangjj'
__mtime__ = '20161110上午 12:08'
# url_info = 'http://bj.xiaozhu.com/fangzi/5076532914.html'
headers = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 6.1; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/53.0.2785.116 Safari/537.36'
}


def get_fangzi_info(url_info, data=None):
    global headers
    wb_data = requests.get(url_info, headers=headers)
    soup = BeautifulSoup(wb_data.text, 'lxml')
    title = soup.select(
        'body > div.wrap.clearfix.con_bg > div.con_l > div.pho_info > h4 > em')
    address = soup.select(
        'body > div.wrap.clearfix.con_bg > div.con_l > div.pho_info > p > span')
    rent = soup.select('#pricePart > div.day_l > span')
    image = soup.select('#curBigImage')
    host_image = soup.select(
        '#floatRightBox > div.js_box.clearfix > div.member_pic > a > img')
    host_name = soup.select(
        '#floatRightBox > div.js_box.clearfix > div.w_240 > h6 > a')
    host_sex = soup.select(
        '#floatRightBox > div.js_box.clearfix > div.member_pic > div')
    # print(
    #     title,
    #     address,
    #     rent,
    #     image,
    #     host_image,
    #     host_name,
    #     host_sex,
    #     sep='\n-----------\n')
    for i in range(len(host_sex)):

        if host_sex[i].get('class')[0] == 'member_ico1':
            host_sex[i] = '女'
        else:
            host_sex[i] = '男'
    if data is None:
        for title_, address_, rent_, image_, host_image_, host_name_, host_sex_ in zip(
                title, address, rent, image, host_image, host_name, host_sex):
            data = {
                'title': title_.get_text(),
                'address': (address_.get_text()).strip(),
                'rent': rent_.get_text(),
                'image': image_.get('src'),
                'host_image': host_image_.get('src'),
                'name': host_name_.get_text(),
                'host_sex': host_sex_
            }
            print(data)


def get_page_urls():
    urls = [
        'http://bj.xiaozhu.com/search-duanzufang-p{}-0/'.format(str(i)) for i in range(0, 30)]
    return urls


def get_url_info(url):
    global headers
    wb_data = requests.get(url, headers=headers)
    soup = BeautifulSoup(wb_data.text, 'lxml')
    urls_info = soup.select('#page_list > ul > li > a')
    for i in range(len(urls_info)):
        urls_info[i] = urls_info[i].get('href')
    return urls_info

if __name__ == '__main__':
    # get_fangzi_info('http://bj.xiaozhu.com/fangzi/5076532914.html')
    # urls=get_page_urls()
    # for url in urls:
    #     print(url)
    urls_info = get_url_info('http://bj.xiaozhu.com/search-duanzufang-p3-0/')
