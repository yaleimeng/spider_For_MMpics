# -*- coding: utf-8 -*-
'''
@author: Yalei Meng    E-mail: yaleimeng@sina.com
@license: (C) Copyright 2017, HUST Corporation Limited.
@desc:从百思不得其解网站获取前面几页的图片。
@DateTime: Created on 2017/9/5，at 13:06            '''
from bs4 import BeautifulSoup
import requests as rq
import  time
import  re
import urllib.request  as urq
import random

home = 'http://www.neihan.net/'    #抓取最新栏目下的50页
#sites = [home+'_{}.html'.format(str(i)) for i in range(1,50)]
sites = [home+'index_{}.html'.format(str(i)) for i in range(12,51)]
ua = 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/62.0.3192.0 Safari/537.36'

head = {'User-Agent':ua}
links = []
folder_path = 'E:/Joke/'
def get_A_page(url):
    r = rq.get(url)
    soup = BeautifulSoup(r.text, 'lxml')
    imgs = soup.select('dl.main-list > dd.content.content-pic > p > img')
    #先用select（‘选择器’）选择符合要求的所有标签。然后在容器里迭代获取出具体属性或文本。
    for img in  imgs:
        if img['src'][0:8] == '/Uploads':
            link = 'http://www.neihan.net' + img['src']
        else:
            link = img['src']
        links.append(link)
    print("A page done！ %d pics got!"%len(imgs))

rgexp = re.compile('\d{8,15}\.\w{3,5}')         #查找数字.webp
def savePicList(data):
    for link in data:
        if re.search(rgexp,link) is not None:#把收集到的网络图片保存到指定文件夹。
            name = re.search(rgexp,link).group()     #然后再查找“数字+扩展名”。
            urq.urlretrieve(link,folder_path+name)   #第2个参数是路径+文件名。确保/不能缺少或重复
            print(name + '\tsaving finished!')
            #time.sleep(0.8)                          #保存1个文件之后，休眠0.8秒。
total =0
for st in sites:
    get_A_page(st)
    total += len(links)
    savePicList(links)  #把links里面的图片保存到本地硬盘。
    links.clear()       #清空links列表。
    time.sleep(random.uniform(0.5,2.1))
    print('\t\t目前已收集图片：%d张。'%total)