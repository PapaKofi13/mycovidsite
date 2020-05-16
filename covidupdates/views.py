from django.shortcuts import render
from django.http import HttpResponse
from django.template.response import TemplateResponse
from django.views.generic import ListView
import requests
import json




def index(request):
    getApi = requests.get('https://corona.lmao.ninja/v2/all')
    data = getApi.json()

    return render(request, 'covidupdates/covidupdates.html',
    	{
    	'cases': data['cases'] ,
    	'active': data['active'],
    	'deaths': data['deaths'],
    	'todayCases': data['todayCases'],
    	'recovered': data['recovered'],	
    	'critical': data['critical']
    	})  
