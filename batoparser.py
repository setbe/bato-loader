from bs4 import BeautifulSoup
from PIL import Image
import requests, shutil, os

headers = {
  'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; rv:91.0) Gecko/20100101 Firefox/91.0'
}

parent_dir = os.getcwd()

class Page():
    def __init__(self, page_num, link) -> None:
        self.num = page_num
        self.link = link

    def save(self, comic_name: str, chapter_name) -> None:
        os.chdir(os.path.join("", parent_dir))
        try:
            os.makedirs(os.path.join(comic_name, chapter_name))
        except:
            pass
        os.chdir(os.path.join(comic_name, chapter_name))
        response = requests.get(self.link, stream=True)

        img = Image.open(response.raw)
        img.save(str(self.num)+".jpeg", "JPEG")

        #with open(str(self.num)+".webp", "wb") as file:
        #    shutil.copyfileobj(response.raw, file)
        del response

    def info(self) -> None:
        print("\tid: ", self.num, "\t  link: ", self.link)



class Chapter():
    def __init__(self, name, link) -> None:
        self.pages = []
        self.name = name
        self.link = link
    
    def parse(self) -> None:
        self.pages.clear()
        #requests.get("https://bato.to" + self.link, headers = headers).text
        # html = requests.get("https://bato.to/chapter/2149357", headers = headers).text
        # start_i = html.find("const imgHttpLis")
        
        # start_i = html.find("[", start_i)
        # end_i = html.find("]", start_i)

        # imgs = html[start_i:end_i]
        # print(imgs)
        # "https://xfs-210.batcg.org/comic/7006/cdd/63b919ab2c20f3655cef8ddc/23919215_720_4000_105300.webp?acc=H-0yqdzMcqpLMV3iWJIzaA&exp=1673952902"
        # "https://xfs-210.batcg.org/comic/7006/cdd/63b919ab2c20f3655cef8ddc/23919215_720_4000_105300.webp?acc=Y1PXDUKF2DJC2Fmvn6cM9A&exp=1673959973"
        html = BeautifulSoup(input(f"copypaste the {self.name}'s div tag with id \"viewer\": "), "html.parser")
        imgs = html.find_all("img", {"class" : "page-img"})
        
        for i, value in enumerate(imgs):
            p = Page(i+1, value.get("src"))
            self.pages.append(p)

    def page(self, num) -> Page:
        return self.pages[num]

    def save(self, comic_name: str) -> None:
        try:
            os.makedirs(os.path.join(comic_name, self.name))
        except:
            pass
        for i, value in enumerate(self.pages):
            value.save(comic_name, self.name)

    def info(self) -> None:
        print("\nChapter name: ", self.name, "\t  page amount: ", len(self.pages),"\t  link: ", self.link)
        for i, value in enumerate(self.pages):
            value.info()

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
        
    def save_all(self, comic_name: str) -> None:
        try:
            os.mkdir(comic_name)
        except:
            pass
        for i, value in enumerate(self.chapters):
            value.save(comic_name)