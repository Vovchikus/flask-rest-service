from app.components.order.models import *


class OrderRepository:
    @staticmethod
    def get_orders_all():
        return Order.objects.all()

    @staticmethod
    def get_orders_public():
        return Order.objects().only('article', 'created', 'slug', 'items.name', 'items.cost', 'items.weight',
                                    'items.article')

    @staticmethod
    def get_order_by_slug(slug):
        return Order.objects.get_or_404(slug=slug)
