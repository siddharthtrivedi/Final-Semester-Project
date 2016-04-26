from . import forms, models
from django import forms as django_forms
from django.views.generic import ListView
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.apps import apps
from django.shortcuts import render
from django.core.urlresolvers import reverse_lazy
from django.http import HttpResponseRedirect

# Create your views here.

class ReporterList(ListView):
	model = models.Coord_Reporter
	template_name = 'list_tables.html'
	
	def get_context_data(self, **kwargs):
		context = super(ReporterList, self).get_context_data(**kwargs)
		context['title'] = 'Reporters'
		notifications = models.Coord_Reporter_Request.objects.filter(respond_status='NVR');
		notifications_count = len(notifications)
		context['notifications'] = notifications
		context['notifications_count'] = notifications_count
		return context

class ReporterCreate(CreateView):
	model = models.Coord_Reporter
	form_class = forms.Reporter_Form
	template_name = 'create_form.html'
	
	success_url = reverse_lazy('App_Admin:reporter_list')
	def get_context_data(self, **kwargs):
		context = super(ReporterCreate, self).get_context_data(**kwargs)
		context['title'] = 'Add Reporter'
		notifications = models.Coord_Reporter_Request.objects.filter(respond_status='NVR');
		notifications_count = len(notifications)
		context['notifications'] = notifications
		context['notifications_count'] = notifications_count
		return context

class ReporterUpdate(UpdateView):
	model = models.Coord_Reporter
	form_class = forms.Reporter_Form
	template_name = 'update_form.html'
	
	success_url = reverse_lazy('App_Admin:reporter_list')

	def get_context_data(self, **kwargs):
		context = super(ReporterUpdate, self).get_context_data(**kwargs)
		context['title'] = 'Update Reporter'
		notifications = models.Coord_Reporter_Request.objects.filter(respond_status='NVR');
		notifications_count = len(notifications)
		context['notifications'] = notifications
		context['notifications_count'] = notifications_count
		return context

class ReporterDelete(DeleteView):
	model = models.Coord_Reporter
	success_url = reverse_lazy('App_Admin:reporter_list')
	template_name = 'confirm_delete.html'
	
	def get_context_data(self, **kwargs):
		context = super(ReporterDelete, self).get_context_data(**kwargs)
		context['title'] = 'Delete Reporter'
		notifications = models.Coord_Reporter_Request.objects.filter(respond_status='NVR');
		notifications_count = len(notifications)
		context['notifications'] = notifications
		context['notifications_count'] = notifications_count
		return context

class UserList(ListView):
	model = models.User
	template_name = 'list_tables.html'
	

	def get_context_data(self, **kwargs):
		context = super(UserList, self).get_context_data(**kwargs)
		context['title'] = 'Users'
		notifications = models.Coord_Reporter_Request.objects.filter(respond_status='NVR');
		notifications_count = len(notifications)
		context['notifications'] = notifications
		context['notifications_count'] = notifications_count
		return context

class UserCreate(CreateView):
	model = models.User
	form_class = forms.User_Form
	template_name = 'create_form.html'
	
	success_url = reverse_lazy('App_Admin:user_list')
	def get_context_data(self, **kwargs):
		context = super(UserCreate, self).get_context_data(**kwargs)
		context['title'] = 'Add User'
		notifications = models.Coord_Reporter_Request.objects.filter(respond_status='NVR');
		notifications_count = len(notifications)
		context['notifications'] = notifications
		context['notifications_count'] = notifications_count
		return context

class UserUpdate(UpdateView):
	model = models.User
	form_class = forms.User_Form
	template_name = 'update_form.html'
	
	success_url = reverse_lazy('App_Admin:user_list')

	def get_context_data(self, **kwargs):
		context = super(UserUpdate, self).get_context_data(**kwargs)
		context['title'] = 'Update User'
		notifications = models.Coord_Reporter_Request.objects.filter(respond_status='NVR');
		notifications_count = len(notifications)
		context['notifications'] = notifications
		context['notifications_count'] = notifications_count
		return context

class UserDelete(DeleteView):
	model = models.User
	success_url = reverse_lazy('App_Admin:user_list')
	template_name = 'confirm_delete.html'
	
	def get_context_data(self, **kwargs):
		context = super(UserDelete, self).get_context_data(**kwargs)
		context['title'] = 'Delete User'
		notifications = models.Coord_Reporter_Request.objects.filter(respond_status='NVR');
		notifications_count = len(notifications)
		context['notifications'] = notifications
		context['notifications_count'] = notifications_count
		return context


# def add_user(request):
# 	title = 'Add User'
# 	form = forms.User_Form(request.POST or None)
# 	if form.is_valid():
# 		user_name = form.cleaned_data['username']
# 		models.User.objects.get_or_create(username = user_name)
# 		return HttpResponseRedirect("/app_admin/")

# 	context = {'form' : form, 'title' : title}
# 	template = "add.html"
# 	return render(request, template, context)

class RouteList(ListView):
	model = models.Route
	template_name = 'list_tables.html'
	
	def get_context_data(self, **kwargs):
		context = super(RouteList, self).get_context_data(**kwargs)
		context['title'] = 'Routes'
		notifications = models.Coord_Reporter_Request.objects.filter(respond_status='NVR');
		notifications_count = len(notifications)
		context['notifications'] = notifications
		context['notifications_count'] = notifications_count
		return context

class RouteCreate(CreateView):
	model = models.Route
	form_class = forms.Route_Form
	template_name = 'create_form.html'
	
	success_url = reverse_lazy('App_Admin:route_list')
	def get_context_data(self, **kwargs):
		context = super(RouteCreate, self).get_context_data(**kwargs)
		context['title'] = 'Add Route'
		notifications = models.Coord_Reporter_Request.objects.filter(respond_status='NVR');
		notifications_count = len(notifications)
		context['notifications'] = notifications
		context['notifications_count'] = notifications_count
		return context

class RouteUpdate(UpdateView):
	model = models.Route
	form_class = forms.Route_Form
	template_name = 'update_form.html'
	
	success_url = reverse_lazy('App_Admin:route_list')
	def get_context_data(self, **kwargs):
		context = super(RouteUpdate, self).get_context_data(**kwargs)
		context['title'] = 'Update Route'
		notifications = models.Coord_Reporter_Request.objects.filter(respond_status='NVR');
		notifications_count = len(notifications)
		context['notifications'] = notifications
		context['notifications_count'] = notifications_count
		return context

class RouteDelete(DeleteView):
	model = models.Route
	success_url = reverse_lazy('App_Admin:route_list')
	template_name = 'confirm_delete.html'
	
	def get_context_data(self, **kwargs):
		context = super(RouteDelete, self).get_context_data(**kwargs)
		context['title'] = 'Delete Route'
		notifications = models.Coord_Reporter_Request.objects.filter(respond_status='NVR');
		notifications_count = len(notifications)
		context['notifications'] = notifications
		context['notifications_count'] = notifications_count
		return context

# def add_route(request):
# 	title = 'Add Route'
# 	form = forms.Route_Form(request.POST or None)
# 	if form.is_valid():
# 		route_name = form.cleaned_data['route_name']
# 		obj, created = models.Route.objects.get_or_create(route_name = route_name)

# 		if not created:
# 			raise django_forms.ValidationError("This route already exist in database.")

# 		return HttpResponseRedirect("/app_admin/")

# 	context = {'form': form, 'title' : title}
# 	template  = "add.html"
# 	return render(request, template, context)

class StopList(ListView):
	model = models.Stop
	template_name = 'list_tables.html'
	
	def get_context_data(self, **kwargs):
		context = super(StopList, self).get_context_data(**kwargs)
		context['title'] = 'Stops'
		notifications = models.Coord_Reporter_Request.objects.filter(respond_status='NVR');
		notifications_count = len(notifications)
		context['notifications'] = notifications
		context['notifications_count'] = notifications_count
		return context

class StopCreate(CreateView):
	model = models.Stop
	form_class = forms.Stop_Form
	template_name = 'create_form.html'
	
	success_url = reverse_lazy('App_Admin:stop_list')
	def get_context_data(self, **kwargs):
		context = super(StopCreate, self).get_context_data(**kwargs)
		context['title'] = 'Add Stop'
		notifications = models.Coord_Reporter_Request.objects.filter(respond_status='NVR');
		notifications_count = len(notifications)
		context['notifications'] = notifications
		context['notifications_count'] = notifications_count
		return context

class StopUpdate(UpdateView):
	model = models.Stop
	form_class = forms.Stop_Form
	template_name = 'update_form.html'
	
	success_url = reverse_lazy('App_Admin:stop_list')
	def get_context_data(self, **kwargs):
		context = super(StopUpdate, self).get_context_data(**kwargs)
		context['title'] = 'Update Stop'
		notifications = models.Coord_Reporter_Request.objects.filter(respond_status='NVR');
		notifications_count = len(notifications)
		context['notifications'] = notifications
		context['notifications_count'] = notifications_count
		return context

class StopDelete(DeleteView):
	model = models.Stop
	success_url = reverse_lazy('App_Admin:stop_list')
	template_name = 'confirm_delete.html'
	
	def get_context_data(self, **kwargs):
		context = super(StopDelete, self).get_context_data(**kwargs)
		context['title'] = 'Delete Stop'
		notifications = models.Coord_Reporter_Request.objects.filter(respond_status='NVR');
		notifications_count = len(notifications)
		context['notifications'] = notifications
		context['notifications_count'] = notifications_count
		return context

# def add_stop(request):
# 	form = forms.Stop_Form(request.POST or None)
# 	title = "Add Stop"
# 	if form.is_valid():
# 		stop_name = form.cleaned_data['stop_name']
# 		route = form.cleaned_data['route']
# 		models.Stop.objects.get_or_create(stop_name = stop_name, route = route)
# 		return HttpResponseRedirect("/app_admin/")

# 	context = {'form': form, 'title' : title}
# 	template  = "add.html"
# 	return render(request, template, context)

class BusList(ListView):
	model = models.Bus
	template_name = 'list_tables.html'
	
	def get_context_data(self, **kwargs):
		context = super(BusList, self).get_context_data(**kwargs)
		context['title'] = 'Buses'
		notifications = models.Coord_Reporter_Request.objects.filter(respond_status='NVR');
		notifications_count = len(notifications)
		context['notifications'] = notifications
		context['notifications_count'] = notifications_count
		return context

class BusCreate(CreateView):
	model = models.Bus
	form_class = forms.Bus_Form
	template_name = 'create_form.html'
	
	success_url = reverse_lazy('App_Admin:bus_list')
	def get_context_data(self, **kwargs):
		context = super(BusCreate, self).get_context_data(**kwargs)
		context['title'] = 'Add Bus'
		notifications = models.Coord_Reporter_Request.objects.filter(respond_status='NVR');
		notifications_count = len(notifications)
		context['notifications'] = notifications
		context['notifications_count'] = notifications_count
		return context

class BusUpdate(UpdateView):
	model = models.User
	form_class = forms.Bus_Form
	template_name = 'update_form.html'
	
	success_url = reverse_lazy('App_Admin:bus_list')
	def get_context_data(self, **kwargs):
		context = super(BusUpdate, self).get_context_data(**kwargs)
		context['title'] = 'Update Bus'
		notifications = models.Coord_Reporter_Request.objects.filter(respond_status='NVR');
		notifications_count = len(notifications)
		context['notifications'] = notifications
		context['notifications_count'] = notifications_count
		return context

class BusDelete(DeleteView):
	model = models.Bus
	success_url = reverse_lazy('App_Admin:bus_list')
	template_name = 'confirm_delete.html'
	
	def get_context_data(self, **kwargs):
		context = super(BusDelete, self).get_context_data(**kwargs)
		context['title'] = 'Delete Bus'
		notifications = models.Coord_Reporter_Request.objects.filter(respond_status='NVR');
		notifications_count = len(notifications)
		context['notifications'] = notifications
		context['notifications_count'] = notifications_count
		return context

# def add_bus(request):
# 	form = forms.Bus_Form(request.POST or None)
# 	title = "Add Bus"
# 	if form.is_valid():
# 		bus_name = form.cleaned_data['bus_name']
# 		route = form.cleaned_data['route']
# 		stops = form.getfield['stops']
# 		status = form.cleaned_data['status']

# 		models.Bus.objects.get_or_create(bus_name = bus_name, route=route, stops=stops, status=status)
# 		return HttpResponseRedirect("/app_admin/")

# 	context = {'form': form, 'title' : title}
# 	template  = "add.html"
# 	return render(request, template, context)

class CoordRequestList(ListView):
	model = models.Coord_Reporter_Request
	# queryset = models.Coord_Reporter_Request.objects.all()
	template_name = 'list_tables.html'
	form_class = forms.Coord_Reporter_Request_Form

	def get_context_data(self, **kwargs):
		context = super(CoordRequestList, self).get_context_data(**kwargs)
		context['title'] = 'Requests for reporting Bus Coordinates'
		notifications = models.Coord_Reporter_Request.objects.filter(respond_status='NVR');
		notifications_count = len(notifications)
		context['notifications'] = notifications
		context['notifications_count'] = notifications_count
		return context

class CoordRequestCreate(CreateView):
	model = models.Coord_Reporter_Request
	form_class = forms.Coord_Reporter_Request_Form
	template_name = 'create_form.html'
	
	success_url = reverse_lazy('App_Admin:request_list')
	def get_context_data(self, **kwargs):
		context = super(CoordRequestCreate, self).get_context_data(**kwargs)
		context['title'] = 'Add Request'
		notifications = models.Coord_Reporter_Request.objects.filter(respond_status='NVR');
		notifications_count = len(notifications)
		context['notifications'] = notifications
		context['notifications_count'] = notifications_count
		return context

class CoordRequestUpdate(UpdateView):
	model = models.Coord_Reporter_Request
	form_class = forms.Coord_Reporter_Request_Form
	template_name = 'update_form.html'
	
	success_url = reverse_lazy('App_Admin:request_list')
	def get_context_data(self, **kwargs):
		context = super(CoordRequestUpdate, self).get_context_data(**kwargs)
		context['title'] = 'Request Update'
		notifications = models.Coord_Reporter_Request.objects.filter(respond_status='NVR');
		notifications_count = len(notifications)
		context['notifications'] = notifications
		context['notifications_count'] = notifications_count
		return context

class CoordRequestDelete(DeleteView):
	model = models.Coord_Reporter_Request
	success_url = reverse_lazy('App_Admin:request_list')
	template_name = 'confirm_delete.html'
	
	def get_context_data(self, **kwargs):
		context = super(CoordRequestDelete, self).get_context_data(**kwargs)
		context['title'] = 'Delete Request'
		notifications = models.Coord_Reporter_Request.objects.filter(respond_status='NVR');
		notifications_count = len(notifications)
		context['notifications'] = notifications
		context['notifications_count'] = notifications_count
		return context

# def add_coordrequest(request):
# 	form = forms.Coord_Reporter_Request_Form(request.POST or None)
# 	title = "Request for reporting Bus Coordinates"
# 	if form.is_valid():
# 		route_name = form.cleaned_data['route_name']
# 		models.Coord_Reporter_Request.objects.get_or_create(route_name = route_name)
# 		return HttpResponseRedirect("/app_admin/")

# 	context = {'form': form, 'title' : title}
# 	template  = "add.html"
# 	return render(request, template, context)

def dashboard(request):
	app = apps.get_app_config('App_Admin')
	app_models = []
	app_models = app.models.values();
	notifications = models.Coord_Reporter_Request.objects.filter(respond_status='NVR');
	notifications_count = len(notifications)

	app_models_verbose = []
	for i in app_models:
		i_verbose_name = i._meta.verbose_name
		if i_verbose_name != 'bus-stop relationship':
			app_models_verbose.append(i_verbose_name)
			# if(i_verbose_name == 'Routes'):


	title = "Dashboard"
	context = {'title': title, 'app_models' : app_models_verbose, 'notifications' : notifications, 'notifications_count': notifications_count}
	
	template = "dashboard.html"

	return render(request, template, context)