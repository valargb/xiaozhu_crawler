# xiaozhu_crawler

基于Python的小猪短租网热门城市房源爬取：

利用Python爬虫爬取小猪短租网全国18个热门城市的短租房源，获取每一个城市的短租房房间名字，照片，地理位置，所在城市，价格等，房主昵称，性别等，具体内容如下：

1.观察需爬取的页面特征，检查网页元素属性，确定代码工作流程和方法；

2.利用requests模块向服务器请求网页内容，利用BeautifulSoup模块从获取到的html页面中抓取数据；--geturls,get_details

3.利用pymongo模块，爬取到的数据存放进本地的MongoDB数据库中；

4.利用multiprocessing的Pool模块，实现多进程爬取，提升爬取效率；

5.实现断点续传；--main

6.编写本地数据库监控程序，实时监控爬取到的数据量。--counts

