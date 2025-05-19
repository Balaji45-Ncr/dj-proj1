from django.urls import path,include
from . import views



app_name='blog'

urlpatterns=[
    path('',views.index.as_view(),name='index'),
    path('post/<int:id>',views.detail.as_view(),name='detail'),
    path('new_url/<int:id>',views.new_url_view,name='new_url'),
    path('old_url/<int:id>',views.old_url_redirect,name='old_url')

]