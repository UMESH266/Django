"""
* To render html web pages

* As per Django Documentation, A view function is a Python function that takes a Web request and returns a Web response. 
This response can be the HTML contents of a Web page, a redirect, a 404 error, an XML document, an image, or anything 
that a web browser can display.

Django views are part of the user interface — they usually render the HTML/CSS/Javascript in your Template files into what
you see in your browser when you render a web page.
"""

# Required libraries
from django.http import HttpResponse
import random
from django.template.loader import render_to_string

# Method 1: view creation
# HTML_STRING = """
# <h1> Hello world! </h1>
# """

# def home_view(request):
#     """
#     Take in request (Django sends request) and
#     Return HTML as a response (we pick to return the response)
#     """
#     return HttpResponse(HTML_STRING)

# Method 2: Dynamic view 
# def dynamic_view(request):
#     """
#     Takes variable input in the request.
#     """
#     name = "Umesh"
#     num = random.randint(10, 1000)
#     html_str = f"""
#     <h1>Hello, {name} - {num}!</h1>
#     """

#     html_para = f"""
#     <p>Hello, {name} - {num}!</p>
#     """
#     html = html_str + html_para
#     return HttpResponse(html)

# Method 3: using class object 
from articles.models import Articles

def home_view(request):
    """
    Take in request (Django sends request) and
    Return HTML as a response (we pick to return the response)
    """
    # Fetching data from database
    random_id = random.randint(1, 3)
    article_obj = Articles.objects.get(id=random_id)

    # Django templates
    # Method - 1:
    # HTML_STRING = f"""
    # <h1>{article_obj.title} (id: {article_obj.id})</h1>
    # <p>{article_obj.content}</p>
    # """

    # Method - 2: Using context dictionary and format
    # context = {
    #     "id": article_obj.id,
    #     "title": article_obj.title,
    #     "content": article_obj.content
    # }

    # HTML_STRING = """
    # <h1>{title} (id: {id})</h1>
    # <p>{content}</p>
    # """.format(**context)

    # Method - 3: Reading content from template file having html files and rendering to stirng
    context = {
        "id": article_obj.id,
        "title": article_obj.title,
        "content": article_obj.content
    }
    HTML_STRING = render_to_string("home-view.html", context=context)

    return HttpResponse(HTML_STRING)
