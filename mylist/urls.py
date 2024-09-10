from django.urls import path
from mylist.views import *

urlpatterns = [
    path('', mylist, name='mylist'),
]