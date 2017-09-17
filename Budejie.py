# -*- coding: utf-8 -*-
'''@author: Yalei Meng    E-mail: yaleimeng@sina.com
   @DateTime: Created on 2017/9/16，at 7:55            '''
import time
import random
import requests as rq
from bs4 import BeautifulSoup as bs
from urllib.request import urlretrieve as save

def requestPage(page):    #经过测试发现不设置User-Agent也能提取原始图片地址。
    r = rq.get(page, timeout=3)
    return bs(r.text, 'lxml')

def  get_pics_from(car_page):
    soup = requestPage(car_page)
    links = soup.select('div.j-r-list-c-img > a > img')   #每页有20张图片
    for ele in links:
        link = ele.get('data-original')
        print(link)
        pic_name = link.split('/')[-1]
        save(link,'E:/Joke/Budejie/'+pic_name)
        print(pic_name,'\t saving Done!')  # 这是图片链接。
        time.sleep(0.3)  # 停顿0.3秒

pages = ['http://www.budejie.com/pic/{}'.format(str(n))  for n in range(1,51)]   
# 1000幅图。该网站只允许访问前50页。
for page in pages:
    get_pics_from(page)
    time.sleep(random.uniform(1.2,2.1))  #在1.1到1.9之间取一个随机数
