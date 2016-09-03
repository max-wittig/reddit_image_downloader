import requests
import os


class Downloader:
    def __init__(self, min_file_size, override=False):
        self.min_file_size = min_file_size
        self.override = override

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
            file_location = os.path.join(path, filename)
            Downloader.create_folder(path)
            if self.override or not os.path.exists(file_location):
                with open(file_location, 'wb') as f:
                    for chunk in file.iter_content(chunk_size=1024):
                        if chunk:
                            f.write(chunk)
                            f.flush()
            else:
                print("exists. Skipping...")
            self.clean(file_location)
        except:
            print("Could not download: " + folder_name + "/" + filename)


