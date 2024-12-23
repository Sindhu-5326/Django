from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.
def exams_view(request):
    return HttpResponse('<h1>Exams Views</h1>')
def attendence_view(request):
    return HttpResponse('<h1>Attendence Views</h1>')
def fees_view(request):
    return HttpResponse('<h1>Fee Views</h1>')
