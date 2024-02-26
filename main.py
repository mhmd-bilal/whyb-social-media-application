import os
from flask import Flask
from flask_restful import Resource, Api
from applications import config
from applications.config import LocalDevelopmentConfig
from applications.database import db
#from flask_cors import CORS


app = None
api = None


def create_app():
    app = Flask(__name__, template_folder="templates")
    if os.getenv('ENV', "development") == "production":
        raise Exception("Currently no production config is setup")
    else:
        print("Starting Local Development")
        app.config.from_object(LocalDevelopmentConfig)
    db.init_app(app)
    api = Api(app)
    app.app_context().push()
    return app, api


app, api = create_app()

from applications.controllers import *

from applications.api import *
# api.add_resource(UserAPI,"/api/categories/<int:category_id>","/api/categories/<string:category_name>","/api/categories/")
api.add_resource(UserAPI_posts,"/api/posts/<string:capt>")
api.add_resource(UserAPI_users,"/api/users/<string:user_n>")
# api.add_resource(UserAPI1,"/api/products/<int:product_id>","/api/products/<string:product_name>","/api/products/")
# api.add_resource(UserAPI_pro,"/api/products")

if __name__ == '__main__':
    app.run(host='127.0.0.1', debug=True, port=8080)
