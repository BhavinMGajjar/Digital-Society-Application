from django.db import models
from django.utils import timezone


# Create your models here.

class User(models.Model):
	fname=models.CharField(max_length=100)
	lname=models.CharField(max_length=100)
	email=models.EmailField()
	mobile=models.BigIntegerField()
	password=models.CharField(max_length=100)
	profile_picture=models.ImageField(default="", upload_to="profile_picture")
	usertype=models.CharField(max_length=100, default="member")

def __str__(self):
		return self.fname+" "+self.lname

class Watchmen(models.Model):
	fname=models.CharField(max_length=100)
	lname=models.CharField(max_length=100)
	address=models.CharField(max_length=100)
	mobile=models.BigIntegerField()

class Events(models.Model):
	title=models.CharField(max_length=100)
	desc=models.CharField(max_length=100)
	date=models.DateTimeField(default=timezone.now)


