__author__ = 'plasmashadow'


import unittest
from pyhttp import Request


class TestRequest(unittest.TestCase):

    def setUp(self):
        self.request = Request("www.google.com")

    def test_get(self):
        response = self.request.get()
        self.assertEqual(response.status, 302)