#!/usr/bin/env python
# -*- coding: utf-8 -*-
import requests
from bs4 import BeautifulSoup
__author__ = 'wangjj'
__mtime__ = '20161111下午 4:27'
headers = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 6.1; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/53.0.2785.116 Safari/537.36',
}
def get_proxy():
    global headers
    base_url = [
        'http://www.xicidaili.com/nn/{}'.format(str(i)) for i in range(1, 10)]
    wb_data = requests.get(base_url[0], headers=headers)
    soup = BeautifulSoup(wb_data.text, 'lxml')
    countries = soup.select('td.country > img')
    ip_ports = []
    for country in countries:
        ip = country.find_next('td')
        port = ip.find_next('td')
        # data = {
        #     '国家': country.get('alt'),
        #     'ip': ip.get_text(),
        #     'port': port.get_text()
        # }
        ip_port = ip.get_text() + ':' + port.get_text() + \
            ' ' + country.get('alt') + '\n'
        ip_ports.append(ip_port)
    with open('proxy.txt', 'w') as f:
        for i in ip_ports:
            f.write(i)
        f.close()


def test_proxy():
    test_url = 'http://ip.chinaz.com/getip.aspx'
    global headers
    proxies = []
    useful_proxies=[]
    with open('proxy.txt', 'r') as f:
        lines = f.readlines()
        for line in lines:
            ip_port = 'http://' + (line.strip()).split(' ')[0]
            proxy = {
                'http': ip_port
            }
            # print(proxy)
            proxies.append(proxy)
        f.close()
    for proxy in proxies:
        try:
            print(proxy)
            res = requests.get(
                test_url,
                proxies=proxy,
                headers=headers,
                timeout=2).text
            print(res)
            useful_proxies.append(proxy)
            with open('useful_proxy.txt', 'w') as file:
                file.write(proxy['http'])
                file.write('\n')
                file.close()
        except Exception as e:
            print(proxy)
            print(e)
            continue
    return useful_proxies
if __name__ == '__main__':
    get_proxy()
    test_proxy()