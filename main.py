from reddit_downloader import *
from sub_reddit import *
import argparse
import threading


def get_subreddits(subreddit_names, limit=100, download_mode=DownloadMode.TOP):
    subreddits = []
    for name in subreddit_names:
        sub = Subreddit(name)
        sub.download_mode = download_mode
        sub.limit = limit
        subreddits.append(sub)
    return subreddits


def get_args():
    parser = argparse.ArgumentParser("Downloads images from reddit")
    parser.add_argument("-d", "--debug", help="Use Debug option", action='store_true')
    parser.add_argument("-s", "--subreddits", help="Add subreddits to download from", nargs="+")
    parser.add_argument("-l", "--limit", help="How many submission it should look at", type=int)
    parser.add_argument("-m", "--multi", help="Subreddits in multireddit form")
    parser.add_argument("-dm", "--download_mode", help="top | hot | new")
    options = parser.parse_args()
    return vars(options)


def debug_get_subreddits():
    return ["funny", "pics"]


def get_user_agent():
    return "Image Downloader"


def main():
    subreddit_names = list()
    options = get_args()
    debug = options.get("debug")
    arg_subreddits = options.get("subreddits")
    limit = options.get("limit")
    multireddits = options.get("multi")
    download_mode = options.get("download_mode")
    if debug:
        subreddit_names = debug_get_subreddits()
    else:
        subreddit_names = arg_subreddits

    if multireddits is not None:
        if subreddit_names is None:
            subreddit_names = []
        subreddit_names += multireddits.split("+")

    if limit is None:
        limit = 100

    if subreddit_names is None:
        exit("No subreddits to download from. \nSpecify some with the -s option")

    if not DownloadMode.contains(download_mode):
        download_mode = DownloadMode.TOP

    subreddits = get_subreddits(subreddit_names, limit=limit, download_mode=download_mode)
    print("Download started...")
    reddit_downloader = RedditDownloader(subreddits)
    thread = threading.Thread(target=reddit_downloader.download)
    """thread dies, if main dies"""
    thread.setDaemon(True)
    thread.start()
    thread.join()

if __name__ == '__main__':
    main()
