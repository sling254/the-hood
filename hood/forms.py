from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from django.forms import fields
from .models import Post

class CreatePostForm(forms.ModelForm):
  class Meta:
    model = Post
    fields = ('title','post','image')

