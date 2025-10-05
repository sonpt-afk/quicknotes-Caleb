
from django.contrib import admin
from django.urls import path, include
from quicknotes import views_site

urlpatterns = [
    path('', views_site.notes, name='notes'),
    path('<int:note_id>/', views_site.note, name='note'),
    path('<int:note_id>/edit/', views_site.edit, name='edit'),
    path('<int:note_id>/delete/', views_site.delete, name='delete'),
    path('add/', views_site.add, name='add'),
]
