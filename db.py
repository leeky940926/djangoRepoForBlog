import os
import django
from django.db import transaction
from apps.orms.models import Cloth

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'blogs.settings')
django.setup()

with transaction.atomic():
   Cloth.objects.create(name="갈색 가디건", price=50000)