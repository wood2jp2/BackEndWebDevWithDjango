from django.urls import path
from . import views

urlpatterns = [
    path('home/', views.namastePage, name='namaste'),
]