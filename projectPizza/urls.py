from django.urls import path

from projectPizza import views
urlpatterns = [
    path('', views.home,name='home'),
    path('menu/', views.menu,name='menu'),
    path('about/', views.about,name='about'),
    path('services/', views.services,name='services'),
    path('contact/', views.contact,name='contact'),
]