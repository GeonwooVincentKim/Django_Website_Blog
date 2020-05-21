from django.conf.urls import url, include
# from django.contrib.auth.views import LogoutView
from . import views
from django.contrib import admin
from django.views.generic.base import TemplateView  # new
from django.contrib.auth.views import (
    login, logout, password_reset, password_reset_done, password_reset_confirm,
    password_reset_complete
)

urlpatterns = [
    url(r'^$', views.post_list, name='post_list'),
    # 1회 이상 반복 : pk
    # d+ 자리 수가 몇 자리까지 올지 모르므로 사용합니다.
    # 1 ~ 9까지의 숫자가 오는 것을 알리기 위해 (?P)를 사용합니다.
    url(r'^post/', include('django.contrib.auth.urls')),
    url(r'^post/(?P<pk>\d+)/$', views.post_detail, name='post_detail'),
    url(r'^post/new/$', views.post_new, name='post_new'),
    url(r'^post/(?P<pk>\d+)/edit/$', views.post_edit, name='post_edit'),
    url(r'^post/(?P<pk>\d+)/delete/$', views.post_delete, name='post_delete'),

    # When users have logged on to the site, go back to base.html.
    # url(r'^accounts/', include('django.contrib.auth.urls')),
    url(r'^signup/', views.SignUp.as_view(), name='signup'),
    url(r'^change-password/',
        views.change_password,
        name='change_password'),
    url(r'', TemplateView.as_view(template_name='base.html'), name='base'),

    # Reset Password
    # url(r'^post/password_reset/$', password_reset, {
    #     'template_name': 'password_reset_form.html',
    #     'post_reset_redirect': 'registration/password_reset_done.html',
    #     'email_template_name': 'registration/password_reset_email.html'},
    #     name='reset_password'),
    #
    # url(r'^post/password_reset_done/$', password_reset_done, {
    #     'template_name': 'registration/password_reset_done.html'},
    #     name='password_reset_done'),
    #
    # url(r'^post/reset/MQ/(?P<uidbd64>[0-9A-Za-z]+)-(?P<token>.+)/$', password_reset_confirm,
    #     {'template_name': 'registration/password_reset_confirm.html',
    #      'post_reset_redirect': 'registration/password_reset_complete'},
    #     name='password_reset_confirm'),
    #
    # url(r'^post/reset/complete/$', password_reset_complete, {'template_name':
    # 'registration/password_reset_complete.html'}, name='password_reset_complete'),

    # url(r'^password_reset/$', views.password_reset),
]
