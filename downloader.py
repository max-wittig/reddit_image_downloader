import requests
import os


class Downloader:
    def __init__(self, min_file_size):
        self.min_file_size = min_file_size

    root_folder_name = "files"

    @staticmethod
    def create_folder(folder_name):
        if not os.path.exists(folder_name):
            os.makedirs(folder_name)

    def clean(self, file):
        if os.path.exists(file) and os.path.getsize(file) < self.min_file_size:
            os.remove(file)

    def download(self, url, folder_name, filename):
        try:
            file = requests.get(url=url)
            print("Downloading: " + filename)
            path = os.path.join(Downloader.root_folder_name, folder_name)
            Downloader.create_folder(path)
            with open(os.path.join(path, filename), 'wb') as f:
                for chunk in file.iter_content(chunk_size=1024):
                    if chunk:
                        f.write(chunk)
                        f.flush()
            self.clean(os.path.join(path, filename))
        except:
            print("Could not download" + folder_name + "/" + filename)


