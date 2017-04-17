from __future__ import unicode_literals
from django.db import models
from django.utils import timezone
from django.contrib.auth.models import User


class UserProfile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    preferred_pass = models.CharField(max_length=50)
    external_id = models.IntegerField(unique=True)

    def __str__(self):
        return self.user.username
