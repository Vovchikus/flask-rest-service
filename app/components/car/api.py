from flask_restful import Resource, reqparse, fields, marshal_with, request
from app.components.car.models import *

engine_format ={
    'gas_type': fields.String,
    'hp_el': fields.String,
    'volume': fields.String
}

car_format = {
    'cid': fields.Integer,
    'source': fields.String,
    'category': fields.String,
    'type_class': fields.String,
    'mark': fields.String,
    'model': fields.String,
    'mark_alias': fields.String,
    'price': fields.Integer,
    'year': fields.String,
    'generation': fields.String,
    'is_checked': fields.Boolean,
    'created_source': fields.String,
    'updated_source': fields.String,
    'gearbox': fields.String,
    'cId_source': fields.Integer,
    'owner_uid': fields.Integer,
    'owner_count': fields.Integer,
    'rid': fields.Integer,
    'run': fields.Integer,
    'services': fields.String,
    'state': fields.String,
    'type': fields.String,
    'vin': fields.String,
    'portal_rid': fields.Integer,
    'color': fields.String,
    'transmission': fields.String,
    'wheel_type': fields.String,
    'condition': fields.String,
    'customs': fields.String,
    'is_change_available': fields.Boolean,
    'comment': fields.String,
    'photos': fields.String,
    'location_link': fields.String
}


class CarList(Resource):
    @staticmethod
    @marshal_with(car_format)
    def post():
        car_parser = reqparse.RequestParser()
        car_parser.add_argument('cid')
        car_parser.add_argument('source', help='Category is required')
        car_parser.add_argument('category', required=True, help='Category is required')
        car_parser.add_argument('type_class')
        car_parser.add_argument('mark', required=True, help='Mark is required')
        car_parser.add_argument('model', required=True, help='Model is required')
        car_parser.add_argument('mark_alias')
        car_parser.add_argument('price', required=True, help='Price is required')
        car_parser.add_argument('year', required=True, help='Year is required')
        car_parser.add_argument('generation', required=True, help='Generation is required')
        car_parser.add_argument('is_checked')
        car_parser.add_argument('created_source')
        car_parser.add_argument('updated_source')
        car_parser.add_argument('gearbox', required=True, help='Gearbox is required')
        car_parser.add_argument('cId_source')
        car_parser.add_argument('owner_uid')
        car_parser.add_argument('owner_count')
        car_parser.add_argument('rid')
        car_parser.add_argument('run', required=True, help='Run is required')
        car_parser.add_argument('services')
        car_parser.add_argument('state')
        car_parser.add_argument('type')
        car_parser.add_argument('vin')
        car_parser.add_argument('portal_rid')
        car_parser.add_argument('color')
        car_parser.add_argument('transmission', required=True, help='Transmission is required')
        car_parser.add_argument('wheel_type')
        car_parser.add_argument('condition')
        car_parser.add_argument('customs')
        car_parser.add_argument('is_change_available')
        car_parser.add_argument('comment')
        car_parser.add_argument('location_link', required=True, help='Location link is required')

        car_args = car_parser.parse_args()

        car_model = Car()
        car_model.cid = car_args['cid']
        car_model.category = car_args['category']
        car_model.type_class = car_args['type_class']
        car_model.mark = car_args['mark']
        car_model.model = car_args['model']
        car_model.mark_alias = car_args['mark_alias']
        car_model.price = car_args['price']
        car_model.year = car_args['year']
        car_model.generation = car_args['generation']
        car_model.is_checked = car_args['is_checked']
        car_model.created_source = car_args['created_source']
        car_model.updated_source = car_args['updated_source']
        car_model.gearbox = car_args['gearbox']
        car_model.cId_source = car_args['cId_source']
        car_model.owner_uid = car_args['owner_uid']
        car_model.owner_count = car_args['owner_count']
        car_model.rid = car_args['rid']
        car_model.run = car_args['run']
        car_model.services = car_args['services']
        car_model.state = car_args['state']
        car_model.type = car_args['type']
        car_model.vin = car_args['vin']
        car_model.portal_rid = car_args['portal_rid']
        car_model.color = car_args['color']
        car_model.transmission = car_args['transmission']
        car_model.wheel_type = car_args['wheel_type']
        car_model.condition = car_args['condition']
        car_model.customs = car_args['customs']
        car_model.is_change_available = car_args['is_change_available']
        car_model.comment = car_args['comment']
        car_model.location_link = car_args['location_link']
        car_model.save()
        return car_model, 201
