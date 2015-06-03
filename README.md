##PyHTTP

Very Minimal HTTP wrapper for Python.

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