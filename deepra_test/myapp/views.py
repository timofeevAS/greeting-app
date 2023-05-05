from django.shortcuts import render

from django.http import HttpResponse

def hello(request):
    name = request.GET.get('name')
    message = request.GET.get('message')
    return HttpResponse(f'Hello {name}!\n{message}!')