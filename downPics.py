# -*- coding: utf-8 -*-
'''
@author: Yalei Meng    E-mail: yaleimeng@sina.com
@license: (C) Copyright 2017, HUST Corporation Limited.
@DateTime: Created on 2017/9/13，at 15:00            '''
from bs4 import BeautifulSoup as bs
import requests as  rq
import os
import time
import random

def getPageList(url):
    r = rq.get(url, headers=head, timeout=10)
    soup = bs(r.content, 'lxml')  # 因为文字编码问题，不能使用text，而必须是content
    lastPage = soup.select('div.pagenavi span')[-2].text
    maxN = int(lastPage)
    pagelist = [url+ '/{}'.format(str(i))  for i in range(1,maxN+1) ]
    pic = soup.find('div', class_='main-image').find('img')['alt']
    path = 'E:/Joke/'+pic+'/'
    os.makedirs(path,exist_ok=True)
    #print(pagelist)               #打印探测到的页面链接清单。比如1--49页。
    return pagelist, path


def  get_pic_in_One(page,folder_path ):
    r = rq.get(page,headers = head, timeout=3)
    soup = bs(r.text, 'lxml')
    link =soup.find('div',class_='main-image').find('img')['src']
    name = link.split('/')[-1]
    r = rq.get(link,headers = head, timeout=5)   #这里用了Header，从站内进行引用，避免了反盗链封锁
    with open(folder_path+name, "wb") as f:      #如果使用urllib的urlretrieve（）则会下再到假图片。
        f.write(r.content)
    print(name + '\tsaving finished!')



ub = 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/62.0.3192.0 Safari/537.36'
ua = 'Mozilla/5.0 (Windows NT 6.1;) AppleWebKit/532.5 (KHTML, like Gecko) Safari/532.5'
head = {'User-Agent': ua, 'Referer':'http://www.mzitu.com/102712'}    #请求头增加了Refer，避免了反盗链困扰。


#单个系列图片链接的批量下载。
testP = 'http://www.mzitu.com/102712/'    #可以任选一个链接爬取

urls,dir = getPageList(testP)
for one in urls:
    get_pic_in_One(one,dir)
    time.sleep(random.uniform(0.8,1.9))


#从csv文件批量读取链接列表，全部下载。[图片总量有9 GB，慎重。。]
# pages = []                                 #这是所有专场的url地址。
# with open('E:/Meizitu_URLs.txt', 'r', encoding='utf-8')as f:
#     for line in f.readlines():         #按整行依次读取数据。
#         link = line.replace("\n",'')   #把回车符号替换为空。这样网址就是可访问的。
#         urls.append(link)
#
# for page in pages:
#     urls, dir = getPageList(page)
#     for one in urls:
#         get_pic_in_One(one, dir)
#         time.sleep(random.uniform(0.8, 1.9))
