from django.contrib import admin
from django.urls import path
from . import views

urlpatterns = [
    path('pronounce/', views.translate, name='translate'),
]
