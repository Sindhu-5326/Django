from django.shortcuts import render
import datetime
from django.http import HttpResponse

# Create your views here.
def time_info(request):
    date=datetime.datetime.now()
    msg='<h1>Hello Friends Good Evening!!!!!</h1><hr>'
    msg+='<h2>Now The Service Time Is: '+str(date)+'</h2>'
    return HttpResponse(msg)