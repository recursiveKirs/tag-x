from django.conf.urls import url
from . import views

urlpatterns = [
    url(r'^$', views.index, name='index'),
    url(r'^mysystems/$', views.mysystems, name='mysystems'),
    url(r'^system/$', views.system, name='system'),
    url(r'^login/$', views.login, name='login'),
    url(r'^logout/$', views.logout, name='logout'),
    url(r'^mygroups/$', views.mygroups, name='mygroups'),
    url(r'^administration/$', views.administration, name='administration'),
    url(r'^search/$', views.search, name='search'),
    # for alpha release
    url(r'^elastic/$', views.elastic, name='elastic'),
]

