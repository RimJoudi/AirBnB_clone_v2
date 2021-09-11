#!/usr/bin/python3
"""
starts a Flask web application module
"""
from flask import Flask
import sys


app = Flask(__name__)


@app.route('/', strict_slashes=False)
def hbnb():
    """
        fn to display Hello HBNB!
        in the route page
    """
    return 'Hello HBNB!'


@app.route('/hbnb', strict_slashes=False)
def hbnb_():
    """
        fn to display HBNB
        in the route page
    """
    return 'HBNB'


@app.route('/c/<text>', strict_slashes=False)
def hbnb_c(text):
    """
        fn to display a text
        in the route page
    """
    txt = text.replace('_', ' ')
    return 'C {}'.format(txt)


@app.route('/number/<int:n>', strict_slashes=False)
def hbnb_n(n):
    """
        fn to display an integer n
        in the route page
    """
    return '{} is a number'.format(n)


if __name__ == "__main__":
    app.run(host='0.0.0.0', port=5000)
