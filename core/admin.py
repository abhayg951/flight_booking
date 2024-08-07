from django.contrib import admin
from .models import Booking, Flight, User, locations

# Register your models here.

@admin.register(Flight)
class FlightAdmin(admin.ModelAdmin):
    list_display = ('flight_number', 'departure_time', 'arrival_time', 'source', 'destination', 'available_seats')
    list_filter = ('source', 'destination', 'departure_time', 'arrival_time')
    search_fields = ('flight_number', 'source', 'destination')

@admin.register(Booking)
class BookingAdmin(admin.ModelAdmin):
    list_display = ('user', 'get_user_email', 'flight', 'get_flight_number', 'get_departure_time', 'booked_on')
    list_filter = ('flight__flight_number', 'flight__departure_time', 'booked_on')
    search_fields = ('user__username', 'user__email', 'flight__flight_number', 'flight__departure_time')

    def get_user_email(self, obj):
        return obj.user.email
    get_user_email.short_description = 'User Email'
    get_user_email.admin_order_field = 'user__email'

    def get_flight_number(self, obj):
        return obj.flight.flight_number
    get_flight_number.short_description = 'Flight Number'
    get_flight_number.admin_order_field = 'flight__flight_number'

    def get_departure_time(self, obj):
        return obj.flight.departure_time
    get_departure_time.short_description = 'Departure Time'
    get_departure_time.admin_order_field = 'flight__departure_time'
# admin.site.register(Flight, FlightAdmin)
admin.site.register(User)
admin.site.register(locations)
