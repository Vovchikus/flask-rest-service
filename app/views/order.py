from flask import request, render_template, Blueprint, redirect
from flask.ext.mongoengine.wtf import model_form
from flask.views import MethodView

from app.components.model.order import *

order_map = Blueprint('orders', __name__, template_folder='templates')


class ListView(MethodView):
    @staticmethod
    def get():
        orders = Order.objects.all()
        return render_template('orders/list.html', orders=orders)


class DetailView(MethodView):
    form = model_form(Item, exclude=['created'])

    def get_context(self, article):
        order = Order.objects.get_order_by_slug(slug=article)
        form = self.form(request.form)

        context = {
            "order": order,
            "form": form
        }
        return context

    def get(self, article):
        form = self.form(request.form)
        return render_template('orders/detail.html', order=Order.objects.get_or_404(slug=article), form=form)

    def post(self, article):
        context = self.get_context(article)
        form = context.get('form')
        if form.validate():
            item = Item()
            form.populate_obj(item)
            order = context.get('order')
            order.items.append(item)
            order.save()
            return redirect(url_for('orders.detail', slug=article))
        return render_template('orders/detail.html', **context)


order_map.add_url_rule('/orders/', view_func=ListView.as_view('list'))
order_map.add_url_rule('/order/<slug>/', view_func=DetailView.as_view('detail'))
