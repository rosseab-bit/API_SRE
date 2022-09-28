from django.shortcuts import render
import json
from django.http import JsonResponse
import requests
# Create your views here.

def getData(requests):
    data = {'a':1, 'b':2, 'c':3}
    return JsonResponse(data)