from django.contrib import admin
from django.urls import path,include
urlpatterns = [
    path('f/',include('django.contrib.auth.urls'))
]