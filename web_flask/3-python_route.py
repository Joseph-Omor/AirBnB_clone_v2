#!/usr/bin/python3
"""
This script starts a Flask web application.

Modules:
    2-c_hbnb_route contains the definition of the Flask app and its routes

Routes:
    /: Displays 'Hello HBNB!'
    /hbnb: Displays 'HBNB'
    /c/<text>: Displays 'C' followed by the value of the text variable
    /python/<text>: Displays 'Python' followed by the value of the text
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


@app.route('/c/<text>', strict_slashes=False)  # route decorator
def c(text):
    """
    Return formatted string: 'C ' + the value of the text variable

    Args:
        text (str): The text to display after 'C '.
        Underscores are replaced with spaces.

    Returns:
        str: The formatted string
    """
    formatted_text = text.replace('_', ' ')
    return f'C {formatted_text}'


@app.route('/python', strict_slashes=False)  # route decorator
@app.route('/python/', strict_slashes=False)  # route decorator
@app.route('/python/<text>', strict_slashes=False)  # route decorator
def python(text='is cool'):
    """
    Return formatted string: 'Python ' + the value of the text variable

    Args:
        text (str): The text to display after 'Python '.
        Underscores are replaced with spaces.

    Returns:
        str: The formatted string
    """
    formatted_text = text.replace('_', ' ')
    return f'Python {formatted_text}'


if __name__ == '__main__':
    """
    Run the Flask app (only if this file is being run directly).
    """
    app.run(host='0.0.0.0', port=5000)
