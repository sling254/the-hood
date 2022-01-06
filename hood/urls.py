from django.urls import path
from . views import IndexView, ProfileView,ProfileEditView,OnboardingView,BusinessSearch, create_post

urlpatterns = [
    path('',OnboardingView,name='onboarding'),    
    path('home',IndexView,name='index'),
    path('profile/<int:pk>/', ProfileView.as_view(), name='profile'),
    path('profile/edit/<int:pk>/', ProfileEditView.as_view(), name='profile-edit'),    
    path('business/search/', BusinessSearch.as_view(),  name='business-search'),
    path('create_post/',create_post,name='create_post'),
]
