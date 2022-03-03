from django.urls import path
from django.views.decorators.csrf import csrf_exempt

from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('api/', csrf_exempt(views.api), name='api'),
    path('visual/', views.visual, name='visual' ),
]