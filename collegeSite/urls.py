from django.urls import path

from . import views


urlpatterns = [
    path('homepage/', views.index) #our-domain.com/homepage
]