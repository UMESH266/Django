from errno import EXDEV
from multiprocessing import context
from django.shortcuts import redirect, render
from .models import Articles
from django.contrib.auth.decorators import login_required
from articles.forms import ArticleForm
from django.http import Http404
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
    # Method - 1:
    # form = ArticleForm()
    # context = {
    #     "form": form
    # }
    # if request.method =="POST":
    #     form = ArticleForm(request.POST)
    #     context["form"] = form
    #     if form.is_valid():
    #         article_title =  form.cleaned_data.get('title')
    #         content =  form.cleaned_data.get('content')
    #         article_obj = Articles.objects.create(title=article_title, content=content)
    #         context['object'] = article_obj
    #         context['created'] = True
    # return render(request, "articles/create.html", context=context)

    # Method - 2
    form = ArticleForm(request.POST or None)
    context = {
        "form": form
    }
    if form.is_valid():
        # Method - 2
        article_obj = form.save()
        context["form"] = ArticleForm()
        # Method-1
        # title =  form.cleaned_data.get('title')
        # content =  form.cleaned_data.get('content')
        # article_obj = Articles.objects.create(title=title, content=content)
        # context['object'] = article_obj
        # context['created'] = True
        # return redirect("article-detail", slug=article_obj.slug)
        return redirect(article_obj.get_absolute_url())
    
    return render(request, "articles/create.html", context=context)

def article_detail_view(request, slug=None):
    article_obj = None
    if slug is not None:
        try:
            article_obj = Articles.objects.get(slug=slug)
        except Articles.DoesNotExist:
            raise Http404
        except Articles.MultipleObjectsReturned:
            article_obj = Articles.objects.filter(slug=slug).first()
        except:
            raise Http404
    context = {
        "object": article_obj
    }

    return render(request, "articles/detail.html", context=context)