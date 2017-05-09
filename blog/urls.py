from django.conf.urls import url
from . import views

urlpatterns = [
    url(r'^$', views.post_list, name='post_list'),
    url(r'^post/(?P<pk>\d+)/$', views.post_detail, name='post_detail'),
    url(r'^post/new/$', views.post_new, name='post_new'),
    url(r'^post/(?P<pk>\d+)/edit/$', views.post_edit, name='post_edit'),
    url(r'^login/$',views.login,name='login'),
    url(r'^invalid/$',views.invalid_login,name='invalid'),
    url(r'^logout/$',views.logout,name='logout'),
    url(r'auth/$',views.auth_view),
]