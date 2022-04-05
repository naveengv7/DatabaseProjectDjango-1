from django.urls import path
from django.contrib import admin
from . import views

urlpatterns = [
    path('', views.administrator, name='admin'),
    path('admin/f1/', views.f1),
    path('admin/f2/', views.f2),
    path('admin/f3/', views.f3),

]


