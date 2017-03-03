from multiprocessing import Pool
from get_url import channel_list, get_url
from get_url import url_list_all
from get_details import details_list, get_details

if __name__ == '__main__':
    pool = Pool()
    if url_list_all.find().count() < 5000:
        pool.map(get_url, channel_list.split())

    # 实现断点续传（仅details_list抓取时），将list数据类型转换
    url_list_all_s = [item['url'] for item in url_list_all.find()]
    url_list_done_s = [item['index_url'] for item in details_list.find()]
    x = set(url_list_all_s)
    y = set(url_list_done_s)
    rest_of_urls = x - y
    urls = list(rest_of_urls)
#    print(urls)

# map方法，第一个参数方法不加括号，否则报错；第二个参数需为list

    if urls:
        pool.map(get_details, urls)
