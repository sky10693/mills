from django.contrib import admin
from django.urls import path
from home import views

urlpatterns = [
    path('', views.index, name='home'),
    path('contact/', views.contact, name='contact'),
    path('flours/', views.flours, name='flours'),
    path("spices/", views.spices, name="spices")
]