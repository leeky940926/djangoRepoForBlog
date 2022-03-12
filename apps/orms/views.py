import imp
import json
from django.views import View
from django.http import JsonResponse
from django.db.models import F
from orms.models import Posting


class RaceConditionView(View):
    def put(self, request, *args, **kwargs):
        try:
            posting = Posting.objects.get(id=kwargs["posting_id"])
            posting.view = posting.view + 1
            posting.save()
        
        except Posting.DoesNotExist:
            return JsonResponse({'message':'POSTING_DOES_NOT_EXIST'}, status=400)
            
        else:
            return JsonResponse({'message':'update success'}, status=201)


class NonRaceConditionView(View):
    def put(self, request, *args, **kwargs):
        try:
            posting = Posting.objects.get(id=kwargs["posting_id"])
            posting.view = F('view') + 1
            posting.save()
        
        except Posting.DoesNotExist:
            return JsonResponse({'message':'POSTING_DOES_NOT_EXIST'}, status=400)
            
        else:
            return JsonResponse({'message':'update success'}, status=201)
