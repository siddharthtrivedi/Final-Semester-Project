from django import forms
from . import models
from django.utils.translation import ugettext_lazy as tolabel

class User_Form(forms.ModelForm):
	class Meta:
		model = models.User
		fields = ['first_name', 'last_name', 'username', 'password', 'email', 'cell_number']
		widgets = { 
            'username': forms.TextInput(attrs={'required': 'required'}),
            'first_name': forms.TextInput(attrs={'required': 'required'}),
            'last_name': forms.TextInput(attrs={'required': 'required'}),
            'password': forms.TextInput(attrs={'required': 'required', 'type' : 'password', 'pattern':'(?=.*\d)(?=.*[a-z])(?=.*[A-Z]).{8,}', 'title':'Must contain at least one number and one uppercase and lowercase letter, and at least 8 or more characters'}),
            'email' : forms.TextInput(attrs={'required': 'required', 'type': 'email', 'pattern':'[a-z0-9._%+-]+@[a-z0-9.-]+\.[a-z]{2,3}$', 'title': 'Invalid email address.'}), 
            'cell_number': forms.TextInput(attrs={'required': 'required', 'pattern':'(7|8|9)\d{9}', 'title':'Cell number must start with 7 or 8 or 9 and then followed by 9 digits.'}),
        }   
		# error_message={
		# 'first_name': {
		# 		'required': _("Please let us know what to call you!"),
		# 	},
		# }

class Route_Form(forms.ModelForm):
	class Meta:
		model = models.Route
		fields = ['route_name']

class Stop_Form(forms.ModelForm):
	class Meta:
		model = models.Stop
		fields = ['stop_name', 'route']

class Bus_Form(forms.ModelForm):
	class Meta:
		model = models.Bus
		fields = ['bus_name', 'route', 'status', 'stops']

class Coord_Reporter_Request_Form(forms.ModelForm):
	class Meta:
		model = models.Coord_Reporter_Request
		fields = ['requestedfor_bus_number', 'user']
		labels={
			'requestedfor_bus_number' : tolabel('Requesting for bus'),
		}

class Reporter_Form(forms.ModelForm):
	class Meta:
		model = models.Coord_Reporter
		# readonly_fields = ['reporter_id', 'allocated_bus', 'acceptance_date', 'verifier']
		# fields = []
		fields = ['allocated_bus', 'verifier']
		# for i in model._meta.fields:
		# 	print(fields.append(str(i)))