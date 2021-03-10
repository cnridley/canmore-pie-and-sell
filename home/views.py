from django.shortcuts import render
from .models import Gallery

# Create your views here.

def index(request):
    """A view to return index page"""
    gallery = Gallery.objects.all()
    context = {
        'gallery': gallery,
    }
    return render(request, 'index.html', context)