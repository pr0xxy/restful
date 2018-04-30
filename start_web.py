#!/usr/bin/python
# -*- coding: utf-8 -*-
"""
This project provides a RESTful web service.
  a. The web service accepts a number, n, as input and returns the first n Fibonacci numbers, starting from 0. I.e. given n  = 5, appropriate output would represent the sequence [0, 1, 1, 2, 3].
  b. Given a negative number, it will respond with an appropriate error.
2. Include whatever instructions are necessary to build and deploy/run the project, where "deploy/run" means the web service is accepting requests and responding to them as appropriate.
3. Include some unit and/or functional tests
4. This program is written in python
"""
from flask import Flask, request

app = Flask(__name__)

@app.route('/')
def restful_api():
    """
    This is for functional testing.
    :return: string
    """
    return 'This is the root for RESTful web service'


def cruncher(n):
    """
    Needs to raise an exception when the number is less than 0 or not a whole number. Otherwise return a list
    containing a Fibonacci sequence
    :param n: An integer where to the Fibonacci sequence should finish
    :return: A list of numbers in a Fibonacci sequence
    """
    t = [0]
    a, b = 0, 1
    x = n-1
    for i in range(x):
        a, b = b, a + b
        t.append(a)
    return t



@app.route("/fibonacci/<string:seq>/")
def sequence(seq):
    """
    Call the fibonacci function above and convert the return value to a string
    Function borrowed from http://en.literateprograms.org/Fibonacci_numbers_(Python)
    :param seq:
    :return:
    """
    y = int(seq)
    if (y < 0):
        return "Error! Number provided is not a positive number"
    tmp = cruncher(y)
    return str(tmp)


if __name__ == '__main__':
    app.run()
