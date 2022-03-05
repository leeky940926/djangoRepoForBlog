from django.views import View
from django.http import JsonResponse

from indexes.models import Customer

class IndexFirstNameView(View):
    def get(self, request, *args, **kwargs):

        c = Customer.objects.filter(first_name__icontains="a")
        d = Customer.objects.filter(last_name__icontains="a")
        
        return JsonResponse({"count":d.count()}, status=200)