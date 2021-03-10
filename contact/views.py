from django.shortcuts import render


# Create your views here.

def contact(request):
    """A view to return menu page"""
 
    return render(request, 'contact.html')