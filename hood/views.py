from django.http.response import HttpResponse
from django.shortcuts import render


# Create your views here.


def IndexView(request):
    
    context={
    }
    
    return render(request, 'index.html',context)



class ProfileView(View):
    def get(self, request, pk, *args, **kwargs):
        profile = UserProfile.objects.get(pk=pk)
        projects = Project.objects.filter(user=profile.user).all()
        user = profile.user
        
        context = {
            'user': user,
            'profile': profile,
        }

        return render(request, 'profile.html', context)



