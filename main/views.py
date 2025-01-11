from xmlrpc.client import Fault
from django.http import HttpResponse
from django.shortcuts import render
from django.template import context

def index(request):
    context = {
        'title': 'Home - Главная',
        'content': 'Магазин мебели HOME',
        
        }
    return render(request, 'main/index.html', context=context)

def about(request):
    context = {
        'title': 'Home - About page',
        'content': 'About page',
        'text_on_page': 'About page, About page, About page',        
        }
    return render(request, 'main/about.html', context=context)