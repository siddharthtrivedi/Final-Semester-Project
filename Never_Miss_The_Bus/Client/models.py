from django.db import models
from App_Admin.models import User

# Create your models here.
class Client(User):
	user = models.OneToOneField(User)