from django.shortcuts import render
import json
from django.forms.models import model_to_dict

from django.http import HttpResponse, Http404, JsonResponse
from core.models import DataPoint, SensorStation

def index(request):
    return render(request, 'core/index.html')

def api(request):
    if request.method == 'GET':
        print('OK')
        raise Http404
    elif request.method == 'POST': 
        print('got post request')
        if not SensorStation.objects.filter(id=request.POST['stationid']).exists():
            newstation = SensorStation(id=request.POST['stationid'])
            newstation.save()
        datapoint = DataPoint()
        datapoint.populate(request.POST)
        datapoint.save()
        return HttpResponse(status=204)
    else :
        return Http404

def visual(request):

    is_ajax = request.META.get('HTTP_X_REQUESTED_WITH') == 'XMLHttpRequest'
    if is_ajax and request.method == 'POST':
        print('ajax data:')
        print(request.POST)
        data = list(DataPoint.objects.order_by('-id')[:10].values())
        #print(data)
        return JsonResponse({'data':data})
    data = {'stations':list(SensorStation.objects.all().values())}
    print(data)
    
    return render(request,'core/visual.html',data)

def live(request):
    is_ajax = request.META.get('HTTP_X_REQUESTED_WITH') == 'XMLHttpRequest'
    if is_ajax and request.method == 'GET':
        data = model_to_dict(DataPoint.objects.order_by('-timestamp').first())
        #print(data)
        return JsonResponse(data)
    return render(request,'core/live.html')