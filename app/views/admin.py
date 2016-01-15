from flask import request, render_template, Blueprint, redirect
from flask.ext.mongoengine.wtf import model_form
from flask.views import MethodView

from app.components.auth.auth import requires_auth
from app.components.model.order import *

admin_map = Blueprint('admin', __name__, template_folder='templates')


class List(MethodView):
    decorators = [requires_auth]
    cls = Order

    def get(self):
        orders = self.cls.objects.all()
        return render_template('admin/list.html', orders=orders)


class Detail(MethodView):
    decorators = [requires_auth]

    @staticmethod
    def get_context(self, slug=None):
        form_cls = model_form(Order, exclude=('created', 'items'))

        if slug:
            order = Order.objects.get_or_404(slug=slug)
            if request.method == 'POST':
                form = form_cls(request.form, inital=order._data)
            else:
                form = form_cls(obj=order)
        else:
            order = Order()
            form = form_cls(request.form)

        context = {
            "order": order,
            "form": form,
            "create": slug is None
        }
        return context

    def get(self, slug):
        context = self.get_context(slug)
        return render_template('admin/detail.html', **context)

    def post(self, slug):
        context = self.get_context(slug)
        form = context.get('form')

        if form.validate():
            order = context.get('order')
            form.populate_obj(order)
            order.save()

            return redirect(url_for('admin.index'))
        return render_template('admin/detail.html', **context)


# Register the urls
admin_map.add_url_rule('/admin/', view_func=List.as_view('index'))
admin_map.add_url_rule('/admin/create/', defaults={'slug': None}, view_func=Detail.as_view('create'))
admin_map.add_url_rule('/admin/<slug>/', view_func=Detail.as_view('edit'))
