from bs4 import BeautifulSoup
import requests



class Page():
    def __init__(self, this_page_num, link) -> None:
        self.page = this_page_num
        self.link = link



class Chapter():
    def __init__(self, name, link) -> None:
        self.pages = []
        self.name = name
        self.link = link
    
    def page(self, num) -> Page:
        return self.pages[num]



class Parser():
    def __init__(self) -> None:
        self.chapters = []

    def parse(self, url: str) -> None:
        self.chapters.clear()
        soup = BeautifulSoup(requests.get(url).text, "html.parser")

        chapter_list_raw = soup.find('div', {'class': 'episode-list'})

        chapter_list = chapter_list_raw.find_all('a', {'class': 'chapt'})

        for i, value in enumerate(chapter_list):
            c = Chapter(name = value.text.strip(), link = value.get("href"))
            self.chapters.append(c)

    def parse_chapter(self, url: str) -> Chapter:
        chap = Chapter()