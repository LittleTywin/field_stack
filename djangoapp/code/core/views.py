from django.shortcuts import render

from django.http import HttpResponse
from core.models import ButtonSample

def index(request):
    if request.method == 'GET':
        return HttpResponse("U GOT ME")
    elif request.method == 'POST':
        state = bool(int(request.POST.get('state')))
        sample = ButtonSample()
        sample.value = state
        sample.save()
        return HttpResponse("U POSTED ME")