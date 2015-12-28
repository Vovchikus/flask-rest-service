from flask import Flask
from flask.ext.mongoengine import MongoEngine
from flask_restful import Api
from app import views

app = Flask(__name__)
api = Api(app)
app.config.from_object('config')

db = MongoEngine(app)


def register_blueprints(app):
    from app.views.order import order_map
    from app.views.admin import admin_map
    from app.components.api import api_map
    app.register_blueprint(order_map)
    app.register_blueprint(admin_map)
    app.register_blueprint(api_map)

register_blueprints(app)
