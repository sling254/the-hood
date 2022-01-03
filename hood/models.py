from django.db import models
from cloudinary.models import CloudinaryField
from django.contrib.auth.models import User
from django.db.models.signals import post_save
from django.dispatch import receiver
import datetime as dt
from django.db.models.deletion import CASCADE
from django.core.validators import MaxValueValidator, MinValueValidator

# Create your models here.


class Business(models.Model):
  name =models.CharField(max_length=60)
  description = models.TextField()
  image = CloudinaryField('image')
  created_at = models.DateTimeField(auto_now_add=True)
  updated_at = models.DateTimeField(auto_now=True)
  #neighborhood = models.ForeignKey(NeighborHood,on_delete=CASCADE,related_name='business')
  #user = models.ForeignKey(User,on_delete=CASCADE)
  email = models.EmailField()

  def create_business(self):
    self.save()

  def delete_business(self):
    self.delete()

  @classmethod
  def search_businesses(cls, business):
    return cls.objects.filter(name__icontains=business).all()

  def __str__(self):
    return self.name



class UserProfile(models.Model):
    user = models.OneToOneField(User,primary_key=True,verbose_name='user',related_name='profile', on_delete=models.CASCADE)
    username = models.CharField(max_length=50,blank=True,null=True)
    bio = models.TextField(max_length=500,blank=True,null=True)
    birth_date = models.DateField(blank=True,null=True)
    neighborhood  = models.CharField(max_length=50,blank=True,null=True)
    picture = CloudinaryField('image',default='static/usericon.png',blank=True)
    email = models.EmailField(max_length=50,blank=True,null=True)

    def __str__(self):
        return f"{self.user.username}'s Profile"

    
@receiver(post_save, sender=User)
def create_user_profile(sender, instance, created, **kwargs):
    if created:
        UserProfile.objects.create(user=instance)


@receiver(post_save, sender=User)
def save_user_profile(sender, instance, **kwargs):
    instance.profile.save()
