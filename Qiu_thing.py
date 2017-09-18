# -*- coding: utf-8 -*-
'''
@author: Yalei Meng    E-mail: yaleimeng@sina.com
@license: (C) Copyright 2017, HUST Corporation Limited.
@DateTime: Created on 2017/9/18，at 20:13            '''

import time;        import random
import requests as rq
from bs4 import BeautifulSoup as bs
from urllib.request import urlretrieve as save

def requestPage(page):    #经过测试发现只要有User-Agent就能提取原始图片地址。
    head = { 'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Maxthon/5.0.4.3000 Chrome/47.0.2526.73 Safari/537.36'    }
    r = rq.get(page, timeout=3)
    return bs(r.text, 'lxml')

def  get_pics_from(car_page):
    soup = requestPage(car_page)
    links = soup.select('div.thumb  img')   #每页有25张图片
    for ele in links:
        link = 'http:'+ele.get('src')    #div.thumb > a > img
        print(link)
        if link not in all_urls:
            all_urls.add(link)


pics = ['https://www.qiushibaike.com/pic/page/{}'.format(str(n))  for n in range(1,36)]     #网站只有35页。
hots = ['https://www.qiushibaike.com/imgrank/page/{}'.format(str(n))  for n in range(1,14)] #网站只有14页。

all_urls = set()   #用集合做url去重处理。

for page in pics:              #采集糗图频道
    get_pics_from(page)
    time.sleep(random.uniform(1.2,2.1))  #在1.1到1.9之间取一个随机数

for hot in hots:                     #采集热图频道
    get_pics_from(hot)
    time.sleep(random.uniform(1.2,2.1))  #在1.1到1.9之间取一个随机数

for url in all_urls:                #保存所有图片
    pic_name = url.split('/')[-1]
    save(url,'E:/QiuShi/'+pic_name)
    print(pic_name,'\t saving Done!')  # 这是图片链接。
    time.sleep(0.3)  # 停顿0.1秒
