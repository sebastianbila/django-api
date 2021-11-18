from django.contrib.auth.models import User
from django.db import models


class Post(models.Model):
    title = models.CharField(max_length=100, blank=True, default='')
    created = models.DateTimeField(auto_now_add=True)
    content = models.TextField(blank=True, default='')

    class Meta:
        ordering = ('id', )
