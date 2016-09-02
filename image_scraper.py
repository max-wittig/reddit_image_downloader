from bs4 import BeautifulSoup
from link import Link
import requests



class ImageScraper:
    def __init__(self):
        pass

    def get_html(self, url):
        return requests.get(url).content

    def build_real_source(self, img, allowed_file_ext, title):
        if str(img).startswith("//"):
            img = "http:" + img
        link = Link(img, title)
        for ext in allowed_file_ext:
            if link.get_file_extension() == "." + ext:
                return link
        return None

    def get_image_urls(self, link, allowed_file_ext):
        links = []
        soup = BeautifulSoup(self.get_html(link.url), "html.parser")
        i = 1
        for images in soup.find_all('img'):
            img = images.get('src')
            link = self.build_real_source(img, allowed_file_ext, (link.title+"("+str(i)+")"))
            if link is not None:
                i = i + 1
                links.append(link)
        return links
