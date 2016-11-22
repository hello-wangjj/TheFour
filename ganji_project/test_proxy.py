#!python3
# -*- coding: utf-8 -*-
import requests
__author__ = 'wangjj'
__mtime__ = '2016112220:35'
headers = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 6.1; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/53.0.2785.116 Safari/537.36',
}
# proxies='http://www.xicidaili.com/nn/
proxy_list=[
    'http://124.88.67.63:80',
    'http://218.106.205.145:8080',
    'http://122.5.227.57:8888',
]

for proxy_ip in proxy_list:
    proxy = {
        'http': proxy_ip
    }
    test_url = 'http://hz.ganji.com/wu/'
    try:
        res = requests.get(
            test_url,
            proxies=proxy,
            headers=headers,
            timeout=3)
        print(proxy)
        print(res.status_code)
    except Exception as e:
        print(proxy)
        print(e)
