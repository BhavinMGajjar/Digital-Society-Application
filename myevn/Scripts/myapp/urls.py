from django.urls import path
from . import views


urlpatterns = [
    
    path('', views.index, name='index'),
    path('login/', views.login, name='login'),
    path('logout/', views.logout, name='logout'),
    path('forgot-password/',views.forgot_password, name='forgot-password'),
    path('verify-otp/',views.verify_otp, name='verify-otp'),
    path('profile/', views.profile, name='profile'),
    path('members/', views.members, name='members'),
    path('watchmen/', views.watchmen, name='watchmen'),
    path('notice/', views.notice, name='notice'),
    path('events/', views.events, name='events')


  ]