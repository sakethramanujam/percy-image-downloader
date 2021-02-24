import os
from requests.models import Response
import shutil
from .tools import checkpath, get
from .settings import RESOLUTIONS, IMAGE_FORMATS


def create_percy(resolution: str, basepath: str, page_num: int):
    resolutions = RESOLUTIONS.keys()
    if resolution not in resolutions:
        print(f"{resolution} not supported/doesn't exist",
              "available options are:", '\n'.join(map(str, resolutions)), sep="\n")
        raise ValueError(f"Unknown resolution {resolution}")
    if page_num < 0:
        raise ValueError(
            f"Invalid Page Number")
    else:
        return Percy(resolution=resolution, basepath=basepath, page_num=page_num)


class Percy:
    def __init__(self, **config):
        self.init(**config)

    def init(self, **config):
        self.resolution_name = config.get("resolution")
        self.resolution = RESOLUTIONS.get(self.resolution_name)
        self.basepath = config.get("basepath")
        self.page_num = config.get("page_num")
        self.format = IMAGE_FORMATS.get(self.resolution_name)

    def __repr__(self):
        return(f"Percy Image Downloader")

    def _download_image(self, image_url: str):
        try:
            image_data = get(image_url, stream=True)
            return image_data
        except Exception as e:
            print(f"Exception {e}")

    def _saveimage(self,
                   image_data: Response,
                   filename: str):
        with open(filename, 'wb') as img:
            shutil.copyfileobj(image_data.raw, img)

    def _get_image_list(self, url: str):
        try:
            r = get(url)
            image_list = r.json()["images"]
            return image_list
        except Exception as e:
            print(e)

    def _get_image_urls_by_type(self, imagelist: list):
        """
        Takes large, medium, small, fullres
        """
        resolution = self.resolution
        urls = []
        ids = []
        for item in imagelist:
            urls.append(item["image_files"][resolution])
            ids.append(item["imageid"])
        return urls, ids

    def download(self):
        """
        Parses through all of the pages and downloads images
        """
        resolution = self.resolution
        basepath = self.basepath
        page_num = self.page_num
        filepath = os.path.join(basepath, resolution)
        checkpath(filepath)
        url = f"https://mars.nasa.gov/rss/api/?feed=raw_images&category=mars2020&feedtype=json&num=50&page={page_num}&order=sol+desc&&&undefined"
        if page_num > 1:     # todo: make range dynamic
            url = f"https://mars.nasa.gov/rss/api/?feed=raw_images&category=mars2020&feedtype=json&num=50&page={page_num}&order=sol+desc&&&extended="
        print(
            f"Fetching images with resolution: {self.resolution_name}, from page:{page_num}")
        imagelist = self._get_image_list(url=url)
        urls, ids = self._get_image_urls_by_type(imagelist=imagelist)
        for u, _id in zip(urls, ids):
            try:
                image_data = self._download_image(image_url=u)
                filename = os.path.join(filepath, f"{_id}.{self.format}")
                print(f"Now saving:{_id}")
                self._saveimage(image_data=image_data,
                                filename=filename)
            except Exception as e:
                print(f"Error occured downloading image {_id}")
        print("Download Complete!")
