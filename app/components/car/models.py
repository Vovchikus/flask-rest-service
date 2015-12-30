from app import db
from flask import url_for
import datetime


class Engine(db.Document):
    gas_type = db.StringField(verbose_name='Gas type')
    hp_el = db.StringField(verbose_name='Horse power')
    volume = db.StringField(verbose_name='Volume')


class Car(db.Document):
    cid = db.IntField(verbose_name='Id')
    source = db.StringField(verbose_name='Source')
    category = db.StringField(verbose_name='Category', required=True)
    type_class = db.StringField(verbose_name='Type class')
    mark = db.StringField(verbose_name='Mark', required=True)
    model = db.StringField(verbose_name='Model', required=True)
    mark_alias = db.StringField(verbose_name='Mark Alias')
    price = db.IntField(verbose_name='Price', required=True)
    year = db.StringField(verbose_name='Year', required=True)
    generation = db.StringField(verbose_name='Generation', required=True)
    is_checked = db.StringField(verbose_name='Is Checked')
    created_source = db.StringField(verbose_name='Created in Source')
    updated_source = db.StringField(verbose_name='Updated in Source')
    gearbox = db.StringField(verbose_name='Gearbox')
    cId_source = db.IntField(verbose_name='Cid in Source')
    owner_uid = db.IntField(verbose_name='Owner uid')
    owner_count = db.IntField(verbose_name='Owner count')
    rid = db.IntField(verbose_name='Rid')
    run = db.IntField(verbose_name='Run', required=True)
    services = db.StringField(verbose_name='Services')
    state = db.StringField(verbose_name='State')
    type = db.StringField(verbose_name='Type')
    vin = db.StringField(verbose_name='Vin number')
    portal_rid = db.IntField(verbose_name='Portal rid')
    color = db.StringField(verbose_name='Color')
    transmission = db.StringField(verbose_name='Transmission')
    wheel_type = db.StringField(verbose_name='Wheel Type')
    condition = db.StringField(verbose_name='Condition')
    customs = db.StringField(verbose_name='Customs')
    is_change_available = db.StringField(verbose_name='Is Change Available')
    comment = db.StringField(verbose_name='Comment')
    photos = db.ListField(verbose_name='Photos')
    location_link = db.StringField(verbose_name='Location Link')

    created = db.DateTimeField(default=datetime.datetime.now, required=True)

    def get_absolute_url(self):
        return url_for('car', kwargs={'cid': self.cid})

    meta = {
        'allow_inheritance': True,
        'indexes': ['cid'],
        'ordering': ['-created'],
    }
