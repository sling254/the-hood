from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from django.forms import fields
from .models import Post

class CreatePostForm(forms.ModelForm):
  title = forms.CharField(
    label='',
    widget=forms.TextInput(attrs={
      'placeholder': 'Title'
      }))
  post = forms.CharField(
    label='',
    widget=forms.Textarea(attrs={
      'placeholder': 'Say something...',
      'rows': '4',
      'class': 'form-control mt-2',
      }))
  
  class Meta:
    model = Post
    fields = ('title','post','image')

