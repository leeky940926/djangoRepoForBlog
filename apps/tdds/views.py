import json
from django.views import View
from django.http import JsonResponse
from django.db import transaction
from tdds.models import Role, User

class RoleView(View):
    def post(self, request, *args, **kwargs):
        try:
            with transaction.atomic():
                data = json.loads(self.request.body)
                Role.objects.create(name=data["name"])
        
        except KeyError:
            return JsonResponse({'meesage':'KEY_ERROR'}, status=500)
        
        else:    
            return JsonResponse({'message' : 'CREATE_ROLE'}, status=201)