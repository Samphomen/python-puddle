from django.urls import path

from . import views

app_name = 'core'

urlspattern = [
    path('', views.index, name='index')
]