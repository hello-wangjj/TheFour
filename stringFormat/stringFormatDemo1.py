#!python3
# -*- coding: utf-8 -*-
from string import punctuation
import re
__author__ = 'wangjj'
__mtime__ = '2016112612:49'
c = ['2015.12.29', '2016-01-12']
print(punctuation)
r = '[’!"#$%&\'()*+,-./:;<=>?@[\\]^_`{|}~]+'
r2='[!"#$%&\'()\*\+,-./:;<=>?@\[\\]^_`{|}~]+'
pun = set(punctuation)
print(pun)
for i in range(len(c)):
    print(c[i])
    print(''.join(ch for ch in c[i] if ch not in pun))
    print(re.sub(r2, '.', c[i]))
