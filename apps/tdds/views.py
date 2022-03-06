import json
import bcrypt
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


class SignUpView(View):
    def post(self, request, *args, **kwargs):
        try:
            with transaction.atomic():
                data = json.loads(self.request.body)
                
                role_id = data["role_id"]
                nickname = data["nickname"]
                password = data["password"]
                password = bcrypt.hashpw(password=password.encode('utf-8'), salt=bcrypt.gensalt())                
                
                if not Role.objects.filter(id=role_id).exists():
                    return JsonResponse({'message':'ROLE_DOES_NOT_EXIST'}, status=500)
                
                if User.objects.filter(nickname=nickname).exists():
                    return JsonResponse({'meesage':'NICKNAME_ALREADY_EXIST'}, status=500)
                
                User.objects.create(
                    role_id=role_id,
                    nickname=nickname,
                    password=password
                )
        
        except KeyError:
            return JsonResponse({'meesage':'KEY_ERROR'}, status=500)
        
        else:
            return JsonResponse({'message':'CREATE_ROLE'}, status=201)

