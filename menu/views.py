from django.shortcuts import render
from .models import Menu

# Create your views here.

def menu(request):
    """A view to return menu page"""
    pie = Menu.objects.all()
    context = {
        'pie': pie,
    }

    return render(request, 'menu.html', context)