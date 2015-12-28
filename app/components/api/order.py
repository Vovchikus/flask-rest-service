from flask_restful import Resource, reqparse, fields, marshal_with
from flask import Response, request
from app.components.order.models import *
import json
from flask.ext.mongoengine.wtf import model_form


def get_orders_all():
    return Order.objects.all()


def get_orders_public():
    return Order.objects().only('article', 'created', 'slug', 'items.name', 'items.cost', 'items.weight',
                                'items.article')


def get_order_by_slug(slug):
    return Order.objects.get_or_404(slug=slug)


resource_fields = {
    'article': fields.String,
    'slug': fields.String
}


class OrderList(Resource):
    order_form = model_form(Order)

    @staticmethod
    def get():
        resp = json.loads(get_orders_public().to_json())
        return Response(response=json.dumps(resp), status=200, mimetype="application/json")

    def post(self):
        parser = reqparse.RequestParser()
        parser.add_argument('article')
        parser.add_argument('slug')
        args = parser.parse_args()
        order = {'article': args['article'], 'slug': args['slug']}
        order_model = Order()
        order_model.article = order['article']
        order_model.slug = order['slug']
        order_model.save()
        return Response(response=json.dumps(order), status=201, mimetype="application/json")


class OrderDetail(Resource):
    @staticmethod
    def get(slug):
        order = get_order_by_slug(slug)
        return json.loads(order.to_json())
