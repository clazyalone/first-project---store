from django.shortcuts import render
from django.http import HttpResponse
from goods.models import Categories
# Create your views here.


def home_page(request):

    content = {
        'title': 'Home - Главная',
        'content': 'Магазин Мебели HOME',
    }
    return render(request, "main/index.html", content)


def about(request):
    content = {
        'title': 'О нас',
        'content': 'О нас',
        'text': 'Информация о том почему наш магазин такой классный'
    }
    return render(request, "main/about.html", content)
