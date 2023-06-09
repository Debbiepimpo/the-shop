"""Shopping URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.conf import settings
from django.conf.urls.static import static
from django.contrib import admin
from django.contrib.staticfiles.urls import staticfiles_urlpatterns
from django.urls import re_path, include
from accounts.views import index
from accounts import urls as accounts_urls
from items import urls as urls_articles
from cart import urls as urls_cart
from checkout import urls as urls_checkout


urlpatterns = [
    re_path(r'^admin/', admin.site.urls),
    re_path(r'^$', index, name="index"),
    re_path(r'^accounts/', include(accounts_urls)),
    re_path(r'^articles/', include(urls_articles)),
    re_path(r'^cart/', include(urls_cart)),
    re_path(r'^checkout/', include(urls_checkout)),
]

urlpatterns += staticfiles_urlpatterns()
urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)