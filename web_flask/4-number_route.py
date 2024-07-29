#!/usr/bin/python3
"""
This script starts a Flask web application.

Modules:
    4-number_route contains the definition of the Flask app and its routes

Routes:
    /: Displays 'Hello HBNB!'
    /hbnb: Displays 'HBNB'
    /c/<text>: Displays 'C' followed by the value of the text variable
    /python/<text>: Displays 'Python' followed by the value of the text
    /number/<n>: Displays 'n is a number' only if n is an integer
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


@app.route('/number/<int:n>', strict_slashes=False)  # route decorator
def number(n):
    """
    Return formatted string: 'n is a number' only if n is an integer

    Args:
        n (int): The number to check.

    Returns:
        str: The formatted string
    """
    if isinstance(n, int):
        return f'{n} is a number'


if __name__ == '__main__':
    """
    Run the Flask app (only if this file is being run directly).
    """
    app.run(host='0.0.0.0', port=5000)
