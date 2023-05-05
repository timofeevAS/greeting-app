from django.shortcuts import render

from django.http import HttpResponse


def index(request):
    name = request.GET.get('name', None)
    message = request.GET.get('message', None)

    if name is None:
        name = 'Deppra'
    if message is None:
        message = 'Let\'s go be friends!'

    return render(request, 'index.html', {'name': name, 'message': message})