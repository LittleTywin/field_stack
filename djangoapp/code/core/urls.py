from django.urls import path
from django.views.decorators.csrf import csrf_exempt

from . import views

app_name = 'core'

urlpatterns = [
    path('', views.index, name='index'),
    path('api/', csrf_exempt(views.api), name='api'),
    path('visual/', views.visual, name='visual' ),
    path('live/', views.live, name='live'),
]