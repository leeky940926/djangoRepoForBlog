from django.db import models


class Posting(models.Model):
    title = models.CharField(max_length=20)
    text = models.TextField(max_length=500)
    view = models.PositiveIntegerField()
    
    class Meta:
        db_table = 'postings'
