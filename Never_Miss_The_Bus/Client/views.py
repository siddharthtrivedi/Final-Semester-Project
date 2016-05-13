from django.shortcuts import render,get_object_or_404
from django.http import HttpResponseRedirect
from App_Admin.models import Bus, Route
import json
# from django.utils import simplejson
# Create your views here.

# def client_home(request):
# 	buses = Bus.objects.all()
# 	template = "client_home_1.html"
# 	# template = "client_home.html"
# 	context = {'buses' : buses}
# 	if request.method == 'POST':
# 		selected_bus = request.POST.get('bus_select')
# 		# print(selected_bus)
# 		selected_bus = get_object_or_404(Bus, pk=selected_bus)
# 		selected_bus_route = get_object_or_404(Route, pk=selected_bus.route_id)
# 		stops = selected_bus_route.stops.all()
# 		json_origin_stop = json.dumps(selected_bus_route.origin.stop_name)

# 		stop_names = []
# 		json_stops = []
# 		for stop in stops:
# 			stop_names.append(stop.stop_name)
# 			# print(stop.stop_name)
# 			# json_stops.append(json.loads(stop.stop_name))

# 		json_stops = json.dumps(stop_names)
# 		# print(json_stops)

# 		context = {'stops': stops, 'json_stops' : json_stops, 'stop_names' : stop_names, 'json_origin_stop':json_origin_stop, 'buses' : buses, 'selected_bus' : selected_bus}


# 	return render(request, template, context)

def client_home(request):
	if request.user.is_superuser:
	    redirect_to = "/admin"
	    return HttpResponseRedirect(redirect_to)

	elif request.user.is_staff:
	    redirect_to = "/app_admin"
	    return HttpResponseRedirect(redirect_to)

	else:
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
			json_origin_stop_lat = json.dumps(selected_bus_route.origin.latitude)
			json_origin_stop_lon = json.dumps(selected_bus_route.origin.longitude)

			stop_lat = []
			stop_lon = []

			json_stops_lat = []
			json_stops_lon = []

			for stop in stops:
				stop_lat.append(stop.latitude)
				stop_lon.append(stop.longitude)
				# print(stop.stop_name)
				# json_stops.append(json.loads(stop.stop_name))

			json_stops_lat = json.dumps(stop_lat)
			json_stops_lon = json.dumps(stop_lon)
			# print(json_stops)

			context = {'stops': stops, 'json_stops_lat' : json_stops_lat, 'json_stops_lon' : json_stops_lon, 'json_origin_stop_lat':json_origin_stop_lat, 'json_origin_stop_lon':json_origin_stop_lon, 'buses' : buses, 'selected_bus' : selected_bus}


	return render(request, template, context)

def client_home1(request):
	context = {}
	template = "client_home.html"

	return render(request, template, context)


	# if request.method == 'POST':
	# 	selected_bus = get_object_or_404(Bus, pk=(request.POST.get('bus_id')))

	# else:
		

