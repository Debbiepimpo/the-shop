import base64
import io

from PIL import Image
from django.contrib.admin.views.decorators import staff_member_required
from django.http import HttpResponseNotFound
from django.shortcuts import render, get_object_or_404

from django.contrib.auth.decorators import login_required
from rest_framework.decorators import api_view


from .models import Items
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger

users = []


# Create your views here.
@login_required
def articles_to_sell(request):
    """View to display all Professional Services"""
    articles_all = Items.objects.all().order_by(
            '-id'
    ).exclude(status="Current Unavailable")
    for article in articles_all:
        print(type(article.photo))
    paginator = Paginator(articles_all, 9)  # Show 5 Items per page

    page = request.GET.get('page')
    try:
        articles_all = paginator.page(page)
    except PageNotAnInteger:
        articles_all = paginator.page(1)
    except EmptyPage:
        articles_all = paginator.page(paginator.num_pages)
    return render(request, "articles_to_sell.html", {"articles_all": articles_all})


@login_required
def article_detail(request, pk):
    """
    This view that returns a single
    article object details or if is not found
    return 404 error if object is not found.
    """

    article_det = get_object_or_404(Items, pk=pk)

    return render(request, "article_detail.html", {"article_det": article_det})

