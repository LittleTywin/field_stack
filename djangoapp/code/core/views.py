from django.shortcuts import render

from django.http import HttpResponse, Http404
from core.models import ButtonSample, DataPoint

def index(request):
    if request.method == 'GET':
        return HttpResponse("U GOT ME")
    elif request.method == 'POST':
        state = bool(int(request.POST.get('state')))
        sample = ButtonSample()
        sample.value = state
        sample.save()
        return HttpResponse("U POSTED ME")

def api(request):
    if request.method == 'GET':
        print('OK')
        raise Http404
    elif request.method == 'POST': 
        print('got post request')
        datapoint = DataPoint()
        datapoint.populate(request.POST)
        datapoint.save()
        return HttpResponse(status=204)
    else :
        return Http404