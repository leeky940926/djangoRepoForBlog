from django.db import models

from apps.utils.models import TimeStampedModel


class Role(models.Model):
    name = models.CharField(max_length=20)


class User(TimeStampedModel):
    role = models.ForeignKey('tdds.Role', on_delete=models.CASCADE)
    nickname = models.CharField(max_length=20, unique=True)
    password = models.CharField(max_length=500)