from django.shortcuts import render, get_object_or_404
from .models import Meeting, MeetingMinutes, ResourceType, Resource, Event

# Create your views here.
def index (request):
    return render(request, 'PythonClubApp/index.html')

def getresources(request):
    resource_list=Resource.objects.all()
    return render(request, 'PythonClubApp/resources.html', {'resource_list' : resource_list})

def getmeetings(request):
    meetings_list=Meeting.objects.all()
    return render(request, 'PythonClubApp/meetings.html', {'meetings_list' : meetings_list})

def meetingdetails(request, id):
    meet=get_object_or_404(Meeting, pk=id)
    context={'meet' : meet}
    return render(request, 'PythonClubApp/meetingdetails.html', context=context)
