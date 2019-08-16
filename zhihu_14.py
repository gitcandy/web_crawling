import requests
from bs4 import  BeautifulSoup
from  pymongo import MongoClient
import json

# 中文乱码的可能性，使用的编码是gb2312,此时需要在获得内容后加上一句话r.encoding='gb2312
# 中文使用的是UTF-8也是乱码，网站可能使用的是gzip压缩的方式，此时使用html=r.content进行解压，然后在进行解码html.decode('UTF-8)就可以了


'''获取网页内容'''
def scrapy(link):
    headers={
        'User-Agent':'Mozilla/5.0 (Windows NT 6.1; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/69.0.3497.100 Safari/537.36',
        'authority':'api.www.zhihu.com',
        'Origin':'https://www.zhihu.com',
        'Referer':'https://www.zhihu.com/lives',
        # 'authorization':'oauth 8274ffb553d511e6a7fdacbc328e205d'
        # 'referer: https':'// www.zhihu.com / lives'
    }
    r = requests.get(link, headers=headers)
    html = r.content.decode('UTF-8')
    print(html)
    # print(r.text)


link = 'https://www.zhihu.com/lives/homefeed?includes=live'
# scrapy(link)

html = scrapy(link)
decodejson = json.load(html)
print(decodejson)
next_page = decodejson['paging']['next']
is_end = decodejson['paging']['is_end']
print(next_page,'\n')
print(is_end,'\n')
