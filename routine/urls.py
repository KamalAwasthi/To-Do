from django.urls import path
from . import views
from django.conf.urls import url

urlpatterns = [
	url(r'^$', views.todo_list, name='todo_list'),
	url(r'^todo_complete/(?P<pk>\d+)/$', views.todo_complete, name='todo_complete'),
]