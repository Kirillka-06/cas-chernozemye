from django.urls import path

from . import views


app_name = 'seeds'

urlpatterns = [
    path('', views.index, name='index'),
    path('seeds/', views.seeds, name='seeds'),
    path('seeds/<slug:type>/<slug:name>/', views.seed_name, name='seed'),
]