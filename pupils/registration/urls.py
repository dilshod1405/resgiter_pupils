from .views import registration, pupils
from django.urls import path

urlpatterns = [
    path('', registration, name='registration'),
    path('pupils', pupils, name='pupils'),
    path('index.html', registration, name='index'),
    path('pupils.html', pupils, name='pupils.html'),
]