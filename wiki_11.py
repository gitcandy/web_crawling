# 爬取维基百科的内容
import requests
from bs4 import  BeautifulSoup
from  pymongo import  MongoClient
import  time
import re


time1 = time.time()
exist_url = []
g_writecount = 0

def scrappy(url,depth=1):
    global g_writecount
    try:
        link = "https://en.wikipedia.org/wiki/"
        headers = {
            'User-Agent': 'Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/55.0.2883.87 Safari/537.36'
        }
        r = requests.get(link+url,headers=headers)
        html = r.text
        # print("get pages")
    except Exception as e:
        print('Fail downloading and saviing',url)
        print(e)
        exist_url.append(url)
        return  None
    exist_url.append(url)
    link_list = re.findall('<a href="/wiki/([^:#=<>]*?)".*?</a>',html)
    # print(link_list)
    unique_list = list(set(link_list)-set(exist_url))

    for eachone in unique_list:
        g_writecount +=1
        output ="No."+ str(g_writecount)+"\t Depth:"+str(depth)+"/t"+url+'->'+eachone+'/n'
        print(output)
        with open('E:/title.txt',"a+") as f:
            f.write(output)
            # print("Successfuly insert")
            f.close()
        if depth < 2:
            scrappy(eachone,depth+1)

# scrappy("Wikipedia")
# time2 = time.time()
# print("Total time", time2-time1)




# str1='<a href="/wiki/#woiddd">afjjljlj</a>'
# str2=re.findall('<a href="/wiki/([^:#=<>]*?)".*?</a>',str1)
# print(str2)