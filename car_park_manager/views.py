from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from django.contrib import messages

# View to display base
#@login_required  Ensure the user is logged in
def index_view(request):
    if request.user.is_authenticated:
        return redirect('calendar')
    return render(request, 'car_park_manager/index.html')


# View to display booking calendar
#@login_required  Ensure the user is logged in
def calendar_view(request):
    return render(request, 'car_park_manager/calendar.html')

