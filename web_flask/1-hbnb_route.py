#!/usr/bin/python3
"""
This script starts a Flask web application.

Modules:
    1-hbnb_route contains the definition of the Flask app and its routes

Routes:
    /hbnb: Displays 'HBNB'
"""

from flask import Flask

""" Create the Flask app (an instance of the Flask class) """
app = Flask(__name__)


@app.route('/', strict_slashes=False)  # route decorator
def hello():
    """
    Returns:
        str: 'Hello HBNB!'
    """
    return 'Hello HBNB!'


@app.route('/hbnb', strict_slashes=False)  # route decorator
def hbnb():
    """
    Returns:
        str: 'HBNB'
    """
    return 'HBNB'


if __name__ == '__main__':
    """
    Run the Flask app (only if this file is being run directly).
    """
    app.run(host='0.0.0.0', port=5000)
