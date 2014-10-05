from django.db import models
from django.contrib.auth.models import User

# Create your models here.

class Player(models.Model):
	user = models.ForeignKey(User)
	username = models.CharField(max_length=50,unique=True)
	school = models.CharField(max_length=50)
	permalink = models.CharField(max_length=200)
	first_name = models.CharField(max_length=50)
	last_name = models.CharField(max_length=50)

	def __unicode__(self):
		return self.username