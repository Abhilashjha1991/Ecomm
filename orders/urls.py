from django.urls import path

from .views import *

urlpatterns = [
         path('order_create/',order_create,name='order_create'),
         
    ]
