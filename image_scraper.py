from bs4 import BeautifulSoup
from link import Link
import requests
import json


class ImageScraper:
    def __init__(self, allowed_file_ext):
        self.allowed_file_ext = allowed_file_ext

    def get_html(self, url):
        return requests.get(url).content

    def build_real_source(self, img, title):
        if str(img).startswith("//"):
            img = "http:" + img
        link = Link(img, title)
        for ext in self.allowed_file_ext:
            if link.get_file_extension() == "." + ext:
                return link
        return None

    def is_already_in_links(self, links, link):
        for current_link in links:
            if current_link.url == link.url:
                return True
        return False

    def get_image_urls(self, link):
        links = []
        soup = BeautifulSoup(self.get_html(link.url), "html.parser")
        i = 1
        for images in soup.find_all('img'):
            img = images.get('src')
            if img is not None and img != "":
                new_link = self.build_real_source(img, (link.title + "(" + (str(i)) + ")"))
                if new_link is not None and new_link.title is not None \
                        and not self.is_already_in_links(links, new_link):
                    links.append(new_link)
                    i = i + 1
        return links
