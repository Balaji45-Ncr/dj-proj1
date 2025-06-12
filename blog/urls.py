from django.urls import path,include
from . import views



app_name='blog'

urlpatterns=[
    path('',views.index.as_view(),name='index'),
    path('post/<int:pk>',views.Detail.as_view(),name='detail'),
    path('new_url/<int:id>',views.new_url_view,name='new_url'),
    path('old_url/<int:id>',views.old_url_redirect,name='old_url'),
    path('contact/',views.Contact.as_view(),name='contact'),
    path('thanks/',views.Thanks.as_view(),name='thanks'),
    path('register/',views.Register.as_view(),name='register'),
    path('login/',views.Login.as_view(),name='login'),
    path('dashboard/',views.Dashboard.as_view(),name='dashboard'),
    path('logout/',views.Logout.as_view(),name='logout'),

]