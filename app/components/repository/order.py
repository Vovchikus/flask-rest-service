from app.components.model.order import *


def get_orders_all():
    return Order.objects.all()


def get_orders_public():
    return Order.objects().only('article', 'created', 'slug', 'items.name', 'items.cost', 'items.weight',
                                'items.article')


def get_order_by_slug(slug):
    return Order.objects.get_or_404(slug=slug)


def get_order_by_slug_public(slug):
    return Order.objects.only('article', 'created', 'slug', 'items.name', 'items.cost', 'items.weight',
                              'items.article').get_or_404(slug=slug)
