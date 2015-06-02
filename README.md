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
print r.content-type

```

##License

MIT