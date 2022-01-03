from django.http.response import HttpResponse
from django.shortcuts import render

from hood.models import Business

# Create your views here.


def IndexView(request):
    Businesses = Business.objects.all()
    
    context={
        'Businesses': Businesses,
        
    }
    
    return render(request, 'index.html',context)