from django.shortcuts import render
from django.http import HttpResponse
from .models import UserDetails
from django.template.response import TemplateResponse
from django.views.generic import ListView


# Create your views here.

def index(request):
    context = {
        'userdetails': UserDetails.objects.all().order_by('-date_posted')
    }
    return render(request,'users/userdetails.html',context)


class UserDetailsListView(ListView):
    model = UserDetails
    template_name = 'users/userdetails.html'
    context_object_name = 'userdetails' 
    ordering = '-date_posted'


class SearchUserDetailsView(ListView):
    model = UserDetails
    template_name = 'users/userdetails.html'

    def get_queryset(self):  # new
        return UserDetails.objects.filter(first_name__icontains='mikey')
