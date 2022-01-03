from django.db import models
from cloudinary.models import CloudinaryField

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