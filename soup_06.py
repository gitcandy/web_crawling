# 使用BeautifuSoup爬取虎扑论坛的内容
import  requests
from  bs4 import BeautifulSoup
import datetime
from pymongo import  MongoClient
import time
import  numpy as np

url="https://bbs.hupu.com/bxj"
client=MongoClient('localhost',27017)
db = client.blog_database
collection = db.blog

'''获取URL'''
def get_url(url):
    url_list=[]
    url_list.append(url)
    for i in range(2,10):
        myurl = url+'-{}'.format(str(i))
        url_list.append(myurl)
        # print(url_list)
    return url_list

'''获取第一页到第n页的网页链接，并打开网页'''
def get_page(url):
    headers = {
        'User-Agent': 'Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/55.0.2883.87 Safari/537.36'
    }
    r=requests.get(url, headers=headers)
    soup = BeautifulSoup(r.text,'lxml')
    stop = np.random.randint(2,6,1)
    time.sleep(stop[0])
    return  soup

'''从打开的网页中爬取出所需要的信息'''
def get_data(soup):

        post_list=soup.find_all('li')
        for post in post_list:
            title_td=post.find('a',class_='truetit', style=None)
            author_td=post.find('a', class_='aulink')

            time_td = post.find('div',class_='author box')
            liulan=post.find('span', class_='ansour box')

            if title_td != None:
                data={
                    'title':title_td.text,
                    'author_name':author_td.text,
                    'reply':liulan.text.split('/')[0],
                    'view':liulan.text.split('/')[1],
                    'date':time_td.find('a',class_=None).text,
                    'href':url+title_td['href']
                }
                collection.insert_one(data)
                print('get successfully')


'''i用来显示爬取网页到第几页了'''
i=0
page_url = get_url(url)
for myurl in page_url:
    # print(myurl,'/n')
    mysoup = get_page(myurl)
    get_data(mysoup)
    i=i+1
    print(i)


'''代码调试——字符串的使用'''

# channel ='houw'
# str1 = 1
# str2 = 2
# str = 'mynameis{}{}{}/'.format(channel,str1,str2)
# print(str)







