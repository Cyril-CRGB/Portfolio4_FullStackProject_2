from django.urls import path
from . import views

urlpatterns = [
    path('', views.book_slot, name='book_slot'), # URL for booking a slot
    path('booking_success/', views.booking_success, name='booking_success'), # URL for booking success
    path('calendar/', views.calendar_view, name='calendar'), # URL for booking success
]