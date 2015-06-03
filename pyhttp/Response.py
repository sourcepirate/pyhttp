__author__ = 'plasmashadow'


import urllib3
import json

class Response(object):

    def __init__(self, http_obj):

        self.data = http_obj
        self._status = self.data.status
        self._headers = self.data.getheaders()

    @property
    def header(self):
        return self._headers

    @property
    def status(self):
        return self._status

    @property
    def content(self):
        return self.data.data

    @property
    def json(self):
        try:
            return json.loads(self.data.data)
        except Exception as e:
            raise ValueError("Error opening the json response")