from xmlrpc.client import Fault
from django.http import HttpResponse
from django.shortcuts import render
from django.template import context

def index(request):
    context = {
        'title': 'Home',
        'content': 'Main page of shop - Home',
        'list': ['first', '2', 3],
        'dict': {'first': 1, 'second': 2},
        'bool': True
        }
    return render(request, 'main/index.html', context=context)

def about(request):
    return HttpResponse('About page')