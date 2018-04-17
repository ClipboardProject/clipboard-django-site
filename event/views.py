from django.http import Http404
from django.shortcuts import render, get_object_or_404
from .models import Event

def index(request):
	all_events = Event.objects.all()
	return render(request, 'event/index.html', {'all_events': all_events})

def detail(request, event_id):
	event = get_object_or_404(Event, pk=event_id)
	return render(request, 'event/detail.html', {'event': event})

def url_redirect(request):
	return HttpResponseRedirect('/events')
