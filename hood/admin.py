from django.contrib import admin
from .models import UserProfile, NeighborHood, Business

# Register your models here.

#admin.site.register(Business)
admin.site.register(UserProfile)
admin.site.register(NeighborHood)
admin.site.register(Business)