#!python3
# -*- coding: utf-8 -*-
from bs4 import BeautifulSoup
import requests
__author__ = 'wangjj'
__mtime__ = '2016112220:30'
start_url = 'http://hz.ganji.com/wu/'
host_url = 'http://hz.ganji.com'
headers = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 6.1; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/53.0.2785.116 Safari/537.36',
}


def get_index_url(url):
    global headers
    wb_data = requests.get(url, headers=headers)
    soup = BeautifulSoup(wb_data.text, 'lxml')
    links = soup.select('dl.fenlei > dt > a')
    for link in links:
        page_url = host_url + link.get('href')
        print(page_url)

channel_list = '''
http://hz.ganji.com/jiaju/
http://hz.ganji.com/rirongbaihuo/
http://hz.ganji.com/shouji/
http://hz.ganji.com/shoujihaoma/
http://hz.ganji.com/bangong/
http://hz.ganji.com/nongyongpin/
http://hz.ganji.com/jiadian/
http://hz.ganji.com/ershoubijibendiannao/
http://hz.ganji.com/ruanjiantushu/
http://hz.ganji.com/yingyouyunfu/
http://hz.ganji.com/diannao/
http://hz.ganji.com/xianzhilipin/
http://hz.ganji.com/fushixiaobaxuemao/
http://hz.ganji.com/meironghuazhuang/
http://hz.ganji.com/shuma/
http://hz.ganji.com/laonianyongpin/
http://hz.ganji.com/xuniwupin/
http://hz.ganji.com/qitawupin/
http://hz.ganji.com/ershoufree/
http://hz.ganji.com/wupinjiaohuan/
'''

if __name__ == '__main__':
    get_index_url(start_url)
