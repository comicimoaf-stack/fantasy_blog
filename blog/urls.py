from django.urls import path
from . import views


urlpatterns = [
path('', views.home, name='home'),
path('about/', views.about, name='about'),
path('post/new/', views.create_post, name='create_post'),
]