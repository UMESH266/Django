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

# Fetching created object using id
article_obj = Articles.objects.get(id=2)

def home_view(request):
    """
    Take in request (Django sends request) and
    Return HTML as a response (we pick to return the response)
    """
    HTML_STRING = f"""
    <h1>{article_obj.title}</h1>
    <p>{article_obj.content}</p>
    """
    return HttpResponse(HTML_STRING)
