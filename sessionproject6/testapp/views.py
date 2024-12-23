from django.shortcuts import render
from testapp.forms import NameForm, AgeForm, GfForm

def name_view(request):
    form = NameForm()
    return render(request, 'testapp/name.html', {'form': form})

def age_view(request):
    name = request.GET['name']
    request.session['name'] = name
    form = AgeForm()
    return render(request, 'testapp/age.html', {'form': form, 'name': name})

def gf_view(request):
    gf = request.GET.get('gf')
    request.session['gf'] = gf
    name = request.session.get('name', 'Default Name')
    age = request.session.get('age', 'Unknown Age')
    form = GfForm()
    return render(request, 'testapp/gf.html', {'form': form, 'name': name})

def results_view(request):
    name = request.session.get('name', 'Default Name')
    age = request.session.get('age', 'Unknown Age')
    gf = request.session.get('gf', 'No GF provided')
    return render(request, 'testapp/results.html', {'name': name, 'age': age, 'gf': gf})
