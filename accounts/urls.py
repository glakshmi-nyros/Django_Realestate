from django.conf.urls import url

from . import views

urlpatterns = [
    url('login', views.login,name='login'),
    url('register', views.register,name='register'),
    url('logout', views.logout,name='logout'),
    url('dashboard', views.dashboard,name='dashboard'),

    
]