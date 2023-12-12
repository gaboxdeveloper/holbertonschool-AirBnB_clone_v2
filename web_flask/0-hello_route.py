#!/usr/bin/python3
from flask import Flask
"""documentation"""
app = Flask(__name__)
"""documentation"""


@app.route('/', strict_slashes=False)
def hello_hbnb():
    """documentation"""
    return 'Hello HBNB!'


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
