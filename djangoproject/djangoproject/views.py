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

HTML_STRING = """
<h1> Hello world! </h1>
"""

def home_view(request):
    """
    Take in request (Django sends request) and
    Return HTML as a response (we pick to return the response)
    """
    return HttpResponse(HTML_STRING)