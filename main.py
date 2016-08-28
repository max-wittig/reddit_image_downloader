from reddit_downloader import *
from sub_reddit import *


def get_subreddits():
    subreddits = []
    sub = Subreddit("pics")
    subreddits.append(sub)
    sub2 = Subreddit("funny")
    subreddits.append(sub2)
    return subreddits


def get_user_agent():
    return "Image Downloader"


def main():
    reddit_downloader = RedditDownloader(get_subreddits())
    reddit_downloader.download()

if __name__ == '__main__':
    main()
