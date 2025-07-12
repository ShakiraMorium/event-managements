
from django.urls import path
from .views import event_view

urlpatterns = [
    path('event/', event_view, name='event-view'),
]