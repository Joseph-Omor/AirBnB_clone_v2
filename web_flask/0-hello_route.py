#!/usr/bin/python3
# This script starts a Flask web application

from flask import Flask

# Create the Flask app (an instance of the Flask class)
app = Flask(__name__)


# Define the route for the Default(root) URL ("/")
@app.route('/', strict_slashes=False)
def hello_hbnb():
    """ Displays 'Hello HBNB!' """
    return 'Hello HBNB!'


# Setup to run only if this file is being run directly
if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
