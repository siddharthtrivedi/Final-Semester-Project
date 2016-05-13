from django.contrib.admin.views.decorators import staff_member_required
from django.conf.urls import url
from . import views

# app_name = 'App_Admin'

urlpatterns = [
	# url(r'^user/$',staff_member_required(views.UserList.as_view(template_name="model_list.html")), name = "user_list"),
	url(r'^route/$',staff_member_required(views.RouteList.as_view(template_name="model_list.html")), name = "route_list"),
	url(r'^stop/$',staff_member_required(views.StopList.as_view(template_name="model_list.html")), name = "stop_list"),
	url(r'^bus/$',staff_member_required(views.BusList.as_view(template_name="model_list.html")), name = "bus_list"),
	url(r'^reporter/$',staff_member_required(views.ReporterList.as_view(template_name="model_list.html")), name = "reporter_list"),
	url(r'^request/$',staff_member_required(views.CoordRequestList.as_view(template_name="model_list.html")), name = "request_list"),
	# url(r'^bus/(?P<pk>[0-9]+)/$',staff_member_required(views.BusUpdate.as_view()), name = "update-bus"),

	# url(r'^user/add/$',staff_member_required(views.UserCreate.as_view()), name = "user_create"),
	url(r'^route/add/$',staff_member_required(views.RouteCreate.as_view()), name = "route_create"),
	url(r'^stop/add/$',staff_member_required(views.StopCreate.as_view()), name = "stop_create"),
	url(r'^bus/add/$',staff_member_required(views.BusCreate.as_view()), name = "bus_create"),
	url(r'^request/add/$',staff_member_required(views.CoordRequestCreate.as_view()), name = "request_create"),
	url(r'^reporter/add/$',staff_member_required(views.ReporterCreate.as_view()), name = "reporter_create"),

	# url(r'^user/update/(?P<pk>[0-9]+)/$',staff_member_required(views.UserUpdate.as_view()), name = "user_update"),
	url(r'^route/update/(?P<pk>[0-9]+)/$',staff_member_required(views.RouteUpdate.as_view()), name = "route_update"),
	url(r'^stop/update/(?P<pk>[0-9]+)/$',staff_member_required(views.StopUpdate.as_view()), name = "stop_update"),
	url(r'^bus/update/(?P<pk>[0-9]+)/$',staff_member_required(views.BusUpdate.as_view()), name = "bus_update"),
	url(r'^request/update/(?P<pk>[0-9]+)/$',staff_member_required(views.CoordRequestUpdate.as_view()), name = "request_update"),
	url(r'^reporter/update/(?P<pk>[0-9]+)/$',staff_member_required(views.ReporterUpdate.as_view()), name = "reporter_update"),


	# url(r'^user/delete/(?P<pk>[0-9]+)/$',staff_member_required(views.UserDelete.as_view()), name = "user_delete"),
	url(r'^route/delete/(?P<pk>[0-9]+)/$',staff_member_required(views.RouteDelete.as_view()), name = "route_delete"),
	url(r'^stop/delete/(?P<pk>[0-9]+)/$',staff_member_required(views.StopDelete.as_view()), name = "stop_delete"),
	url(r'^bus/delete/(?P<pk>[0-9]+)/$',staff_member_required(views.BusDelete.as_view()), name = "bus_delete"),
	url(r'^request/delete/(?P<pk>[0-9]+)/$',staff_member_required(views.CoordRequestDelete.as_view()), name = "request_delete"),
	url(r'^reporter/delete/(?P<pk>[0-9]+)/$',staff_member_required(views.ReporterDelete.as_view()), name = "reporter_delete"),

	url(r'^request/accept/$',staff_member_required(views.accept_request), name = "accept_request"),
	url(r'^request/deny/$',staff_member_required(views.deny_request), name = "deny_request"),
	

	url(r'^$',staff_member_required(views.dashboard), name = "Dashboard"),
]