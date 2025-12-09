#user A
from django.shortcuts import render, HttpResponse

def test(request):
    return HttpResponse("This is a test response.")

def aweb(request):
    return HttpResponse("This is the aweb response.finish!")
