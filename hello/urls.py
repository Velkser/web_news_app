from django.urls import path
from hello.views import home
from hello.views import about
from hello.views import increase

urlpatterns = [
    path('', home, name="home"),
    path('about/', about, name="about"),
    path('increase/', increase, name="increase")
]
