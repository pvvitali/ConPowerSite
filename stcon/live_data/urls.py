
from django.urls import path
from .views import *

urlpatterns = [
    path('', index),
    path('st/<int:st_id>/', station),
]