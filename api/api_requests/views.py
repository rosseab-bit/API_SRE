from django.shortcuts import render
from django.core import serializers
from django.http import HttpResponse
import json
from django.http import JsonResponse
import requests
from django.views.decorators.csrf import csrf_exempt
from .models import DataFly
# Create your views here.

def getData(requests):
    if requests.method == "GET":
        data = {'a':1, 'b':2, 'c':3}
        dataSqlite = DataFly.objects.all().values()
        dataJson = {'data': list(dataSqlite)}
        print(dataJson)
        return JsonResponse(dataJson)

@csrf_exempt
def putData(requests):
    # nombre de los campos de la tabla.
    column_names = [
            "fecha_i",
            "vlo_i",
            "ori_i",
            "des_i",
            "emp_i",
            "fecha_o",
            "vlo_o",
            "ori_o",
            "des_o",
            "emp_o",
            "day_month",
            "month_fly",
            "year_fly",
            "day_fly",
            "type_fly",
            "enterprice",
            "siglaori",
            "siglades",
    ]
    if requests.method == "POST":
        print(json.loads(requests.body)["data"])
        for item in json.loads(requests.body)["data"]:
            print(item)
            for name in item:
                print(name)
                if name not in column_names:
                    return JsonResponse({'response':'Error in format object, veried your data.'})
        return JsonResponse({'response':'Data load'})
