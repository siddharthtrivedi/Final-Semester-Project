from django import forms
from django.contrib.auth.forms import UserCreationForm
from . import models
from django.contrib.auth.models import User as Auth_User
from django.utils.translation import ugettext_lazy as tolabel

class User_Form(UserCreationForm):
	class Meta:
		model = Auth_User
		fields = ['first_name', 'last_name', 'username','email']
		widgets = { 
            'username': forms.TextInput(attrs={'required': 'required'}),
            'first_name': forms.TextInput(attrs={'required': 'required'}),
            'last_name': forms.TextInput(attrs={'required': 'required'}),
            'password1': forms.TextInput(attrs={'required': 'required', 'type' : 'password', 'id' : 'password', 'pattern':'(?=.*\d)(?=.*[a-z])(?=.*[A-Z]).{8,}', 'title':'Must contain at least one number and one uppercase and lowercase letter, and at least 8 or more characters'}),
            'password2': forms.TextInput(attrs={'required': 'required', 'type' : 'password', 'id' : 'confirm_password'}),
            'email' : forms.TextInput(attrs={'required': 'required', 'type': 'email', 'pattern':'[a-z0-9._%+-]+@[a-z0-9.-]+\.[a-z]{2,3}$', 'title': 'Invalid email address.'}), 
        }   
		# error_message={
		# 'first_name': {
		# 		'required': _("Please let us know what to call you!"),
		# 	},
		# }

class Route_Form(forms.ModelForm):
	class Meta:
		model = models.Route
		fields = ['route_name','origin' ,'stops']

class Stop_Form(forms.ModelForm):
	class Meta:
		model = models.Stop
		fields = ['stop_name', 'latitude', 'longitude']

class Bus_Form(forms.ModelForm):
	class Meta:
		model = models.Bus
		fields = ['bus_name', 'route']

class Coord_Reporter_Request_Form(forms.ModelForm):
	class Meta:
		model = models.Coord_Reporter_Request
		fields = ['requestedfor_bus_number', 'user']
		labels={
			'requestedfor_bus_number' : tolabel('Requesting for bus'),
		}

	def __init__(self, *args, **kwargs):
		super(Coord_Reporter_Request_Form, self).__init__(*args, **kwargs)
		if self.instance:
			self.fields["requestedfor_bus_number"].queryset = models.Bus.objects.filter(status='OPN')
			all_users = Auth_User.objects.all()
			current_reporters = models.Coord_Reporter.objects.all()
			current_requests = models.Coord_Reporter_Request.objects.all()
			reporter_excluded_qs = all_users.exclude(id__in = current_reporters.values_list('user'))
			self.fields["user"].queryset = reporter_excluded_qs.exclude(id__in = current_requests.values_list('user'))


class Reporter_Form(forms.ModelForm):
	class Meta:
		model = models.Coord_Reporter
		# readonly_fields = ['reporter_id', 'allocated_bus', 'acceptance_date', 'verifier']
		# fields = []
		fields = ['allocated_bus', 'user', 'accepted_by']
		# for i in model._meta.fields:
		# 	print(fields.append(str(i)))