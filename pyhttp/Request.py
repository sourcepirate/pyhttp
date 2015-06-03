__author__ = 'plasmashadow'

from Response import Response
import urllib3
import json
import certifi



class HttpTimeout(urllib3.Timeout):

    connect_time_out = 10
    """
       A simple time out for http request
    """
    def __init__(self, read_time_out):
        """
        Constructor for HttpTimeout
        default connection timeout as 10 seconds
        :param read_time_out: time_out for reading
        :return:
        """
        super(HttpTimeout, self).__init__(connect=HttpTimeout.connect_time_out, read=read_time_out)




class Request(object):
    """
    Http Request object for Representing http reques
    """
    _default_time_out = HttpTimeout(10)

    def __init__(self, url, **kwargs):

        self._url = url
        ssl = kwargs.pop('ssl', False)
        if not ssl:
            self.http = urllib3.PoolManager(timeout=Request._default_time_out)
        else:
            self.http = urllib3.PoolManager(cert_reqs='CERT_REQUIRED',
                                            ca_certs=certifi.where(),
                                            timeout=Request._default_time_out)
        self._header = {}

    @property
    def headers(self):
        return self._header if self._header else None

    @headers.setter
    def headers(self, value):
        try:
            self._header.update(urllib3.make_headers(**value))
        except Exception as e:
            self._header.update(value)


    @staticmethod
    def get_params(params):
        if not params:
            return None
        return json.dumps(params)

    def get(self, params={}):
        body = Request.get_params(params)
        response = self.http.urlopen('GET', self._url, body=body, headers=self.headers)
        return Response(response)

    def post(self, params={}):
        body = Request.get_params(params)
        response = self.http.urlopen('POST', self._url, body=body, headers=self.headers)
        return Response(response)

    def put(self, params={}):
        body = Request.get_params(params)
        response = self.http.urlopen('PUT', self._url, body=body, headers=self.headers)
        return Response(response)

    def delete(self):
        response = self.http.urlopen('DELETE', self._url)
        return Response(response)




