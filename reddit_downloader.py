import praw


class RedditDownloader:
    def __init__(self, subreddits):
        self.subreddits = subreddits
        self.reddit = praw.Reddit(user_agent="Image Downloader")

    def download(self):
        for subreddit in self.subreddits:
            print(subreddit.name)
