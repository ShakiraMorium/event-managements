"""
URL configuration for event_management project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path,include
from events.views import home_view, dashboard_view
from django.conf import settings
from events import views
from django.conf.urls.static import static
from events.views import EventDetailView   
from users.views import login_view,signup_view


urlpatterns = [
    path('admin/', admin.site.urls),
    path('',home_view, name='home'),
    path('all_event/', views.all_event_view, name='all_event'),
    path('dashboard/', dashboard_view, name='dashboard'),
    # path('', include('events.urls')),
    path('users/', include('users.urls')),
    path('events/<int:pk>/', EventDetailView.as_view(), name='event_detail'),
    path('accounts/', include('django.contrib.auth.urls')), 
    path('login/', login_view, name='login'),
    path('signup/', signup_view, name='signup'),
]
 

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)