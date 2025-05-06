# /myproject/myapp/urls.py
from django.urls import path
from .views import home
from . import views

urlpatterns = [
    path('', home, name='home'),  # Home page at root URL
    path('search/', views.search_results, name='search_results'), # Search tab in home page
    path('', views.home, name='home'),
    path('room/<uuid:room_id>/', views.room_detail, name='room_detail'),
]