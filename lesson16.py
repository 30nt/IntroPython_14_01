import requests
from requests_oauthlib import OAuth1
import os
import random


class IconSaver:
    def __init__(self, path_dir):
        self._path_dir = path_dir
        self._auth = OAuth1(os.environ["KEY"], os.environ["SECRET"])

    @property
    def path_dir(self):
        return self._path_dir

    def get_icon(self, key_word=""):
        if not key_word:
            key_word = str(random.randint(1,100))
        endpoint = f"http://api.thenounproject.com/icon/{key_word}"
        response = requests.get(endpoint, auth=self._auth)
        data = response.json()
        self._save_icon(data, key_word)

    def _save_icon(self, data, key_word):
        if "icon_url" in data["icon"]:
            icon_url = data["icon"]["icon_url"]
            ext = "svg"
        else:
            icon_url = data["icon"]["preview_url"]
            ext = "png"
        img = requests.get(icon_url)
        with open(os.path.join(self._path_dir, f"{key_word}.{ext}"), "wb") as file:
            file.write(img.content)


icon_saver = IconSaver("qqq")
icon_saver.get_icon("iphone")
