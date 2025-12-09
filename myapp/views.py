from django.shortcuts import render, HttpResponse

def test(request):
    return HttpResponse("This is a test response")
