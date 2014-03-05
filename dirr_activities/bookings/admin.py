from django.contrib import admin
from bookings.models import Booking, BookingOptions, People


admin.site.register(Booking)
admin.site.register(BookingOptions)
admin.site.register(People)
