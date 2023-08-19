# This file makes the website folder a Python package
#
# Basically, when we import the folder "website", we run whatever that is inside "__init__.py" file

from flask import Flask

def create_app():
    app = Flask(__name__)   # __name__ represents the name of the file
    app.config['SECRET_KEY'] = 'k!as@koiw9i34ad12Alasdw2 21H&'   # This is going to encrypt/secure the cookies/session data, related to the website

    return app

# TL;DR - Flask application / Initialized Secret Key / Returned from this function