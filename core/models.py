from django.db import models
from django.contrib.auth.models import AbstractUser

class User(AbstractUser):
    email = models.EmailField(unique=True)
    name = models.CharField(max_length=150)
    address = models.TextField()
    postal_code = models.PositiveIntegerField(max_length=6, null=True)
    city = models.CharField(max_length=100, null=True)

    def __str__(self) -> str:
        return f"{self.name}"

class locations(models.Model):
    name = models.CharField(max_length=100)

    def __str__(self) -> str:
        return f"{self.name}"

class Flight(models.Model):
    flight_number = models.CharField(max_length=10, unique=True)
    departure_time = models.DateTimeField()
    arrival_time = models.DateTimeField()
    source = models.ForeignKey(locations, on_delete=models.CASCADE, related_name="departure_flights", verbose_name="From")
    destination = models.ForeignKey(locations, on_delete=models.CASCADE, related_name="arrival_flights", verbose_name="To")
    available_seats = models.PositiveIntegerField(default=60)

    def __str__(self) -> str:
        return f"{self.flight_number}"

class Booking(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    flight = models.ForeignKey(Flight, on_delete=models.CASCADE)
    booked_on = models.DateTimeField(auto_now_add=True)

    def __str__(self) -> str:
        return f"{self.user.name}"
