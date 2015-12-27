from app import app
from flask import request, render_template, Blueprint, redirect
from flask.views import MethodView
from app.components.order.models import *
from flask.ext.mongoengine.wtf import model_form

order_blueprint = Blueprint('orders', __name__, template_folder='templates')


class ListView(MethodView):

    @staticmethod
    def get(self):
        orders = Order.objects.all()
        return render_template('orders/list.html', orders=orders)


class DetailView(MethodView):
    form = model_form(Item)

    def get_context(self, slug):
        order = Order.objects.get_or_404(slug=slug)
        form = self.form(request.form)

        context = {
            "order": order,
            "form": form
        }
        return context

    def get(self, slug):
        context = self.get_context(slug)
        return render_template('orders/detail.html', **context)

    def post(self, slug):
        context = self.get_context(slug)
        form = context.get('form')

        if form.validate():
            item = Item()
            form.populate_obj(item)

            order = context.get('order')
            order.items.append(item)
            order.save()
            return redirect(url_for('orders.detail', slug=slug))

        return render_template('orders/detail.html', **context)


order_blueprint.add_url_rule('/orders', view_func=ListView.as_view('list'))
order_blueprint.add_url_rule('/order/<slug>/', view_func=DetailView.as_view('detail'))


# @app.route('/order/add', methods=['GET', 'POST'])
# def order_add():
#     order = Order(article='ORDER-0002', slug='ORDER-0002')
#     item = Item(name='IPHONE-6S', cost=600, weight=3, article='ITEM-0002')
#     order.items.append(item)
#     order.save()
