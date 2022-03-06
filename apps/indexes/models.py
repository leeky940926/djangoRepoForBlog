from django.db import models

class Customer(models.Model):
    first_name = models.CharField(max_length=20)
    last_name = models.CharField(max_length=20)
    
    class Meta:
        indexes = [
            models.Index(fields=['first_name'], name='first_name_idx'),
        ]