import os
import django
from faker import Faker
from django.db import transaction

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'blogs.settings')
django.setup()

from indexes.models import Customer

f = Faker()

with transaction.atomic():
    customer_list = [Customer(first_name=f.name(), last_name=f.name) for _ in range(100000)]
    Customer.objects.bulk_create(customer_list)