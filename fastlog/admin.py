from django.contrib import admin

from .models import *

admin.site.register(DriverUser)
admin.site.register(BookerUser)
admin.site.register(Order)

# Register your models here.
