from django.shortcuts import render
from django.db.models import Q
from django.shortcuts import render, redirect
from django.urls import reverse_lazy
from django.views import View
from .models import UserProfile


# Create your views here.


def IndexView(request):
    
    context={
    }
    
    return render(request, 'index.html',context)



class ProfileView(View):
    def get(self, request, pk, *args, **kwargs):
        profile = UserProfile.objects.get(pk=pk)
        user = profile.user
        
        context = {
            'user': user,
            'profile': profile,
        }

        return render(request, 'profile.html', context)



