from flask import request, render_template, Blueprint, redirect
from flask.views import MethodView
from app.components.order.models import *
from flask.ext.mongoengine.wtf import model_form

order_map = Blueprint('orders', __name__, template_folder='templates')


class ListView(MethodView):
    @staticmethod
    def get():
        orders = Order.objects.all()
        return render_template('orders/list.html', orders=orders)


class DetailView(MethodView):
    item_form = model_form(Item)

    def get(self, slug):
        form = self.item_form(request.form)
        return render_template('orders/detail.html', order=Order.objects.get_or_404(slug=slug), form=form)

    def post(self, slug):
        form = self.item_form(request.form)
        if form.validate():
            item = Item()
            form.populate_obj(item)
            order = Order.objects.get_or_404(slug=slug)
            order.items.append(item)
            order.save()
            return redirect(url_for('orders.detail', slug=slug))
        return render_template('orders/detail.html')


order_map.add_url_rule('/orders/', view_func=ListView.as_view('list'))
order_map.add_url_rule('/order/<slug>/', view_func=DetailView.as_view('detail'))
