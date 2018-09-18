from django.http import Http404
from django.shortcuts import render, get_object_or_404
#from .models import Event
import requests

class EventData:
	events = None

	@staticmethod
	def get_event(event_id):
		return next(e for e in EventData.events if e['id'] == event_id)

def index(request):
	events_response = requests.get(f'http://192.168.99.100:5000/getevents', params= {
        'start_timestamp': 0, 
        'end_timestamp': 10000000000
    })
	#all_events = [Event.objects.create(**event) for event in events.json()]
	#all_events = Event.objects.all()
	EventData.events = events_response.json()
	#request.session['events'] = events
	return render(request, 'event/index.html', {'all_events': EventData.events})

def detail(request, event_id):
	#events = request.session['events']

	event = EventData.get_event(event_id)
	#event = get_object_or_404(Event, pk=event_id)
	return render(request, 'event/detail.html', {'event': event})

def url_redirect(request):
	return HttpResponseRedirect('/events')
