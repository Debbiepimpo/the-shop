from django.conf.urls import re_path
from .views import articles_to_sell, article_detail


urlpatterns = [
        re_path(r'^$', articles_to_sell, name='articles_to_sell'),
        re_path(r'^(?P<pk>\d+)/$', article_detail, name='article_detail'),

]
