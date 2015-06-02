__author__ = 'plasmashadow'

import httplib
import urllib

class Response(object):

    def __init__(self, http_obj):

        self.http_obj = http_obj
        self._response = http_obj
        self.status_code = self._response.status
        self.reason = self._response.reason
        self.body = http_obj.read()



    @property
    def status(self):
        return self.status_code

    @property
    def length(self):
        return self.http_obj.getheaders("content-length")

    @property
    def content_type(self):
        return self.http_obj.getheaders("content-type")

    @property
    def version(self):
        return self.http_obj.version

    @property
    def headers(self):
        return self.http_obj.msg

    @property
    def socket(self):
        return self.http_obj.fileno()
