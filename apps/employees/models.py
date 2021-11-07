from django.db import models

GENDERS = [
    ('neither', 'Neither'),
    ('male', 'Male'),
    ('female', 'Female'),
]


class Employee(models.Model):
    first_name = models.CharField(max_length=100, blank=False)
    last_name = models.CharField(max_length=100, blank=False)
    gender = models.CharField(choices=GENDERS, max_length=7, default='neither')
    email = models.EmailField(blank=True, default='')
    phone = models.CharField(max_length=60, blank=True, default='')
    github_link = models.URLField(blank=True, default='')
    joining_date = models.DateTimeField(auto_now_add=True)
