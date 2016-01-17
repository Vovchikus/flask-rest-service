from flask_restful import Resource, reqparse, fields, marshal_with, marshal
from app.components.model.order import *

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


def order_request_parse():
    order_parser = reqparse.RequestParser()
    order_parser.add_argument('article', required=True, help='Article is required')
    order_parser.add_argument('slug', required=True, help='Slug is required')
    order_parser.add_argument('items', required=True, action='append', type=nested_item_validator)
    return order_parser.parse_args()


def order_builder(order_model, new_data):
    order_model.article = new_data['article']
    order_model.slug = new_data['slug']

    for item in new_data['items']:
        item_model = Item()
        item_model.name = item['name']
        item_model.article = item['article']
        item_model.weight = item['weight']
        item_model.cost = item['cost']
        order_model.items.append(item_model)
    return order_model


class OrderList(Resource):
    @staticmethod
    @marshal_with(orders_list_format)
    def get():
        orders = Order.objects.all()
        return {'orders': orders}, 200

    @staticmethod
    @marshal_with(order_format)
    def post():
        response = order_request_parse()
        order_model = Order()
        build_order = order_builder(order_model, response)
        build_order.save()
        return order_model, 201


class OrderDetail(Resource):
    @staticmethod
    @marshal_with(order_format)
    def get(slug):
        order = Order.objects.get_or_404(slug=slug)
        return order, 200

    @staticmethod
    def put(slug):
        response = order_request_parse()
        order_model = Order.objects.get_or_404(slug=slug)
        build_order = order_builder(order_model, response)
        return build_order, 201
