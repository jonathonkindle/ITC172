from django.shortcuts import render, get_object_or_404
from .models import Meeting, MeetingMinutes, ResourceType, Resource, Event
from .forms import MeetingForm, ResourceForm
from django.contrib.auth.decorators import login_required

# Create your views here.
def index (request):
    return render(request, 'PythonClubApp/index.html')

def loginmessage(request):
    return render(request, 'PythonClubApp/loginmessage.html')

def logoutmessage(request):
    return render(request, 'PythonClubApp/logoutmessage.html')

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

@login_required
def newmeeting(request):
    form=MeetingForm()
    if request.method=='POST':
        form=MeetingForm(request.POST)
        if form.is_valid():
            post=form.save(commit=True)
            post.save()
            form=MeetingForm()
    else:
        form=MeetingForm()
    return render(request, 'PythonClubApp/newmeeting.html', {'form': form})

@login_required
def newresource(request):
    form=ResourceForm()
    if request.method=='POST':
        form=ResourceForm(request.POST)
        if form.is_valid():
            post=form.save(commit=True)
            post.save()
            form=ResourceForm()
    else:
        form=ResourceForm()
    return render(request, 'PythonClubApp/newresource.html', {'form': form})