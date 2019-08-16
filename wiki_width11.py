# 进行多线程爬取
import  threading
import  requests
import re
import  time

g_mutex = threading.Condition()
g_pages = []  #解析出的URL链接
g_queueURL = [] #等待爬取的URL
g_existURL = []  #已经爬取的URL
g_writecount = 0 #找到的链接数
class Crawler:
    '''初始化爬虫类'''
    def __init__(self, url, threadnum):
        self.url = url
        self.threadnum = threadnum
        self.threadpool = []

    ''' 爬虫的控制大脑，包括爬取网页，更新队列'''
    def craw(self):
        global g_queueURL
        g_queueURL.append(url)
        depth=1
        while (depth < 3):
            print('Searching depth ', depth, '...\n')
            self.downloadAll()
            self.updateQueueURL()
            g_pages = []
            depth += 1

    '''调用多线程爬虫，在小于线程最大值和没爬完队列之前会增加线程'''
    def downloadAll(self):
        global  g_queueURL
        i = 0
        while i<len(g_queueURL):
            j=0
            while j<self.threadnum and i+j <len(g_queueURL):
                threadresult = self.download(g_queueURL[i+j],j)
                j+=1
            i+=j
            for thread in self.threadpool:
                thread.join(30)
            threadpool = []
            g_queueURL = []

    '''调用多线程爬虫'''
    def download(self,url,tid):
        crawthread =CrawlerThread(url,tid)
        self.threadpool.append(crawthread)
        crawthread.start()

    '''完成一个深度的爬虫之后更新队列'''
    def updateQueueURL(self):
        global  g_queueURL
        global  g_existURL
        newUrlList = []
        for content in g_pages:
            newUrlList += self.getUrl(content)
            g_queueURL = list(set(newUrlList)-set(g_existURL))

    '''从获取的网页中解析URL'''
    def getUrl(self,content):
        link_list = re.findall('<a href="/wiki/([^:#=<>]*?)".*?</a>',content)
        unique_list=list(set(link_list))
        return  unique_list

'''爬虫线程'''
class CrawlerThread(threading.Thread):
    def  __init__(self,url,tid):
        threading.Thread.__init__(self)
        self.url = url
        self.tid =tid

    def run(self):
        global g_mutex
        global  g_writecount
        link = "https://en.wikipedia.org/wiki/"
        try:
            print(self.tid,"crawl",self.url)
            headers = {
                'User-Agent': 'Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/55.0.2883.87 Safari/537.36'
            }
            r = requests.get(url=link+self.url,headers=headers)
            html = r.text
            link_list2 = re.findall('<a href="/wiki/([^:#=<>]*?)".*?</a>',html)
            unique_list = list(set(link_list2))
            for eachone in unique_list:
                g_writecount +=1
                content2 = "No."+ str(g_writecount)+"\t Thread:"+str(self.tid)+"\t"+self.url+'->'+eachone+'\n'
                with open('E:/title2.txt',"a+") as f:
                    f.write(content2)
                    f.close()
        except Exception as e:
            g_mutex.acquire()
            g_existURL.append(self.url)
            g_mutex.release()
            print("Failed downloading and saving",self.url)
            print(e)
            return None
        g_mutex.acquire()
        g_pages.append(html)
        g_existURL.append(self.url)
        g_mutex.release()

if __name__ == "__main__":
    url ="Wikipedia"
    threadnum=5
    crawler =Crawler(url,threadnum)
    crawler.craw()





