from django.http import HttpResponse
from django.shortcuts import render

html = """
<h2>Welcome to HyperJob!</h2>
<div><a href="/login">login</a></div>
<div><a href="/signup">signup</a></div>
<div><a href="/vacancies">vacancies</a></div>
<div><a href="/resumes">resumes</a></div>
<div><a href="/home">home</a></div>
"""


def homepage_view(request, *args, **kwargs):
    return HttpResponse(html)


def home_view(request, *args, **kwargs):
    return render(request, "home.html")
