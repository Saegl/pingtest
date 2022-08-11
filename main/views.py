from django.shortcuts import render
from django.http import HttpResponse


def index(req):
    return HttpResponse("Ping test of django in digital ocean")