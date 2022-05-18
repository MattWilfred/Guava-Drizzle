from django.urls import path
from .models import Data, DataB

from . import views

urlpatterns = [
    path("", views.index, name="landing_page"),
    path("home/", views.home, name="home"),
    path("aboutus/", views.aboutus, name="aboutus"),
    path("contactus/", views.contactus, name="contactus"),
    path('predictcrop/', views.predictcrop, name='predictcrop'),
    path('predictedcrops/', views.predictedcrops, name='predictedcrops'),
    path('checkoptimal/', views.checkoptimal, name='checkoptimal'),
    path('information_page/',views.information_page, name='information_page')
]