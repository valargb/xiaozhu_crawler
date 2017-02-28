import time
from get_url import url_list_all
from get_details import details_list


# 5秒显示以此urls_list和details_list中的房源数量，便于实时监控
def counts():
    while True:
        print("urls:"+str(url_list_all.find().count()))
        print("details:"+str(details_list.find().count()))
        time.sleep(5)

counts()

