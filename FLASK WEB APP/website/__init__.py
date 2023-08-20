# This file makes the website folder a Python package
#
# Basically, when we import the folder "website", we run whatever that is inside "__init__.py" file

from flask import Flask

def create_app():
    app = Flask(__name__)   # __name__ represents the name of the file
    app.config['SECRET_KEY'] = 'k!as@koiw9i34ad12Alasdw2 21H&'   # This is going to encrypt/secure the cookies/session data, related to the website
    
    from .views import views
    from .auth import auth

    app.register_blueprint(views, url_prefix='/')
    app.register_blueprint(auth, url_prefix='/')

    return app

# TL;DR - Flask application / Initialized Secret Key / Returned from this function