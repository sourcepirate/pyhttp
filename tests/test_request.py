__author__ = 'plasmashadow'


import unittest
from pyhttp import Request


class TestRequest(unittest.TestCase):

    def setUp(self):
        self.request1 = Request("http://jsonplaceholder.typicode.com/posts/1")
        self.request2 = Request("http://jsonplaceholder.typicode.com/posts")

    def test_get(self):
        response = self.request1.get()
        self.assertEqual(response.status, 200)

    def test_post(self):
        self.request2.headers = {'content-type': 'application/json'}
        response = self.request2.post({'title': 'foo', 'body': 'bar', 'userId': 34})
        self.assertEqual(response.status, 200)

    def test_put(self):
        self.request1.headers = {'content-type': 'application/json'}
        response = self.request1.put({'id': 1, 'title': 'foo', 'body': 'bar_baz', 'userId': 340})
        self.assertEqual(response.status, 200)

    def test_delete(self):
        response = self.request1.delete()
        self.assertEqual(response.status, 200)


