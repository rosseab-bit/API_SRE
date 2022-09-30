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
        # controlo que los datos enviados cincidan con las columnas creadas en la base.
        # en caso de no coincidir retorno un mensaje para que puedan chequear los datos.
        for item in json.loads(requests.body)["data"]:
            print(item)
            for name in item:
                print(name)
                if name not in column_names:
                    return JsonResponse({'response': 'Error in format, verify your data.'})
        for item in json.loads(requests.body)["data"]:
            DataFly.objects.create(
                fecha_i=item["fecha_i"],
                vlo_i=item["vlo_i"],
                ori_i=item["ori_i"],
                des_i=item["des_i"],
                emp_i=item["emp_i"],
                fecha_o=item["fecha_o"],
                vlo_o=item["vlo_o"], 
                ori_o=item["ori_o"],
                des_o=item["des_o"],
                emp_o=item["emp_o"],
                day_month=item["day_month"],
                month_fly=item["month_fly"],
                year_fly=item["year_fly"],
                day_fly=item["day_fly"],
                type_fly=item["type_fly"],
                enterprice=item["enterprice"],
                siglaori=item["siglaori"],
                siglades=item["siglades"])
                
        return JsonResponse({'response': 'Data loaded'})
