from django.http import HttpResponse, Http404, JsonResponse
from django.shortcuts import render, get_object_or_404, redirect
from django.views.decorators.http import require_POST
from .models import Note
from .forms import NoteForm

def home(request):
    return HttpResponse("Welcome Home!")


def api_notes(request):
    data = list(Note.objects.all())
    return JsonResponse( {'notes': data})
