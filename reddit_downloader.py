from downloader import *
import praw
import main


class RedditDownloader:
    def __init__(self, subreddits, min_filesize=50, override=False, allowed_extensions=None):
        self.subreddits = subreddits
        self.reddit = praw.Reddit(user_agent=main.get_user_agent())
        self.running = True
        self.downloader = Downloader(min_filesize, override=override)
        self.allowed_extensions = allowed_extensions

    def download(self):
        for subreddit in self.subreddits:
            """overrides default allowed file extensions"""
            if self.allowed_extensions is not None:
                subreddit.allowed_extensions = self.allowed_extensions
            """stop thread if running is False"""
            links = subreddit.get_subreddit_links()
            if links is not None:
                for link in links:
                    if self.running is False:
                        return
                    try:
                        self.downloader.download(link.url, subreddit.name, link.title + link.get_file_extension())
                    except:
                        print("Download_error")

    def stop(self):
        self.running = False
        print("Stopping...")
