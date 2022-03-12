from django.views import View
from django.http import JsonResponse
from orms.models import Cloth

class RaceConditionView(View):
    def put(self, request, *args, **kwargs):
        return JsonResponse({'message':'update success'}, status=201)


class NonRaceConditionView(View):
    def put(self, request, *args, **kwargs):
        return JsonResponse({'message':'update success'}, status=201)
