from django.contrib import admin
from .models import City, Users, Forecast

# Register your models here.
admin.site.register(City)
admin.site.register(Users)
admin.site.register(Forecast)