from django.db.models import Q
from goods.models import Products, Categories
from django.contrib.postgres.search import SearchVector, SearchQuery, SearchRank


def q_search(search):
    if search.isdigit() and len(search) <= 5:
        return Products.objects.filter(id=int(search))

    vector = SearchVector("name", "description")
    query = SearchQuery(search)
    return Products.objects.annotate(rank=SearchRank(vector, query)).order_by("-rank")

    # keywords = [word for word in search.split() if len(word) > 2]
    # q_objects = Q()
    # for token in keywords:
    #     q_objects |= Q(description__icontains=token)
    #     q_objects |= Q(name__icontains=token)
    # return Products.objects.filter(q_objects)
