from download_mode import *
import praw
import main


class Subreddit:
    def __init__(self, name):
        self.name = name
        self.download_mode = DownloadMode.TOP
        self.limit = 10
        self.reddit = praw.Reddit(user_agent=main.get_user_agent())
        self.subreddit = self.reddit.get_subreddit(self.name)

    def get_submission_links(self, submissions):
        links = []
        for sub in submissions:
            if sub.url is not None:
                links.append(sub.url)
        return links

    def get_subreddit_links(self):
        links = []
        if self.download_mode is DownloadMode.TOP:
            submissions = self.subreddit.get_top(limit=self.limit)
            links.extend(self.get_submission_links(submissions))
        elif self.download_mode == DownloadMode.HOT:
            submissions = self.subreddit.get_hot(limit=self.limit)
            links.extend(self.get_submission_links(submissions))
        return links
