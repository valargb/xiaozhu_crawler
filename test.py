from bs4 import BeautifulSoup
import requests
import time

headers = {
    'User_Agent':'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/55.0.2883.87 Safari/537.36',
    'Cookie':'abtest_ABTest4SearchDate=b; xzuuid=96037454; newcheckcode=18df5924227e28fb6c875a533cea4732; xzuinfo=%7B%22user_id%22%3A7713801415%2C%22user_name%22%3A%2218819473745%22%2C%22user_key%22%3A%224fe689cc43%22%7D; xzucode=595b89c0b95de0bc0329614f15fe404d; xzucode4im=f7fd0a5d60d2db7703faa8473383e855'
}

web_data = requests.get('http://sanya.xiaozhu.com/fangzi/3863028529.html', headers=headers)
time.sleep(2)
soup = BeautifulSoup(web_data.text, 'lxml')
citys = soup.select('div.con_l > div.pho_info > p > em > a:nth-of-type(2)')


for city in citys:
    print(city.get_text())

