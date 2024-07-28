#!/usr/bin/python3
"""
This script starts a Flask web application.

Modules:
    0-hello_route contains the definition of the Flask app and its routes

Functions:
    hello_hbnb: Returns a greeting message.

"""

from flask import Flask

""" Create the Flask app (an instance of the Flask class) """
app = Flask(__name__)


@app.route('/', strict_slashes=False)  # route decorator
def hello_hbnb():
    """
    Returns:
        str: 'Hello HBNB!'
    """
    return 'Hello HBNB!'


if __name__ == '__main__':
    """
    Run the Flask app (only if this file is being run directly).
    """
    app.run(host='0.0.0.0', port=5000)
