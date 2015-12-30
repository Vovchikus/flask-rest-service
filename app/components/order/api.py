from flask_restful import Resource, reqparse, fields, marshal_with, marshal
from app.components.order.models import *
from app.components.order.repository import OrderRepository
import json

item_format = {
    'name': fields.String,
    'cost': fields.Integer,
    'weight': fields.Integer,
    'article': fields.String
}

order_format = {
    'article': fields.String,
    'slug': fields.String,
    'created': fields.DateTime,
    'items': fields.List(fields.Nested(item_format))
}

orders_list_format = {
    'orders': fields.List(fields.Nested(order_format))
}


def nested_item_validator(item):
    try:
        dm = marshal(item, item_format)
        for k, v in dm.iteritems():
            if v is None:
                raise TypeError("Empty parameter in Item: {}".format(k))
    except TypeError:
        raise
    except ValueError:
        raise ValueError('Unknown value error, call support')
    return item


class OrderList(Resource):
    @staticmethod
    @marshal_with(orders_list_format)
    def get():
        public_orders = OrderRepository.get_orders_public()
        return {'orders': public_orders}, 200

    @staticmethod
    @marshal_with(order_format)
    def post():
        order_parser = reqparse.RequestParser()
        order_parser.add_argument('article', required=True, help='Article is required')
        order_parser.add_argument('slug', required=True, help='Slug is required')
        order_parser.add_argument('items', required=True, action='append', type=nested_item_validator)
        order_args = order_parser.parse_args()

        order_model = Order()
        order_model.article = order_args['article']
        order_model.slug = order_args['slug']

        for item in order_args['items']:
            item_model = Item()
            item_model.name = item['name']
            item_model.article = item['article']
            item_model.weight = item['weight']
            item_model.cost = item['cost']
            order_model.items.append(item_model)
        order_model.save()
        return order_model, 201


class OrderDetail(Resource):
    @staticmethod
    def get(slug):
        order = OrderRepository.get_order_by_slug(slug)
        return json.loads(order.to_json())
