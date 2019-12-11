#-*-coding:utf-8 -*-

import urllib.request
from bs4 import BeautifulSoup
import re

class ConCraw():
    def __init__(self, url):
        self.url = url
    def crawling(self, book):
        header = {"User-Agent":"Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/78.0.3904.70 Safari/537.36"}
        page = urllib.request.Request(self.url, headers = header)
        # print(self.url)
        pageInfo = urllib.request.urlopen(page)
        pageInfo = pageInfo.read().decode("gbk")
        # print(pageInfo)
        soup = BeautifulSoup(pageInfo, "html.parser")
        content = soup.find(class_="chapter-content")
        s = re.compile(r"(<[\s\S]*?script&gt;)|(<[\s\S]*?>)|(一秒记住【笔趣阁小说网 www.bqg34.com】，精彩小说无弹窗免费阅读！)")  #通过正则表达式来把爬取的内容中不需要的成分去掉
        cont = content.prettify()
        cont = s.sub("", cont)
        cont = "    " + soup.find("h1").string + cont
        book.write(cont)
        