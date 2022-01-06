from django.contrib.auth.models import User
from django.shortcuts import render
from django.db.models import Q
from django.shortcuts import render, redirect
from django.urls import reverse_lazy
from django.views import View
from .models import UserProfile, Business, NeighborHood, Post
from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin
from django.contrib.auth.decorators import login_required
from django.views.generic import ListView, UpdateView, CreateView, DeleteView
from .forms import CreatePostForm


# Create your views here.


def IndexView(request):
    Businesses = Business.objects.all()
    Posts = Post.objects.all()
    
    context={
        "Businesses": Businesses,
        "Posts": Posts
    }
    
    return render(request, 'index.html',context)
@login_required
def OnboardingView(request):

    return render(request, 'onboarding.html')

class ProfileView(View):
    def get(self, request, pk, *args, **kwargs):
        profile = UserProfile.objects.get(pk=pk)
        user = profile.user
        
        context = {
            'user': user,
            'profile': profile,
        }

        return render(request, 'profile.html', context)

class ProfileEditView(LoginRequiredMixin, UserPassesTestMixin,UpdateView):
    model = UserProfile
    fields = ['neighborhood','email', 'bio', 'birth_date','picture']
    template_name = 'profile_edit.html'

    def get_success_url(self):
        pk = self.kwargs['pk']
        return reverse_lazy('profile', kwargs={'pk': pk})
        

    def test_func(self):
        profile = self.get_object()
        if self.request.user == profile.user:
            return True
        return False

def create_post(request):
  if request.method == 'POST':
    add_post_form = CreatePostForm(request.POST,request.FILES)
    if add_post_form.is_valid():
      post = add_post_form.save(commit=False)
      post.user = request.user
      post.save()
      return redirect('index')
  else:
    add_post_form = CreatePostForm()
  return render(request, 'create_post.html', {'add_post_form': add_post_form})


class BusinessSearch(View):
    def get(self, request, *args, **kwargs):
        query = self.request.GET.get('query')
        business_list = Business.search_businesses(query)

        context = {
            'business_list': business_list,
        }

        return render(request, 'search.html', context)
        