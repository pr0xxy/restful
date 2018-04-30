#!/usr/bin/python
# -*- coding: utf-8 -*-
from flask import Flask
import unittest
import platform
import requests


class TestFib(unittest.TestCase):

    def test_service(self):
        """
        This is to verify functionality.
        :return: "This is the root for RESTful web service"
........"""

        response = requests.get('http://127.0.0.1:5000/'.format(platform.node()))
        self.assertEqual(200, response.status_code,
                         response.status_code)

    def test_negative(self):
        """
        This will respond with an appropriate error.
        :return: "Error! Number provided is not a positive number"
........"""

        response = \
            requests.get('http://127.0.0.1:5000/fibonacci/-1'.format(platform.node()))
        self.assertEqual(200, response.status_code,
                         response.status_code)

    def test_example(self):
        """
        This will check that the example matches (n=5 [0,1,1,2,3])
........"""

        response = \
            requests.get('http://127.0.0.1:5000/fibonacci/5'.format(platform.node()))
        self.assertEqual(str([0, 1, 1, 2, 3]), response.content,
                         response.content)


if __name__ == '__main__':
    unittest.main()
