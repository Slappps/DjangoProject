from django.shortcuts import render
from django.shortcuts import HttpResponse
# Create your views here.


def mainPage(request):
    return HttpResponse("DJANGO BASE PAGE")