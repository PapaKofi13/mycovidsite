from django.shortcuts import render
from django.http import HttpResponse
from django.template.response import TemplateResponse
from django.views.generic import ListView
import requests
import json




def index(request):
    getApi = requests.get('http://corona.lmao.ninja/v2/countries/ghana')
    
    getApi_toJson = getApi.json()
    context = {
        'context': getApi_toJson
    }
    
    
    return render(request, 'covidupdates/covidupdates.html',context)

