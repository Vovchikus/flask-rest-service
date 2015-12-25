from flask import Flask
from flask.ext.mongoengine import MongoEngine

app = Flask(__name__)
app.config.from_object('config')

db = MongoEngine(app)
from app import views


def register_blueprints(app):
    from app.views import order_blueprint
    app.register_blueprint(order_blueprint)


register_blueprints(app)
