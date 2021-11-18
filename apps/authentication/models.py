from django.contrib.auth.models import AbstractUser
from django.db import models


class User(AbstractUser):
   gender = models.BooleanField(default=True) # True for male and False for female
   # you can add more fields here.
