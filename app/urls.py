from django.urls import path
from .views import *

urlpatterns = [
    path('', home),
    path('new', new),
    path('delete', delete)
]