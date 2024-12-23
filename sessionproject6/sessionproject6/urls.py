from django.contrib import admin
from django.urls import path
from testapp import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('name/', views.name_view),
    path('age/', views.age_view),
    path('gf/', views.gf_view),
    path('results/', views.results_view),
]
