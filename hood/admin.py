from django.contrib import admin
from .models import UserProfile, Business, NeighbourHood

# Register your models here.

admin.site.register(Business)
admin.site.register(UserProfile)
admin.site.register(NeighbourHood)