from django.shortcuts import render
from django.http import HttpResponse, JsonResponse
from pprint import pprint
from .models import polls



def index(request):
    return HttpResponse("Hello, world. You're at the polls index.")

def get_polls(request):
    data = list(polls.objects.values())
    return JsonResponse({ 'data': data })