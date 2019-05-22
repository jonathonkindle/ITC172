from django.contrib import admin
from .models import Meeting, MeetingMinutes, ResourceType, Resource, Event

# Register your models here.
admin.site.register(Meeting)
admin.site.register(MeetingMinutes)
admin.site.register(ResourceType)
admin.site.register(Resource)
admin.site.register(Event)