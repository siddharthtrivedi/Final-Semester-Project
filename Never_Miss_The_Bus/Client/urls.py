from django.contrib.auth.decorators import login_required
from django.conf.urls import url
from Client import views

urlpatterns = [
	url(r'^$', login_required(views.client_home), name='client_home'),
	url(r'^test/$', views.client_home1),
]