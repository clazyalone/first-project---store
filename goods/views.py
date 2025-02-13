from django.shortcuts import render
from django.core.paginator import Paginator
from goods.models import Products, Categories
from goods import utils
# Create your views here.


def catalog(request, category_slug=None):

    page = request.GET.get('page', 1)
    on_sale = request.GET.get('on_sale', None)
    order_by = request.GET.get('order_by', None)
    q_search = request.GET.get('q', None)
    print(category_slug)
    print(q_search)
    print(request)
    print(category_slug)

    if category_slug == 'all':
        goods = Products.objects.all()
        print(goods)
    elif q_search != None:
        goods = utils.q_search(q_search)

    else:
        goods = Products.objects.filter(category__slug=category_slug)

    if on_sale:
        goods = goods.filter(discount__gt=0)

    if order_by and order_by != 'default':
        goods = goods.order_by(order_by)

    paginator = Paginator(goods, 3)
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
