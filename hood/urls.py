from django.urls import path
from . views import IndexView, ProfileView,ProfileEditView,OnboardingView

urlpatterns = [
    path('',IndexView,name='index'),
    path('onboarding',OnboardingView,name='onboarding'),
    path('profile/<int:pk>/', ProfileView.as_view(), name='profile'),
    path('profile/edit/<int:pk>/', ProfileEditView.as_view(), name='profile-edit'),
]
