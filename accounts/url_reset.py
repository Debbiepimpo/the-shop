from django.urls import re_path
from django.urls import reverse_lazy
from django.contrib.auth.views import PasswordResetView, PasswordResetDoneView, PasswordResetConfirmView, PasswordResetCompleteView

urlpatterns = [re_path('^$',
                   PasswordResetView.as_view(),
                   {'post_reset_redirect': reverse_lazy('password_reset_done')},
                   name='password_reset'),
               re_path(r'^done/$',
                   PasswordResetDoneView.as_view(),
                   name='password_reset_done'),
               re_path(r'^(?P<uidb64>[0-9A-Za-z]+)-(?P<token>.+)/$',
                   PasswordResetConfirmView.as_view(),
                   {'post_reset_redirect': reverse_lazy('password_reset_complete')},
                   name='password_reset_confirm'),
               re_path('^complete/$',
                   PasswordResetCompleteView.as_view(),
                   name='password_reset_complete')]