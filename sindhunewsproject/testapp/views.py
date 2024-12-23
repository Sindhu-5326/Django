from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.
def news_info(request):
    return render(request, 'testapp/index.html')

def movies_view(request):
    head_msg = 'Movies Information'
    sub_msg1 = 'Kalki will release tomorrow'
    sub_msg2 = 'Planning for Aashiqui 3 with Mahesh sir and Sunny Leone'
    sub_msg3 = "Don't go for movies.... Practice Django"
    my_dict = {'head_msg': head_msg, 'sub_msg1': sub_msg1, 'sub_msg2': sub_msg2, 'sub_msg3': sub_msg3, 'type': 'movies'}
    return render(request, 'testapp/news.html', my_dict)

def sports_view(request):
    head_msg = 'Sports Information'
    sub_msg1 = 'Present world Cup is going on'
    sub_msg2 = 'Tomorrow match will be India vs England'
    sub_msg3 = 'India will win world cup'
    my_dict = {'head_msg': head_msg, 'sub_msg1': sub_msg1, 'sub_msg2': sub_msg2, 'sub_msg3': sub_msg3, 'type': 'sports'}
    return render(request, 'testapp/news.html', my_dict)
def politics_view(request):
    my_dict = {
        'head_msg': 'Politics Informatione',
        'sub_msg1': 'India PM is Modiji',
        'sub_msg2': 'AP CM is NCBN',
        'sub_msg3': 'AP Deputy CM is Pawan Klyan',
        'type': 'politics'  
    }
    return render(request, 'testapp/news.html', my_dict)
