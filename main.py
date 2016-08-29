from reddit_downloader import *
from sub_reddit import *


def get_subreddits():
    subreddits = []
    sub = Subreddit("earthporn")
    sub.limit = 1000
    subreddits.append(sub)
    sub2 = Subreddit("funny")
    sub2.limit = 1000
    subreddits.append(sub2)
    return subreddits


def get_user_agent():
    return "Image Downloader"


def main():
    reddit_downloader = RedditDownloader(get_subreddits())
    reddit_downloader.download()

if __name__ == '__main__':
    main()
