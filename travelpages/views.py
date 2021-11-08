from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.
def indexPageview(request) :
    return HttpResponse('I am hungry!')

def aboutPageView(request) :
    return HttpResponse('I am the about page')