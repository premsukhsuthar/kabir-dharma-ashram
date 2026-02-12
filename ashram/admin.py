from django.contrib import admin

# Register your models here.
# from .models import Event
# admin.site.register(Event)
from .models import Event, GalleryImage, ContactMessage, DonationInfo

admin.site.register(Event)
admin.site.register(GalleryImage)
admin.site.register(ContactMessage)
admin.site.register(DonationInfo)

