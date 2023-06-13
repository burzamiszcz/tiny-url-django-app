from django.urls import path
from . import views

urlpatterns = [
    path('', views.tinyurl),
    path('<str:tiny_url>', views.tinyurl),
]