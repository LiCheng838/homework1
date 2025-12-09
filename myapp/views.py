#user A
#user B
from django.shortcuts import render, HttpResponse

def test(request):
    return HttpResponse("This is a test response.")

def aweb(request):
    return HttpResponse("This is the aweb response.finish!")
def bweb(request):
    return HttpResponse("Hello, this is a bweb response.")
