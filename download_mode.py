class DownloadMode:
    TOP = "top"
    HOT = "hot"
    LATEST = "new"

    @staticmethod
    def contains(download_mode):
        if download_mode is None:
            return False
        if download_mode != DownloadMode.LATEST and download_mode != DownloadMode.TOP \
                and download_mode != DownloadMode.HOT:
            return False
        else:
            return True
