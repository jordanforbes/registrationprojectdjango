from django.urls import path
from . import views 
from wall import views as wall

urlpatterns = [
    path('', views.index),
    path('register', views.register),
    path('success', views.success),
    path('<user_id>/destroy', views.destroy),
    path('logout', views.logout),
    path('login', views.login),
    path('loginpage', views.index),
    path('wall', wall.home)
]
