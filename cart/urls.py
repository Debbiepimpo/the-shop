from django.conf.urls import url
from .views import cart, add_to_cart, adjust_cart

urlpatterns = [
    url(r'^$', cart, name='cart'),
    url(r'^add/(?P<id>\d+)', add_to_cart, name='add_to_cart'),
    url(r'^adjust/(?P<id>\d+)', adjust_cart, name='adjust_cart'),
]