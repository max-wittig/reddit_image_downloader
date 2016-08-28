import requests
import os


class Downloader:
    root_folder_name = "files"

    @staticmethod
    def create_folder(folder_name):
        if not os.path.exists(folder_name):
            os.makedirs(folder_name)

    @staticmethod
    def download(url, folder_name, filename):
        file = requests.get(url=url)
        path = os.path.join(Downloader.root_folder_name, folder_name)
        Downloader.create_folder(path)
        with open(os.path.join(path, filename), 'wb') as f:
            for chunk in file.iter_content(chunk_size=1024):
                if chunk:
                    f.write(chunk)
                    f.flush()

