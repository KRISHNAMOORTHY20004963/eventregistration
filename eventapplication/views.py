from django.shortcuts import render
from .models import participant

# Create your views here.
def home(request):
    context = {}
    return render(request, 'eventapplication/home.html' , context)



def registration(request):
    context = {}
    if request.method == 'POST':
        p1 = participant()
        p1.username = request.POST.get('username','-')
        p1.email = request.POST.get('email','-')
        p1.phone = request.POST.get('phone', '000')
        p1.instituition = request.POST.get('instituition', '-')

        if len(participant.objects.all()) > 15:
             return render(request, 'eventapplication/failed.html',context)
        else:
            p1.save()
            return render(request, 'eventapplication/success.html',context)

    if request.method == 'GET':
        context['username'] = ''
        context['email'] = ''
        context['phone'] = ''
        context['instituition'] = ''

    return render(request, 'eventapplication/registration.html',context)

def listofparticipant(request):
    context = {}
    return render(request, 'eventapplication/listofparticipant.html',context)

def succes(request):
    context = {}
    return render(request, 'eventapplication/succes.html' , context)

