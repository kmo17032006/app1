from xmlrpc.client import Fault
from django.http import HttpResponse
from django.shortcuts import render
# from django.template import context

from goods.models import Categories

def index(request):

    categories = Categories.objects.all()

    context = {
        'title': 'Home - Главная',
        'content': 'Магазин мебели HOME',
        'copyright': 'KOA3103',
        'categories': categories,
        }
    return render(request, 'main/index.html', context=context)

def about(request):
    context = {
        'title': 'Home - About page',
        'content': 'About page',
        'text_on_page': 'About page, About page, About page',
        'copyright': 'KOA3103'
        }
    return render(request, 'main/about.html', context=context)

def contact_info(request):
    context = {
        'title': 'Контакты',
        'content': 'Как с нами связаться',
        'text_on_page_1': 'Email: kmo17032006@gmail.com',
        'text_on_page_2': 'Telegram: @buypepe',
        'copyright': 'KOA3103'
        }
    return render(request, 'main/contact_info.html', context=context)