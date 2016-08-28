from download_mode import *


class Subreddit:
    def __init__(self, name):
        self.name = name
        self.download_mode = DownloadMode.TOP

    def get_top_submission(self):
        pass