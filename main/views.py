from django.shortcuts import render 
from django.http import HttpResponse

# Create your views here.

def home_page(request):
    content = {
        'content': 'Домашняя страница',
        'title': 'Хз что-то',
        'list': ['das', 'das'],
        'dict': {'lol': 3},
        'bool': False
    }
    return render(request, "main/index.html", content)

def about(request):
    return HttpResponse('About page')