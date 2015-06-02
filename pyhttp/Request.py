__author__ = 'plasmashadow'

import httplib
from Response import Response
import urllib

class Request(object):

    def __init__(self, *args, **kwargs):
        """
        Constructor is the request object
        :param args:
        :param kwargs:
        :return:
        """
        self.url = args[0]
        self.ssl = kwargs.pop("ssl", False)
        self.port = kwargs.pop("port", 80)
        self._headers = {}
        if self.ssl:
            self._connection = httplib.HTTPSConnection(self.url, **kwargs)
        else:
            self._connection = httplib.HTTPConnection(self.url, **kwargs)


    @property
    def header(self):
        return self._headers

    @header.setter
    def header(self, value):
        self._headers.update(**value)

    @property
    def connection(self):
        return self._connection

    def _do_method(self, method, params=None):
        data = urllib.urlencode(params) if params else None
        self._connection.request(method=method, url="/", body=None, headers=self.header)
        response = self.connection.getresponse()
        return Response(response)

    def get(self, params=None):
        return self._do_method("GET", params)

    def post(self, params=None):
        return self._do_method("POST", params)

    def put(self, params=None):
        return self._do_method("PUT", params)

    def delete(self):
        return self._do_method("DELETE")