from django.urls import path
from .views import *

urlpatterns = [
    path('', sampleFormView, name='forecast_url'),
]
