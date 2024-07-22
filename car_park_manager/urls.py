from django.urls import path
from . import views

urlpatterns = [
    path('', views.index_view, name='index'), # URL for base
    path('calendar/', views.calendar_view, name='calendar'), # URL for booking success
]