from downloader import *

import praw
import main
import os


class RedditDownloader:
    def __init__(self, subreddits):
        self.subreddits = subreddits
        self.reddit = praw.Reddit(user_agent=main.get_user_agent())

    def download(self):
        for subreddit in self.subreddits:
            links = subreddit.get_subreddit_links()
            for link in links:
                Downloader.download(link, subreddit.name, link.split('/')[-1])
