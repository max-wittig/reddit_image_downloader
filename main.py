from reddit_downloader import *
from sub_reddit import *
import argparse


def get_subreddits(subreddit_names, limit=100):
    subreddits = []
    for name in subreddit_names:
        sub = Subreddit(name)
        sub.limit = limit
        subreddits.append(sub)
    return subreddits


def get_args():
    parser = argparse.ArgumentParser("Downloads images from reddit")
    parser.add_argument("-d", "--debug", help="Use Debug option", action='store_true')
    parser.add_argument("-s", "--subreddits", help="Add subreddits to download from", nargs="+")
    parser.add_argument("-l", "--limit", help="How many submission it should look at")

    options = parser.parse_args()
    return vars(options)


def debug_get_subreddits():
    return ["funny", "pics"]


def get_user_agent():
    return "Image Downloader"


def main():
    subreddit_names = []
    options = get_args()
    debug = options.get("debug")
    arg_subreddits = options.get("subreddits")
    limit = options.get("limit")
    if debug:
        subreddit_names = debug_get_subreddits()
    else:
        subreddit_names = arg_subreddits

    if limit is None:
        limit = 100
    if subreddit_names is None:
        exit("No arguments")
    subreddits = get_subreddits(subreddit_names, limit=limit)
    reddit_downloader = RedditDownloader(subreddits)
    reddit_downloader.download()

if __name__ == '__main__':
    main()
