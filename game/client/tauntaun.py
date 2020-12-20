import requests
from .webclient import WebClient
from game.persistency import remote_save_url
from pathlib import Path

class Tauntaun(WebClient):
    def __init__(self):
        self.base_url = remote_save_url()

    def post_miz(self, filepath: Path):
        files = {'upload_file': open(filepath, "rb")}
        headers = {'Content-type': 'application/zip'}
        requests.post(self.base_url + "/upload", files=files,)