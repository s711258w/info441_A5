from django.urls import path, include
from helloapp import views

urlpatterns = [
    path('', views.register, name="register"),
]
