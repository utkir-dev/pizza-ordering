from django.urls import path

from projectPizza.views import index
urlpatterns = [
    path('', index),
]