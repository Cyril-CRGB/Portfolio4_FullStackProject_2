from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from .models import ParkingSlot, Booking
from .forms import BookingForm


# View to handle booking a slot
# @login_required  Ensure the user is logged in
def book_slot(request):
    if request.method == 'POST':
        form = BookingForm(request.POST)
        if form.is_valid():
            booking = form.save(commit=False)
            booking.user = request.user # Associate booking with the logged-in user
            slot = booking.slot

            # Check if the slot is available for the selected time
            overlapping_bookings = Booking.objects.filter(
                slot=slot,
                start_time__lt=booking.end_time,
                ent_time__gt=booking.start_time,
            )
            if overlapping_bookings.exists():
                messages.error(request, 'This slot is already booked for the chosen time.')
            else:
                booking.save()
                messages.success(request, 'Your booking has been successfully created.')
                return redirect ('booking_success')

    else:
        form = BookingForm()

    return render(request, 'car_park_manager/book_slot.html', {'form': form})


# View to display booking success message
#@login_required  Ensure the user is logged in
def booking_success(request):
    return render(request, 'car_park_manager/booking_success.html')


# View to display booking calendar
#@login_required  Ensure the user is logged in
def calendar_view(request):
    return render(request, 'car_park_manager/calendar.html')