# This file contains all the pages of the website that the user can use. For example: homepage.
# Note: Login page is not included, here. It is related to the authentication file.

# Blueprints allow us to organise our views, so that they are not all on the same file.

from flask import Blueprint

views = Blueprint('views', __name__)    # This is a blueprint for our flask application

@views.route('/')
def home():
    return "<h1>Test<h1>"