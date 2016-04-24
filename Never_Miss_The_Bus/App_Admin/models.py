from django.db import models
from django.core.validators import RegexValidator
from django.core.urlresolvers import reverse

# Create your models here.
class Route(models.Model):
	route_id = models.AutoField(
		primary_key=True, 
		editable=False,
		verbose_name='Route ID'
	)
	route_name = models.CharField(
		"Route Name", 
		max_length=50,
		blank=False
	)

	def __str__(self):
		return self.route_name

	def get_absolute_url(self):
		return reverse('App_Admin:route_update', args=[str(self.route_id)] ) #"/app_admin/route/%i/" % self.id

	def get_fileds(self):
		return [field.verbose_name for field in self._meta.fields]

	def get_field_values(self):
		return [(field.value_to_string(self)) for field in self._meta.fields]

	class Meta:
		verbose_name = "Routes"

class Stop(models.Model):
	stop_id = models.AutoField(
		primary_key=True, 
		editable=False,
		verbose_name='Stop ID'
	)

	stop_name = models.CharField(
		"Stop Name", 
		max_length=50,
		blank=False
	)

	route = models.ForeignKey(
		Route, 
		on_delete=models.CASCADE,
		verbose_name='Route ID',
		blank=False
	)

	def __str__(self):
		return self.stop_name

	def get_absolute_url(self):
		return reverse('App_Admin:stop_update', args=[str(self.stop_id)] )

	def get_fileds(self):
		return [field.verbose_name for field in self._meta.fields]

	def get_field_values(self):
		return [(field.value_to_string(self)) for field in self._meta.fields]

	class Meta:
		verbose_name = "Stops"

class Bus(models.Model):
	bus_id = models.AutoField(
		verbose_name='ID',
		primary_key=True, 
		editable=False
	)
	bus_name = models.CharField(
		"Bus Name",
		max_length=30,
		blank=False
	)
	route = models.ForeignKey(
		Route, 
		on_delete=models.CASCADE,
		verbose_name='Route Number',
		blank=False
	)
	stops = models.ManyToManyField(Stop,
		blank=False)
	statuses = (
		('REG', 'Registered'),
		('OPN', 'Open/Not Registered'),
	)
	status = models.CharField(
		'Status',
		choices=statuses, 
		max_length=3, 
		default='OPN',
		blank=False
	)

	def get_fileds(self):
		return [field.verbose_name for field in self._meta.fields]

	def get_field_values(self):
		return [(field.value_to_string(self)) for field in self._meta.fields]

	def __str__(self):
		return self.bus_name

	def get_absolute_url(self):
		return reverse('App_Admin:bus_update', args=[str(self.bus_id)] )

	class Meta:
		verbose_name = "Buses"


class User(models.Model):
	user_id = models.AutoField(
		'ID',
		primary_key=True,
		editable=False,
	)
	username = models.CharField(
		'User Name',
		unique=True,
		max_length=30,
		blank=False,
		error_messages={'blank' : "Please let us know what to call you!"},
	)
	password = models.CharField(
		'Password',
		max_length=128,
		blank=False
	)
	is_superuser = models.BooleanField(
		editable=False,
		default=False
	)
	first_name = models.CharField(
		'First Name',
		max_length=30,
		blank=False
	)
	last_name = models.CharField(
		'Last Name',
		max_length=30,
		blank=False
	)
	email = models.EmailField(
		'Email',
		max_length=148,
		blank=False
	)
	date_joined = models.DateTimeField(
		auto_now_add = True
	)
	last_modified = models.DateTimeField(
		auto_now=True,
		auto_now_add=False,
		null=True,
		editable=False
	)

	cell_number_validator = RegexValidator(
		regex=r'^\+{1}\d{12}$', 
		message="Cell number must contain country code and then followed by 10 digits!"
	)

	cell_number = models.CharField(
		'Cell Number',
		# validators=[cell_number_validator], 
		blank=False, 
		max_length=13
	)
	last_login = models.DateTimeField(null=True, editable=False)

	def get_absolute_url(self):
		return reverse('App_Admin:user_update', args=[str(self.user_id)] )

	def get_fileds(self):
		gen = [field for field in self._meta.fields]
		for genfield in gen:
			if genfield.name not in ('last_modified', 'date_joined', 'last_login', 'is_superuser'):
				yield genfield.verbose_name

	def get_field_values(self):
		gen = [field for field in self._meta.fields]
		for genfield in gen:
			if genfield.name not in ('last_modified', 'date_joined', 'last_login', 'is_superuser'):
				yield genfield.value_to_string(self)

	class Meta:
		verbose_name = "Users"


class Coord_Reporter_Request(models.Model):
	request_id = models.AutoField(
		primary_key=True, 
		editable=False
	)

	user = models.ForeignKey(
		User,
		on_delete = models.CASCADE,
		blank=False
		)

	requestedfor_bus_number = models.ForeignKey(
		Bus, 
		on_delete=models.CASCADE,
		blank=False
	)

	request_created_date_time = models.DateTimeField(
		auto_now_add=True
	)

	respond_date_time = models.DateTimeField(
		auto_now=True, 
		auto_now_add=False, 
		null=True
	)

	statuses = (
		('NVR', 'Not Verified'),
		('DND', 'Denied'),
	)

	respond_status = models.CharField(
		max_length=3, 
		choices= statuses
	)

	def get_fileds(self):
		return [field.verbose_name for field in self._meta.fields]

	def get_field_values(self):
		return [(field.value_to_string(self)) for field in self._meta.fields]

	class Meta:
		verbose_name = "Coordinates Reporting Requests"

class Coord_Reporter(models.Model):
	reporter_id = models.AutoField(
		primary_key=True, 
		editable=False
	)

	allocated_bus = models.ForeignKey(
		Bus,
		editable=False
	)

	acceptance_date = models.DateTimeField(
		auto_now_add=True,
		editable=False
	)

	verifier = models.ForeignKey(
		User,
		editable=False
	)
	def get_fileds(self):
		return [field.verbose_name for field in self._meta.fields]

	def get_field_values(self):
		return [(field.value_to_string(self)) for field in self._meta.fields]

	class Meta:
		verbose_name = "Coordinates Reporters"