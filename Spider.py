#-*-coding:utf-8 -*-

import urllib.request
from bs4 import BeautifulSoup


class Spi():
    def __init__(self, dirUrl):
        self.url = dirUrl
        self.links = []

    def search(self):
        header = {"User-Agent":"Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/78.0.3904.70 Safari/537.36"}
        page = urllib.request.Request(self.url, headers = header)
        # print(self.url)
        pageInfo = urllib.request.urlopen(page)
        pageInfo = pageInfo.read().decode("gbk")
        # print(pageInfo)
        soup = BeautifulSoup(pageInfo, "html.parser")
        links = soup.find_all("ul")[1].find_all("a")
        for link in links:
            self.links.append(self.url + link.attrs["href"])
        return self.links

if __name__ == "__main__":
    s = Spi("https://www.bqg34.com/book_47294/")
    links = s.search()
    for link in links:
        print(link)