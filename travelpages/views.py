from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.
def indexPageview(request) :
    return render(request, 'travelpages/index.html')

def aboutPageView(request) :
    return HttpResponse('I am the about page')