from django.urls import path
from . import views

urlpatterns = [
    path('', views.signup, name='signup'),
    path('signin/', views.signin, name='signin'),
    path('signout/', views.signout, name='signout'),
    path('index/', views.index, name='index'),
    path('username_check/', views.username_check, name='username_check'),
    path('userupdate/', views.userupdate, name='userupdate'),
]