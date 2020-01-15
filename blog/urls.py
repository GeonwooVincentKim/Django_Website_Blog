from django.conf.urls import url, include
# from django.contrib.auth.views import LogoutView
from . import views
from django.contrib import admin
from django.views.generic.base import TemplateView # new

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
    url(r'', TemplateView.as_view(template_name='base.html'), name='base'),
]
