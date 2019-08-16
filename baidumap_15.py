import  requests
from  bs4 import  BeautifulSoup
import  json
def getjson(loc,page_num=0):
    headers = {
        'User-Agent':'Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/55.0.2883.87 Safari/537.36',
    }
    pa={
        'q':'公园',
        'region':loc,
        'scope':'2',
        'page_size':20,
        'page_num':page_num,
        'out_put':'json',
        'ak':'ARkegiN6DXFPyIFq8SBzjnDB6a7GKy62'
    }

    r=requests.get("http://api.map.baidu.com/place/v2/search",params=pa,headers=headers)
    print(r.text)
    # soup = BeautifulSoup(r.text,'lxml')
    # park_list = soup.find_all('name')
    # adrress_list = soup.find_all('address')
    #
    # for i in (0,len(park_list)):
    #     print(park_list[i],adrress_list[i],'\n')


    # decodejson = json.loads(r.text)
    # return (decodejson)
getjson('北京市')
# print(r)