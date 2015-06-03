__author__ = 'plasmashadow'


import urllib3

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
