from flask import Blueprint
from app.components.order.api import OrderList, OrderDetail
from app.components.car.api import CarList
from app import api

api_map = Blueprint('api', __name__)

api.add_resource(OrderList, '/api/orders/')
api.add_resource(OrderDetail, '/api/order/<slug>')

api.add_resource(CarList, '/api/cars/')