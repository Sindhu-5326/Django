from django.shortcuts import render

# Create your views here.
def result_view(request):
    return render(request,'testapp/results.html')
