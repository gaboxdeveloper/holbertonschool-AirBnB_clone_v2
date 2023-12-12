#!/usr/bin/python3
"""documentation importing Flask"""
from flask import Flask
"""documentation calling flask"""
app = Flask(__name__)


@app.route('/', strict_slashes=False)
def hello_hbnb():
    """function to return Hello HBNB"""
    return 'Hello HBNB!'


@app.route('/hbnb', strict_slashes=False)
def hbnb():
    """function to return HBNB"""
    return 'HBNB'


@app.route('/c/<text>', strict_slashes=False)
def c_isfun(text):
    """function to return C"""
    formatted_text = text.replace('_', ' ')
    return f'C {formatted_text}'


@app.route('/python/<text>', strict_slashes=False)
def python(text="is cool"):
    """function to return python"""
    formatted_text = text.replace('_', ' ')
    return f'Python {formatted_text}'


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
