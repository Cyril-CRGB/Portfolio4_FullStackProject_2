from django import forms
from .models import Booking

# Form for creating a booking
class BookingForm(forms.ModelForm):
    class Meta:
        model = Booking
        fields = ['slot', 'start_time', 'end_time'] # Fields to include in the form

    # Custom validation for the form
    def clean(self):
        cleaned_data = super().clean()
        start_time = cleaned_data.get('start_time')
        end_time = cleaned_data.get('end_time')

        # Ensure end time is after start time
        if end_time <= start_time:
            raise forms.ValidationError("End time must be after start time.")

        # Ensure the booking duration is at least half a day (12 hours)
        if (end_time - start_time).total_seconds() < 43200:
            raise forms.ValidationError("The booking must be for at least half a day (12 hours).")