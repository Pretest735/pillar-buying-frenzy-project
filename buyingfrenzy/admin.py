from django.contrib import admin
from .models import Restaurant, Menu, OpenHours, User, PurchaseHistory

# Register your models here.
admin.site.register(Restaurant)
admin.site.register(Menu)
admin.site.register(OpenHours)
admin.site.register(User)
admin.site.register(PurchaseHistory)
