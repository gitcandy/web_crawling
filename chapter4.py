#爬取豆瓣电影Top25信息
import requests
from bs4 import  BeautifulSoup
import time
import re

def get_movie_state():
    headers = {
        'user-agent':'Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/55.0.2883.87 Safari/537.36',
        'Referer':'https://movie.douban.com/top250'
    }

    for i in range(0,1):
        url = 'https://movie.douban.com/top250?start='+str(i*25)+'&filter='
        r=requests.get(url, headers=headers)
        print(str(i),"页面响应码为：",r.status_code)
        # print(r.text)
    return r

def get_movies():
    headers = {
        'user-agent': 'Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/55.0.2883.87 Safari/537.36',
        'Referer': 'https://movie.douban.com/top250'
    }
    movie_name_list = []
    movie_names=[]
    for i in range(0,10):
        url = 'https://movie.douban.com/top250?start=' + str(i * 25) + '&filter='
        r = requests.get(url, headers=headers)
        soup=BeautifulSoup(r.text,'lxml')
        movie_name=soup.find_all("span",class_="title")
        # movie_name=soup.select('div.hd > a > span:nth-of-type(1)').text.strip()
        movie_name_list+=movie_name
        # print(movie_name)
        # print(type(movie_name_list))

        time.sleep(3)

    for i in range(0,len(movie_name_list)):
        print(movie_name_list[i],"/n")

            # with open("D/test.txt", "a") as f:
            #     f.write(str1)
            #     f.close()
    #
    #     if (i%2==0&i<5):
    #         print("第", i, "名电影：", movie_name_list[i], "/n")
    #
    #     if i%2==1&i>7:
    #          print("第",i,"名电影：",movie_name_list[i],"/n")
    #     i += 1






# get_movies()
# path="D//test.txt"
# str1=["hello,world!!%[545世界]","jsjklfjdj","<<<<我的世界"]
# for i in range(1,len(str1)):
    # str = re.match(u"[\u4e00-\u9fa5]+", str1[i])
    # str = re.sub("[A-Za-z0-9\!\%\[\]\,\。]", "", str1[0])
    # if str != "":
    #     print(str1[i])
#         with open(path,'a') as f:
#             f.write(str)
#             print("sucssece")
#             f.close()

# # # print(type(str1))
str2="hello,world!!%/\"[545世界]?//"
str = re.sub("[A-Za-z0-9\!\%\[\]\,\。\<\>\#\?\/]", "", str2)
print(str)