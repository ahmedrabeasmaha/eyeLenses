from django.urls import path
from . import views

urlpatterns = [
    path('', views.logen, name='login'),
    path('logout/', views.logoout, name='logout'),
    path('relSearch/', views.relSearch, name='realSearch'),
    path('storeadd/', views.storeAdd, name='storeadd'),
    path('storeshow/', views.storeShow, name='storeshow'),
    path('editstore/<slug:id>', views.storeEdit, name='editstore'),
    path('storesearch/', views.storeSearch, name='storesearch'),
    path('add/', views.add, name='add'),
    path('all/', views.all, name='all'),
    path('edit/<slug:id>', views.edit, name='edit'),
    path('del/', views.dliverd, name='del'),
    path('allz/', views.alll, name='alll'),
]
