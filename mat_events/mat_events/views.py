from django.views.generic import DetailView
from django.shortcuts import render
from .models import MatEvent, HireService, PrivateSession

def home(request):
    return render(request, 'index.html')

class MatEventDetailView(DetailView):
    model = MatEvent
    template_name = 'mat_events/mat_event_detail.html'
    context_object_name = 'event'

class HireServiceDetailView(DetailView):
    model = HireService
    template_name = 'mat_events/hire_service_detail.html'
    context_object_name = 'service'

class PrivateSessionDetailView(DetailView):
    model = PrivateSession
    template_name = 'mat_events/private_session_detail.html'
    context_object_name = 'session'

def events_list(request):
    events = MatEvent.objects.all().order_by('date')
    return render(request, 'mat_events/events_list.html', {'events': events})

def hire_services_list(request):
    services = HireService.objects.filter(is_available=True)
    return render(request, 'mat_events/hire_services_list.html', {'services': services})

def private_sessions_list(request):
    sessions = PrivateSession.objects.filter(is_available=True)
    return render(request, 'mat_events/private_sessions_list.html', {'sessions': sessions})