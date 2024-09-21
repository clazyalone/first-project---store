from django.shortcuts import render
from django.core.paginator import Paginator
from goods.models import Products, Categories
# Create your views here.


def catalog(request, category_slug):

    page = request.GET.get('page', 1)
    print(page)

    if category_slug == 'all':
        goods = Products.objects.all()
    else:
        goods = Products.objects.filter(category__slug=category_slug)

    paginator = Paginator(goods, 3)
    print(category_slug)
    current_page = paginator.page(int(page))
    context = {
        "title": "Home - Каталог",
        "goods": current_page,
        "category_slug": category_slug
    }
    return render(request, "goods/catalog.html", context=context)


def product(request, product_slug):
    product = Products.objects.get(slug=product_slug)

    print(product)
    context = {
        "product": product
    }
    return render(request, "goods/product.html", context=context)
