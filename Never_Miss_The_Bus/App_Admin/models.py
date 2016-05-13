from django.db import models
from django.contrib.auth.models import User as Auth_User
from django.core.urlresolvers import reverse

# Create your models here.

class Stop(models.Model):
	stop_id = models.AutoField(
		primary_key=True, 
		editable=False,
		verbose_name='Stop ID'
	)

	stop_name = models.CharField(
		"Stop Name", 
		max_length=50,
		blank=False,
		unique=True,
	)

	latitude = models.CharField(
		"Latitude",
		max_length=10,
		blank=False,
	)

	longitude = models.CharField(
		"Longitude",
		max_length=10,
		blank=False,
	)

	def __str__(self):
		return self.stop_name

	def get_absolute_url_for_update(self):
		return reverse('App_Admin:stop_update', args=[str(self.stop_id)] )

	def get_absolute_url_for_delete(self):
		return reverse('App_Admin:stop_delete', args=[str(self.stop_id)] )

	def get_fileds(self):
		return [field.verbose_name for field in self._meta.fields]

	def get_field_values(self):
		return [(field.value_to_string(self)) for field in self._meta.fields]

	class Meta:
		verbose_name = "Stops"

class Route(models.Model):
	route_id = models.AutoField(
		primary_key=True, 
		editable=False,
		verbose_name='Route ID'
	)
	route_name = models.CharField(
		"Route Name", 
		max_length=50,
		blank=False,
		unique=True,
	)

	origin = models.ForeignKey(
		Stop,
		blank=False,
		related_name="%(app_label)s_origin_stop_related",
		verbose_name='Origin Stop',
	)

	stops = models.ManyToManyField(
		Stop,
		blank=False,
		verbose_name='Stops')

	def __str__(self):
		return self.route_name

	def get_absolute_url_for_update(self):
		return reverse('App_Admin:route_update', args=[str(self.route_id)] ) #"/app_admin/route/%i/" % self.id

	def get_absolute_url_for_delete(self):
		return reverse('App_Admin:route_delete', args=[str(self.route_id)] )

	def get_fileds(self):
		return [field.verbose_name for field in self._meta.fields]

	def get_field_values(self):
		return [(field.value_to_string(self)) for field in self._meta.fields]

	class Meta:
		verbose_name = "Routes"

class Bus(models.Model):
	bus_id = models.AutoField(
		verbose_name='ID',
		primary_key=True, 
		editable=False
	)
	bus_name = models.CharField(
		"Bus Name",
		unique=True,
		max_length=30,
		blank=False
	)
	route = models.ForeignKey(
		Route, 
		on_delete=models.CASCADE,
		verbose_name='Route',
		blank=False
	)

	statuses = (
		('REG', 'Registered'),
		('OPN', 'Open/Not Registered'),
	)
	status = models.CharField(
		'Status',
		choices=statuses, 
		max_length=3, 
		default='OPN',
		blank=False,
	)

	def set_status(self, status = 'OPN'):
		self.status = status

	def get_fileds(self):
		return [field.verbose_name for field in self._meta.fields]

	def get_field_values(self):
		return [(field.value_to_string(self)) for field in self._meta.fields]

	def __str__(self):
		return self.bus_name

	def get_absolute_url_for_update(self):
		return reverse('App_Admin:bus_update', args=[str(self.bus_id)] )

	def get_absolute_url_for_delete(self):
		return reverse('App_Admin:bus_delete', args=[str(self.bus_id)] )

	class Meta:
		verbose_name = "Buses"


# class User(Auth_User):

# 	def get_absolute_url_for_update(self):
# 		return reverse('App_Admin:user_update', args=[str(self.id)] )

# 	def get_absolute_url_for_delete(self):
# 		return reverse('App_Admin:user_delete', args=[str(self.id)] )

# 	def get_fileds(self):
# 		gen = [field for field in self._meta.fields]
# 		for genfield in gen:
# 			if genfield.name not in ('last_modified', 'date_joined', 'last_login', 'is_superuser', 'password', 'staff_status','active','user_ptr'):
# 				yield genfield.verbose_name

# 	def get_field_values(self):
# 		gen = [field for field in self._meta.fields]
# 		for genfield in gen:
# 			if genfield.name not in ('last_modified', 'date_joined', 'last_login', 'is_superuser', 'password', 'staff_status','active','user_ptr'):
# 				yield genfield.value_to_string(self)

# 	def __str__(self):
# 		return self.username

# 	class Meta:
# 		verbose_name = "Users"


class Coord_Reporter_Request(models.Model):
	request_id = models.AutoField(
		primary_key=True, 
		editable=False
	)

	user = models.OneToOneField(
		Auth_User,
		on_delete = models.CASCADE,
		blank=False,
		verbose_name='Requested by',
		)

	requestedfor_bus_number = models.ForeignKey(
		Bus, 
		on_delete=models.CASCADE,
		blank=False,
		verbose_name='Requesting for bus'
	)

	request_created_date_time = models.DateTimeField(
		auto_now_add=True,
		verbose_name='Request created on'
	)

	respond_date_time = models.DateTimeField( 
		null=True
	)

	statuses = (
		('NVR', 'Not Verified'),
		('DND', 'Denied'),
	)

	respond_status = models.CharField(
		max_length=3, 
		choices= statuses,
		default='NVR',

	)

	def get_absolute_url_for_accept(self):
		return reverse('App_Admin:accept_request')

	def get_absolute_url_for_deny(self):
		return reverse('App_Admin:deny_request')

	def get_absolute_url_for_update(self):
		return reverse('App_Admin:request_update', args=[str(self.request_id)] )

	def get_absolute_url_for_delete(self):
		return reverse('App_Admin:request_delete', args=[str(self.request_id)] )

	def get_fileds(self):
		return [field.verbose_name for field in self._meta.fields]

	def get_field_values(self):
		return [field.value_to_string(self) for field in self._meta.fields]

	class Meta:
		verbose_name = "Coordinates Reporting Requests"


class Coord_Reporter(models.Model):
	reporter_id = models.AutoField(
		primary_key=True, 
		editable=False
	)

	user = models.OneToOneField(
		Auth_User,
		on_delete = models.CASCADE,
		blank=False,
		verbose_name='Reporter',
	)

	allocated_bus = models.ForeignKey(
		Bus,
	)

	acceptance_date = models.DateTimeField(
		auto_now_add=True,
	)

	accepted_by = models.ForeignKey(
		Auth_User,
		related_name = 'accepted_by',
		on_delete = models.CASCADE,
	)

	def get_absolute_url_for_update(self):
		return reverse('App_Admin:reporter_update', args=[str(self.reporter_id)] )

	def get_absolute_url_for_delete(self):
		return reverse('App_Admin:reporter_delete', args=[str(self.reporter_id)] )

	def get_fileds(self):
		return [field.verbose_name for field in self._meta.fields]

	def get_field_values(self):
		return [(field.value_to_string(self)) for field in self._meta.fields]

	def __str__(self):
		return str(self.user.username)	

	class Meta:
		verbose_name = "Coordinates Reporters"