from django.db import models
from django.contrib.auth.models import User 

# Model to represent a parking slot
class ParkingSlot(models.Model):
    number = models.CharField(max_length=10) # Slot number or identifier
    location = models.CharField(max_length=100) # Location of the parking slot
    is_available = models.BooleanField(default=True) # Availabitiy status

    def __str__(self):
        return f"Slot {self.number} at {self.location}"

# Model to represent a booking
class Booking(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE) # User who made the booking
    slot = models.ForeignKey(ParkingSlot, on_delete=models.CASCADE) # Booked slot
    start_time = models.DateTimeField() # Booking start time
    end_time = models.DateTimeField() # Booking end time
    created_at = models.DateTimeField(auto_now_add=True) # Timestamp when the booking was made

    def __str__(self):
        return f"{self.user.username} booking for {self.slot.number} from {self.start_time} to {self.end_time}"



