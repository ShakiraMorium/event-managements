from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.

# from .models import Event

#home view
def home_view(request):
    return HttpResponse('welcome')

#contact
def contact_view(request):
    return  HttpResponse('contact')

#dashboard
def dashboard_view(request):
    return  HttpResponse('dashboard')


# def event_view(request):
#     event = Event.objects.first()
#     return HttpResponse(f"Event: {event.title} - {event.description}")