from flask import Blueprint
from order import OrderList, OrderDetail
from app import api

api_map = Blueprint('api', __name__)

api.add_resource(OrderList, '/api/orders/')
api.add_resource(OrderDetail, '/api/order/<slug>')