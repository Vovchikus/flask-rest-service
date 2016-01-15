import datetime
from app import db
from flask import url_for


class Item(db.EmbeddedDocument):
    name = db.StringField(verbose_name='Name', max_length=255, required=True, help_text='Default')
    cost = db.IntField(verbose_name='Cost', required=True, help_text='Default')
    weight = db.IntField(verbose_name='Weight', required=True, help_text='Default')
    article = db.StringField(verbose_name='Article', max_length=255, required=True, help_text='Default')


class Order(db.Document):
    article = db.StringField(verbose_name='Article', max_length=255, required=True, help_text='Default')
    created = db.DateTimeField(default=datetime.datetime.now, required=True, help_text='Default')
    items = db.ListField(db.EmbeddedDocumentField('Item'))
    slug = db.StringField(verbose_name='Slug', max_length=255, required=True, help_text='Default')

    def get_absolute_url(self):
        return url_for('order', kwargs={'article': self.article})

    meta = {
        'allow_inheritance': True,
        'indexes': ['-created', 'article'],
        'ordering': ['-created'],
    }
