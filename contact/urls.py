from django.contrib import admin
from django.urls import path
from . import views


urlpatterns = [
    path('', views.contact, name='contact'),
    path('returns/', views.r_and_e, name='r_and_e'),
    path('policies/', views.policies_page, name='policies_page'),
]
