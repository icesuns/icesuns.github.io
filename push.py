#coding:utf-8
import requests
import time
from bs4 import BeautifulSoup as bp

print unicode('www.zicesun.com 自动推送开启....','utf-8')
time.sleep(0.5)
site_url = 'http://www.zicesun.com/baidusitemap.xml'

try:
    print unicode('zicesun 获取sitemap链接....','utf-8')
    data_ = bp(requests.get(site_url).content,'lxml')
except Exception, e:
    print e

list_url=[]

def get_(data):
    headers={'User-Agent':'curl/7.12.1 ',
             'Content-Type':'text/plain '}
    try:
        r = requests.post(url='http://data.zz.baidu.com/urls?site=www.zicesun.com&token=wUbVaP5YIPFU8QRv',data=data)
        print r.status_code
        print r.content
    except Exception, e:
        print e

print '---------------------------------'
for x,y in enumerate(data_.find_all('loc')):
    print x,y.string
    list_url.append(y.string.replace('http://','http://www.'))

print '---------------------------------'

print unicode('zicesun.com 开始推送....','utf-8')

for x in list_url:
    print unicode('zicesun.com 当前推送条目为:','utf-8') + x
    get_(x)

