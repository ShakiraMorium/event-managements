from django.urls import path
from . import views
from .views import event_list

urlpatterns = [
    path('', views.home_view, name='home'),

    path('dashboard/', views.dashboard_view, name='dashboard'),
    path('all_event/', views.all_event_view, name='all_event'),
    path('test/', views.test_view, name='test'),
]
