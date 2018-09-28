#! /usr/bin/env python
#coding=GB18030
import requests
from bs4 import BeautifulSoup
import re
import sys
import time
# url='https://sh.fang.anjuke.com/fangyuan/?from=navigation'
# file = urllib.urlopen(url).read()
# file=file.decode('utf-8')
# with open('./TT','w') as tt:
#     tt.write(file)
headers={
        'User-Agent':'Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/62.0.3202.94 Safari/537.36'
        }
list=['jiading','pudong','songjiang','minhang','baoshan','qinpu','putuo','yangpu','jinshan','fengxian','xuhui','huanpu','hongkou','changning','chongming','shanghaizhoubian','huaqiao']
# for i in range(0,len(list)):
url='https://sh.fang.anjuke.com/fangyuan/%s/'%list[0]
res=requests.get(url,headers=headers)
soup=BeautifulSoup(res.text,'html.parser')
xml=soup.find_all('div',class_="filter-item")
# print(xml)
for i in xml:
    a=i.find_all('a')
#     print(a)
    for p in a:
#         print(p.text)
#         Price=r'^\d+\D*\d*\w'
        Price=r'\d+\D?\d*\w*'
        if re.findall(Price,p.text):
            print(re.findall(Price,p.text)[0])


# addr=soup.find_all('dl',class_="F-info")
# print(addr)
# total=[]
# for i in addr:
#     total.append(i.a.text)
#     print(i.a.text)
# print(len(total))
#价格
# p=[]
# price=soup.find_all('div',class_="F-price")
# # print(price)
# for i in price:
#     if i:
#         p.append(i.em.text)
#         print(i.em.text)
# print(len(p))
# patt='<em>\d*</em>'
# re.findall(patt, price)
#     t1=list[i]
#     with open(t1,'w') as tt:
#         tt.write(soup)
#     pattern=r'<em>\d*</em>'
#     if re.findall(pattern, soup):
#         print(list[i],re.findall(pattern, soup))
#     else:
#         print(list[i])




# def use_proxy(proxy_addr,url):
#     proxy=urllib2.ProxyHandler({'http':proxy_addr})
#     opener=urllib2.build_opener(proxy,urllib2.HTTPHandler)
#     urllib2.install_opener(opener)
#     req = urllib2.Request(url)
#     req.add_header('User-Agent':'Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/62.0.3202.94 Safari/537.36')
#     data=urllib2.urlopen(url).read().decode('utf8')
#     return data
# 
# proxy_addr='61.163.39.70:9999'
# data=use_proxy(proxy_addr,'https://sh.fang.anjuke.com/fangyuan/jiading/')
# print data



# list=['jiading','pudong','songjiang','minhang','baoshan','qinpu','putuo','yangpu','jinshan','fengxian','xuhui','huanpu','hongkou','changning','chongming','shanghaizhoubian','huaqiao']
# for i in range(0,len(list)):
#     url2='https://sh.fang.anjuke.com/fangyuan/%s/'%list[i]
#     file = urllib.urlopen(url2).read()
#     file=file.decode('utf-8')
#     t1=list[i]
#     with open(t1,'w') as tt:
#         tt.write(file)
#     pattern=r'<em>\d*</em>'
#     if re.findall(pattern, file):
#         print list[i],re.findall(pattern, file)
#     else:
#         print list[i]
#     time.sleep(5)
