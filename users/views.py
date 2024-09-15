from http.client import HTTPResponse

from django.shortcuts import render

# Create your views here.

def render_index(request) -> HTTPResponse:
    return render(request, 'index.html')
