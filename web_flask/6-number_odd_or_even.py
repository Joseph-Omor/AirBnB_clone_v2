#!/usr/bin/python3
"""
This script starts a Flask web application.

Modules:
    5-number template contains the definition of the Flask app and its routes
    H1 tag

Routes:
    /: Displays 'Hello HBNB!'
    /hbnb: Displays 'HBNB'
    /c/<text>: Displays 'C' followed by the value of the text variable
    /python/<text>: Displays 'Python' followed by the value of the text
    /number/<n>: Displays 'n is a number' only if n is an integer
    /number_template/<n>: Displays an HTML page only if n is an integer
"""

from flask import Flask, render_template

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


@app.route('/python/', defaults={'text': 'is cool'}, strict_slashes=False)
@app.route('/python/<text>', strict_slashes=False)  # route decorator
def python(text):
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
        n: The number to check.

    Returns:
        str: The formatted string
    """
    if isinstance(n, int):
        return f'{n} is a number'


@app.route('/number_template/<int:n>', strict_slashes=False)  # route decorator
def number_template(n):
    """
    Return an HTML page only if n is an integer
    with H1 tag: 'Number: n' inside the HTML body tag

    Args:
        n (int): The number to display in the HTML page.

    Returns:
        str: The rendered HTML template only if n is an integer
    """
    if isinstance(n, int):
        return render_template('5-number.html', n=n)


@app.route('/number_odd_or_even/<int:n>', strict_slashes=False)
def number_odd_or_even(n):
    """
    Returns an HTML page only if n is an integer
    with H1 tag: 'Number is even or odd' inside the HTML body tag

    Args:
        n (int): The number to display in the HTML page.

    Returns:
        str: The rendered HTML template only if n is an integer
    """
    if isinstance(n, int):
        if n % 2 == 0:
            return render_template('6-number_odd_or_even.html',
                                   n=n, even_or_odd="even")
        else:
            return render_template('6-number_odd_or_even.html',
                                   n=n, even_or_odd="odd")


if __name__ == '__main__':
    """
    Run the Flask app (only if this file is being run directly).
    """
    app.run(host='0.0.0.0', port=5000)
