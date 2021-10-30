from django.contrib import admin
from .models import Condition, Region, Vendor, Phone

# Register your models here.
admin.site.register(Condition)
admin.site.register(Vendor)
admin.site.register(Phone)
admin.site.register(Region)