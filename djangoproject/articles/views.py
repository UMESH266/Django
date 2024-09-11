from multiprocessing import context
from django.shortcuts import render
from .models import Articles
from django.contrib.auth.decorators import login_required
# Create your views here.

def article_search_view(request):
    query_dict = request.GET # This is a dicitonary
    try:
        query = int(query_dict.get('q'))
    except:
        query = None
    article_obj = None
    if query is not None:
        article_obj = Articles.objects.get(id=query)
    context = {
        "object": article_obj
    }
    return render(request, "articles/search.html", context=context)

@login_required
def article_create_view(request):
    context = {}
    if request.method =="POST":
        article_title =  request.POST.get('title')
        content =  request.POST.get('content')
        article_obj = Articles.objects.create(title=article_title, content=content)
        context['object'] = article_obj
        context['created'] = True
    return render(request, "articles/create.html", context=context)

def article_detail_view(request, id=None):
    article_obj = None
    if id is not None:
        article_obj = Articles.objects.get(id=id)
    context = {
        "object": article_obj
    }

    return render(request, "articles/detail.html", context=context)