from django.urls import path
from app.views import *
app_name='special'
urlpatterns=[
    path('virat/',virat,name='virat')
]