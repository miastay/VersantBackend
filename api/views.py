from django.shortcuts import render
from django.http import JsonResponse

# Create your views here.
from django.utils.decorators import method_decorator
from django.views.decorators.csrf import csrf_exempt

import json

@csrf_exempt
def hello(request):
    return JsonResponse({'message': 'Hello from Django!'})

from api.gsch import search as gs

@csrf_exempt
def author(request):
    if request.method == "POST":
        jsonData = json.loads(request.body)
        query = jsonData.get("query")
        print(query)
        resp = gs.search_author(query)
        #print(resp)
        return JsonResponse(resp)


    