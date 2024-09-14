from django.urls import path
from articles.views import  (article_search_view, article_create_view, article_detail_view)

app_name = 'articles'
urlpatterns = [
    path('', article_search_view, name='search'),
    path('create/', article_create_view, name='create'), # Order of operations is important
    # path('articles/<int:id>/', article_detail_view), Using ID 
    path('<slug:slug>/', article_detail_view, name="detail"), # using slug field
    
]
