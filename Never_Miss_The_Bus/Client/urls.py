from django.conf.urls import url
from Client import views

urlpatterns = [
	url(r'^$', views.client_home, name='client_home'),
]