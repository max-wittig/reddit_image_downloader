from downloader import *
import praw
import main


class RedditDownloader:
    def __init__(self, subreddits):
        self.subreddits = subreddits
        self.reddit = praw.Reddit(user_agent=main.get_user_agent())
        self.running = True

    def download(self):
        for subreddit in self.subreddits:
            """stop thread if running is False"""
            links = subreddit.get_subreddit_links()
            if links is not None:
                for link in links:
                    if self.running is False:
                        return
                    Downloader.download(link.url, subreddit.name, link.title + link.get_file_extension())

    def stop(self):
        self.running = False
        print("Stopping...")
