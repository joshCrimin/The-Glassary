from django.urls import path
from glassary import views

urlpatterns = [
    path('', views.index, name='index'),
]