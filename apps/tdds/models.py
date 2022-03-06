from django.db import models


class Role(models.Model):
    name = models.CharField(max_length=20)


class User(models.Model):
    role = models.ForeignKey('tdds.Role', on_delete=models.CASCADE)
    nickname = models.CharField(max_length=20, unique=True)
    password = models.CharField(max_length=500)