#-*-coding:utf-8 -*-

import urllib.request
from bs4 import BeautifulSoup



class DirSearcher():
    def __init__(self, bookName = None):
        self.bookName = bookName
    
    def search(self):
        url = url = "https://www.bqg34.com/modules/article/search.php?searchkey=" + self.bookName +"&submit=搜索"
        url = urllib.request.quote(url, safe=";/?:@&=+$,", encoding="gbk")
        header = {"User-Agent":"Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/78.0.3904.70 Safari/537.36"}
        page = urllib.request.Request(url, headers = header)

        pageInfo = urllib.request.urlopen(page).read().decode("gbk")
        soup = BeautifulSoup(pageInfo, "html.parser")

        title = soup.find("title")
        if title.string == "笔趣阁小说网":
            books = soup.find_all("tr")
            for book in books:
                if book.find("a") != None:
                    bookName = book.find_all("a")[0].attrs["title"]
                    if bookName == self.bookName:
                        return book.find("a").attrs["href"]
        elif title.string.find(self.bookName) != -1:
            return soup.find("link").attrs["href"]



if __name__ == "__main__":
    dirSea = DirSearcher("网游之纵横天下")
    print(dirSea.search())