import requests
from bs4 import BeautifulSoup
import pymongo
import time

# 存放18个热门城市的url，先抓取每一个城市的所有详细房源的url存放到url_list表中
channel_list = '''
http://bj.xiaozhu.com/
http://sh.xiaozhu.com/
http://gz.xiaozhu.com/
http://cd.xiaozhu.com/
http://sanya.xiaozhu.com/
http://xm.xiaozhu.com/
http://sz.xiaozhu.com/
http://cq.xiaozhu.com/
http://hz.xiaozhu.com/
http://km.xiaozhu.com/
http://dali.xiaozhu.com/
http://lijiang.xiaozhu.com/
http://xa.xiaozhu.com/
http://hrb.xiaozhu.com/
http://zhuhai.xiaozhu.com/
http://nj.xiaozhu.com/
http://wh.xiaozhu.com/
http://su.xiaozhu.com/
'''

headers = {
    'User_Agent':'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/55.0.2883.87 Safari/537.36',
    'Cookie':'abtest_ABTest4SearchDate=b; xzuuid=96037454; newcheckcode=18df5924227e28fb6c875a533cea4732; xzuinfo=%7B%22user_id%22%3A7713801415%2C%22user_name%22%3A%2218819473745%22%2C%22user_key%22%3A%224fe689cc43%22%7D; xzucode=595b89c0b95de0bc0329614f15fe404d; xzucode4im=f7fd0a5d60d2db7703faa8473383e855'
}


client = pymongo.MongoClient('localhost', 27017)
xiaozhu = client['xiaozhu']
url_list_all = xiaozhu['url_list']


# 获取每页链接
def get_url(channel):
    for i in range(1, 13, 1):
        url = channel+'search-duanzufang-p'+str(i)+'-0/'
        web_data = requests.get(url, headers=headers)
        soup = BeautifulSoup(web_data.text, 'lxml')
        url_details = soup.select('#page_list > ul > li > a')
        time.sleep(2)
        for url_detail in url_details:
            url = url_detail.get('href')
            url_list_all.insert_one({'url': url})

