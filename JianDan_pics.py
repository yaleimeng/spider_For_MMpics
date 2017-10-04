# -*- coding: utf-8 -*-
'''
@author: Yalei Meng    E-mail: yaleimeng@sina.com
@license: (C) Copyright 2017, HUST Corporation Limited.
@desc:爬取煎蛋网妹子图
@DateTime: Created on 2017/10/4，at 14:51            '''
import time
import random
import requests as rq
from bs4 import BeautifulSoup as bs
from urllib.request import urlretrieve as save

def requestPage(page):    #经过测试发现只要有User-Agent就能提取原始图片地址。
    head = { 'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Maxthon/5.0.4.3000 Chrome/47.0.2526.73 Safari/537.36'    }
    r = rq.get(page, timeout=3)
    return bs(r.text, 'lxml')

def  get_pics_from(car_page):
    soup = requestPage(car_page)
    links = soup.select('ol.commentlist img')   #每页有30张图片
    for ele in links:
        link = 'http:'+ ele.get('org_src',ele.get('src'))
        pic_name = link.split('/')[-1]
        save(link,'E:/Joke/Jandan/'+pic_name)
        print(pic_name,'\t saving Done!')  # 这是图片链接。
        time.sleep(0.3)  # 停顿0.1秒

pages = ['http://jandan.net/ooxx/page-{}'.format(str(n))  for n in range(1,167)]   #目前只有167页。

# get_pics_from(pages[2])

for page in pages:
    get_pics_from(page)
    time.sleep(random.uniform(1.2,2.1))  #在1.1到1.9之间取一个随机数