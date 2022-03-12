from django.db import models


class Cloth(models.Model):
    name = models.CharField(max_length=20)
    price = models.PositiveIntegerField()
    
    class Meta:
        db_table = 'clothes'
