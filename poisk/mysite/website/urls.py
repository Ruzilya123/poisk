# from django.conf.urls import urls
from . import views
from django.urls import path, include

urlpatterns = [
    path('', views.index, name='index'),
    path('search/', views.search)
]