from django.shortcuts import render,get_object_or_404
from App_Admin.models import Bus, Route
import json
# from django.utils import simplejson
# Create your views here.

def client_home(request):
	buses = Bus.objects.all()
	template = "client_home_1.html"
	# template = "client_home.html"
	context = {'buses' : buses}
	if request.method == 'POST':
		selected_bus = request.POST.get('bus_select')
		# print(selected_bus)
		selected_bus = get_object_or_404(Bus, pk=selected_bus)
		selected_bus_route = get_object_or_404(Route, pk=selected_bus.route_id)
		stops = selected_bus_route.stops.all()
		json_origin_stop = json.dumps(selected_bus_route.origin.stop_name)

		stop_names = []
		json_stops = []
		for stop in stops:
			stop_names.append(stop.stop_name)
			# print(stop.stop_name)
			# json_stops.append(json.loads(stop.stop_name))

		json_stops = json.dumps(stop_names)
		# print(json_stops)

		context = {'stops': stops, 'json_stops' : json_stops, 'stop_names' : stop_names, 'json_origin_stop':json_origin_stop}


	return render(request, template, context)

	# if request.method == 'POST':
	# 	selected_bus = get_object_or_404(Bus, pk=(request.POST.get('bus_id')))

	# else:
		

