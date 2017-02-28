from bs4 import BeautifulSoup
import requests
import time
import pymongo

# 从get_urls中获取到每一个详细房源的url再针对每一个房源详细页面进行抓取，将房源信息存放如details_list表中
headers = {
    'User_Agent':'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/55.0.2883.87 Safari/537.36',
    'Cookie':'abtest_ABTest4SearchDate=b; xzuuid=96037454; newcheckcode=18df5924227e28fb6c875a533cea4732; xzuinfo=%7B%22user_id%22%3A7713801415%2C%22user_name%22%3A%2218819473745%22%2C%22user_key%22%3A%224fe689cc43%22%7D; xzucode=595b89c0b95de0bc0329614f15fe404d; xzucode4im=f7fd0a5d60d2db7703faa8473383e855'
}


# 创建数据库并获取数据库表单
client = pymongo.MongoClient('localhost', 27017)
xiaozhu = client['xiaozhu']
details_list = xiaozhu['details_list']


# 获取房源信息
def get_details(url=None):
    if url is None:
        pass
    else:
        web_data = requests.get(url, headers=headers)
        time.sleep(2)
        soup = BeautifulSoup(web_data.text, 'lxml')
        names = soup.select('div.pho_info > h4 > em')
        addresses = soup.select('div.pho_info > p > span')
        daily_rents = soup.select('div.day_l')
        images = soup.select('#curBigImage')
        lorder_names = soup.select('#floatRightBox > div.js_box.clearfix > div.w_240 > h6 > a')
        lorder_images = soup.select('#floatRightBox > div.js_box.clearfix > div.member_pic > a > img')
        lorder_sexes = soup.select('#floatRightBox > div.js_box.clearfix > div.member_pic > div')
        citys = soup.select('div.con_l > div.pho_info > p > em > a:nth-of-type(2)')

        for city, name, address, daily_rent, image, lorder_name, lorder_image, lorder_sex in zip(citys, names, addresses, daily_rents, images, lorder_names, lorder_images, lorder_sexes):
            data = {
                'index_url': url,
                'city': city.get_text(),
                'name': name.get_text(),
                'address': address.get_text(),
                'daily_rent': daily_rent.get_text(),
                'image': image.get('src'),
                'lorder_name': lorder_name.get_text(),
                'lorder_image': lorder_image.get('src'),
                'lorder_sex': lorder_sex.get('class')
            }
            if data['lorder_sex'] == ['member_ico1']:
                data['lorder_sex'] = '女'
            else:
                data['lorder_sex'] = '男'

    #       房间详细信息数据写入数据库
            details_list.insert_one(data)








#        print(data)
#        file = open('C:/Users/3437/Desktop/room_details.txt', 'a', -1, 'GB18030')
#        file.write(str(data)+'\n')
#        file.close()









