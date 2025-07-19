from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required
from django.views.generic import DetailView
from .models import Category, Event
from users.utils import organizer_required  # Make sure this exists or remove


def test_view(request):
    return render(request, 'events/test.html')


# Home view - show latest 6 events
def home_view(request):
    events = Event.objects.all()[:6]
    return render(request, 'events/home.html', {'events': events})

# All events view (requires login)
@login_required
def all_event_view(request):
    events = Event.objects.all()
    return render(request, 'events/all_events.html', {'events': events})

# Dashboard view (requires login)
@login_required
def dashboard_view(request):
    events = Event.objects.filter(organizer=request.user)
    return render(request, 'dashboard/dashboard.html', {'events': events})

# Event detail view by primary key
def event_detail(request, pk):
    event = get_object_or_404(Event, pk=pk)
    return render(request, 'events/event_detail.html', {'event': event})

# Alternative class-based detail view (optional)
class EventDetailView(DetailView):
    model = Event
    template_name = 'events/event_detail.html'
    context_object_name = 'event'

# Event list view with related objects prefetched
def event_list(request):
    events = Event.objects.select_related('category').prefetch_related('participants').all()
    return render(request, 'events/event_list.html', {'events': events})

# Organizer-only event creation view
@organizer_required
def create_event(request):
    categories = Category.objects.all()
    if request.method == 'POST':
        title = request.POST.get('title')
        description = request.POST.get('description')
        date = request.POST.get('date')
        location = request.POST.get('location')
        category_id = request.POST.get('category')

        Event.objects.create(
            title=title,
            description=description,
            date=date,
            location=location,
            category_id=category_id,
            organizer=request.user
        )
        # Redirect to all_event page after creation
        return redirect('all_event')

    return render(request, 'events/create_event.html', {'categories': categories})
