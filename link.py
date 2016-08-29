import os


class Link:
    def __init__(self, url, title):
        self.url = url
        self.title = title

    def get_file_extension(self):
        suffix = os.path.splitext(self.url)[1]
        return suffix

    def get_file_name(self):
        return self.url.split('/')[-1]
