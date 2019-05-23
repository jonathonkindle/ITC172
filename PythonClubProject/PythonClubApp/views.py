from django.shortcuts import render
from .models import Meeting, MeetingMinutes, ResourceType, Resource, Event

# Create your views here.
def index (request):
    return render(request, 'PythonClubApp/index.html')

def getresources(request):
    resource_list=Resource.objects.all()
    return render(request, 'PythonClubApp/resources.html', {'resource_list' : resource_list})