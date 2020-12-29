from django.urls import path
from . import views
from django.contrib.auth import views as auth_views

urlpatterns = [
  path('signup/', views.signup,  name='signup'),
  path('login/', views.login, name='login'),
  path('logout/', views.logout, name='logout'),
  path('password_change/', views.password_change, name='password_change'),
]
