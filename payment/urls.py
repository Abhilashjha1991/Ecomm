from django.urls import path

from .views import *

urlpatterns = [
         path('payment_process/',payment_process,name='payment_process'),
         path('payment_done/',payment_done,name='payment_done'),
         path('payment_canceled/',payment_canceled,name='payment_canceled'),
         
    ]
