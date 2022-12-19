from django.shortcuts import render, HttpResponse

def index(request):
    return HttpResponse('Welcome')

def create(request):
    return HttpResponse('Create')

def read(request):
    return HttpResponse('Read')