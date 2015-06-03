##PyHTTP

Very Minimal HTTP wrapper for Python.

[![Build Status](https://travis-ci.org/plasmashadow/pyhttp.svg?branch=master)](https://travis-ci.org/plasmashadow/pyhttp)
[![PyPI version](https://badge.fury.io/py/pyrequest.svg)](http://badge.fury.io/py/pyrequest)
[![PyPI](https://img.shields.io/pypi/dm/pyrequest.svg)](https://pypi.python.org/pypi/pyrequest)
[![Code Health](https://landscape.io/github/plasmashadow/pyhttp/master/landscape.svg?style=flat)](https://landscape.io/github/plasmashadow/pyhttp/master)


##installation
```
pip install pyrequest
```

##Usage

```python
  
from pyhttp import Request

r = Request("google.com").get()
print r.status

//POST request

r = Request('http://jsonplaceholder.typicode.com/posts')
response = r.post({'title': 'hello'})
print response.content
print response.status
print response.json

//setting headers

r = Request('http://jsonplaceholder.typicode.com/posts')
r.headers = {'content-type': 'application/json')
response = r.post({'title': 'hello'})
print response.content
print response.status
print response.json

//PUT request

r = Request('http://jsonplaceholder.typicode.com/posts/1')
response = r.put({'title': 'hello'})
print response.content
print response.status
print response.json

//DELETE request

r = Request('http://jsonplaceholder.typicode.com/posts/1')
r.delete()


```

##License

MIT