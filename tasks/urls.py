from django.conf.urls import patterns, url

from . import views

urlpatterns = patterns('',
  url(r'^$', views.tasklist_list, name='tasklist_list'),
  url(r'^new$', views.tasklist_create, name='tasklist_new'),
  url(r'^(?P<pk>\d+)$', views.tasklist, name='tasklist'),
  url(r'^edit/(?P<pk>\d+)$', views.tasklist_update, name='tasklist_edit'),
  url(r'^delete/(?P<pk>\d+)$', views.tasklist_delete, name='tasklist_delete'),
  url(r'^new_task/(?P<pk>\d+)$', views.task_create, name='task_new'),
  url(r'^task/edit/(?P<pk>\d+)$', views.task_update, name='task_edit'),
  url(r'^task/delete/(?P<pk>\d+)$', views.task_delete, name='task_delete'),
  url(r'^(?P<pk>\d+)/task_sort$', views.task_sort, name='task_sort'),
)
