from django.http import HttpResponse, JsonResponse
from events.models import Event

def home_view(request):
    events = Event.objects.all()
    event_list = list(events.values('id', 'title', 'description'))
    return JsonResponse({'events': event_list})