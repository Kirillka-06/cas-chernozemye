from django.urls import path, include

from . import views


app_name = 'seeds'

urlpatterns = [
    path('', views.index, name='index'),
    path('seeds/<slug:type>/<slug:variety>/', views.seed_variety, name='seed'),
]