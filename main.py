#-*-coding:utf-8 -*-

import urllib.request
from bs4 import BeautifulSoup
import Directory
import Spider
import ChapterContentCrawling as ccc

class Main():
    ''' 主函数, 通过调用其它模块来完成爬取书籍'''
    def __init__(self, bookName = None):
        self.bookName = bookName

    def startCrawl(self):
        if self.bookName == None:
            print("请输入参数")
        else:
            dirUrl = Directory.DirSearcher(self.bookName).search()
            if dirUrl == None:
                print("没有这本书")
                return
            links = Spider.Spi(dirUrl).search()
            with open(self.bookName + ".txt", "w") as book:
                for link in links:
                    cc = ccc.ConCraw(link).crawling(book)

if __name__ == "__main__":
    book = Main("魔临")  #传给Main类的字符串参数为书籍名，不允许错
    book.startCrawl()
    