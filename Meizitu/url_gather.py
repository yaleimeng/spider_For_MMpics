# # -*- coding: utf-8 -*-
# '''
# @author: Yalei Meng    E-mail: yaleimeng@sina.com
# @license: (C) Copyright 2017, HUST Corporation Limited.
# @DateTime: Created on 2017/9/13，at 14:43            '''
# from bs4 import BeautifulSoup as bs
# import requests as  rq
# import time
# import random
#
# def  get_session_from(top):
#     r = rq.get(top)
#     soup = bs(r.text, 'lxml')
#     arts = soup.select('ul.archives li  a')  # 在页面中找到下一层链接的位置
#     with open('E:/Meizitu_URLs.txt', 'a', encoding='utf-8')as f:
#         for art in arts:
#             link = art.get('href')
#             out.append(link)
#             f.write(link)
#             f.write("\n")
#             print(art.text,link)
#
# out = []
# host = 'http://www.mzitu.com/all/'
#
# get_session_from(host)
#
# print('目前已写入 %d个链接。！' % len(out))
# #print('\n全部链接写入完成！\n程序结束！')
