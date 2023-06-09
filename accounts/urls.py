from django.conf.urls import url, include
from accounts.views import logout, login, registration, orders, contact
from accounts import url_reset

urlpatterns = [
    url(r'^logout/', logout, name="logout"),
    url(r'^login/', login, name="login"),
    url(r'^register/', registration, name="registration"),
    url(r'^password-reset/', include(url_reset)),
    url(r'^orders/$', orders, name='orders'),
    url(r'^contact/', contact, name="contact"),
]
