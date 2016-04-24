from django.conf.urls import url
from . import views

app_name = 'App_Admin'

urlpatterns = [
	url(r'^user/$',views.UserList.as_view(template_name="model_list.html"), name = "user_list"),
	url(r'^route/$',views.RouteList.as_view(template_name="model_list.html"), name = "route_list"),
	url(r'^stop/$',views.StopList.as_view(template_name="model_list.html"), name = "stop_list"),
	url(r'^bus/$',views.BusList.as_view(template_name="model_list.html"), name = "bus_list"),
	url(r'^reporter/$',views.ReporterList.as_view(template_name="model_list.html"), name = "reporter_list"),
	url(r'^request/$',views.CoordRequestList.as_view(template_name="model_list.html"), name = "request_list"),

	# url(r'^bus/(?P<pk>[0-9]+)/$',views.BusUpdate.as_view(), name = "update-bus"),

	url(r'^user/add/$',views.add_user, name = "Add Users"),
	url(r'^route/add/$',views.add_route, name = "Add Route"),
	url(r'^stop/add/$',views.add_stop, name = "Add Stop"),
	url(r'^bus/add/$',views.add_bus, name = "Add Bus"),
	url(r'^request/add/$',views.add_coordrequest, name = "Add Request"),

	url(r'^user/update/(?P<pk>[0-9]+)/$',views.UserUpdate.as_view(), name = "user_update"),
	url(r'^route/update/(?P<pk>[0-9]+)/$',views.RouteUpdate.as_view(), name = "route_update"),
	url(r'^stop/update/(?P<pk>[0-9]+)/$',views.StopUpdate.as_view(), name = "stop_update"),
	url(r'^bus/update/(?P<pk>[0-9]+)/$',views.BusUpdate.as_view(), name = "bus_update"),
	url(r'^request/update/(?P<pk>[0-9]+)/$',views.CoordRequestUpdate.as_view(), name = "request_update"),

	url(r'^$',views.dashboard, name = "Dashboard"),
]