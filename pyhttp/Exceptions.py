__author__ = 'plasmashadow'


class NetworkException(Exception):
    """
    Base class for all network exception
    """
    pass

class RedirectException(NetworkException):
    """
    Redirect exception whose status
    codes begins with 3xx series.
    """
    series = '3xx'
    code = 300

class HttpException(NetworkException):
    """
    Http exception whose status
    codes begins with 4xx series.
    """
    series = '4xx'
    code = 400

class ServerException(NetworkException):
    """
    Server Failures whoes status codes
    begins with 5xx series.
    """
    series = '5xx'
    code = 500

