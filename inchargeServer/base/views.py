from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.


def home(request) -> 'HttpResponse':
    return HttpResponse("Home")


def telemetry(request) -> 'HttpResponse':
    return HttpResponse("Telemetry")
