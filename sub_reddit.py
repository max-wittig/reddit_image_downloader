from download_mode import *
from image_scraper import *
from link import *
import praw
import main


class Subreddit:
    def __init__(self, name):
        self.name = name
        self.download_mode = DownloadMode.TOP
        self.limit = 10
        self.reddit = praw.Reddit(user_agent=main.get_user_agent())
        self.subreddit = self.reddit.get_subreddit(self.name)
        self.allowed_extensions = ["jpeg", "jpg", "flv", "gif", "gifv"]
        self.image_scraper = ImageScraper(self.allowed_extensions)

    """filters links based on file extension, only allow_suffix"""
    def get_filtered_links(self, links):
        filtered_links = []
        for link in links:
            suffix = link.get_file_extension()
            if suffix is not None and suffix != "":
                suffix = str(suffix).split(".")[1]
                for suf in self.allowed_extensions:
                    if suffix == suf:
                        filtered_links.append(link)
            elif (suffix is None or suffix == "") and str(link.url).find("imgur.com") > 0:
                try:
                    print("Collecting images from " + link.title)
                    for img_link in self.image_scraper.get_image_urls(link):
                        filtered_links.append(img_link)
                except Exception as ex:
                    template = "An exception of type {0} occured. Arguments:\n{1!r}"
                    message = template.format(type(ex).__name__, ex.args)
                    print(message)
        return filtered_links

    def get_submission_links(self, submissions):
        links = []
        for sub in submissions:
            if sub.url is not None:
                    title = str(str(sub).split(":: ")[1])\
                        .replace(" ", "_")\
                        .replace("/", "-")\
                        .replace(".", "")\
                        .replace("'", "_")
                    link = Link(sub.url, title)
                    links.append(link)
        return self.get_filtered_links(links)

    def get_subreddit_links(self):
        links = []
        try:
            if self.download_mode == DownloadMode.TOP:
                submissions = self.subreddit.get_top_from_all(limit=self.limit)
                links.extend(self.get_submission_links(submissions))
            elif self.download_mode == DownloadMode.HOT:
                submissions = self.subreddit.get_hot(limit=self.limit)
                links.extend(self.get_submission_links(submissions))
        except:
            print("Could not download image in " + self.name)
            "Catch forbidden error"
        finally:
            return links
