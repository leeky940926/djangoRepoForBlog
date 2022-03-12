import imp
import json
from django.views import View
from django.http import JsonResponse
from django.db.models import F


class RaceConditionView(View):
    def put(self, request, *args, **kwargs):
        return 1
        # try:
        #     cloth = Cloth.objects.get(id=kwargs["cloth_id"])
        
        #     data = json.loads(self.request.body)
        #     name = data.get("name", None)
        #     price = data.get("price", None)
            
        #     if name:
        #         cloth.name = name
            
        #     cloth.price = F('price')                
            
        #     cloth.save()
        
        # except model.DoesNotExist:
        #     return JsonResponse({'message':'CLOTH_DOES_NOT_EXIST'}, status=400)
            
        # else:
        #     return JsonResponse({'message':'update success'}, status=201)


class NonRaceConditionView(View):
    def put(self, request, *args, **kwargs):
        return JsonResponse({'message':'update success'}, status=201)
