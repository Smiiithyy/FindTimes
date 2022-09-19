from datetime import datetime
from pickle import TRUE
from django.db import models
import cloudinary
from cloudinary.models import CloudinaryField

# Create your models here.


    
    


class Bar(models.Model):
    bar_name = models.CharField(max_length=100)
    photo_url = models.TextField()
    address = models.CharField(max_length=200)
    city = models.CharField(max_length=100)
    state = models.CharField(max_length=20)
    
    def __str__(self):
        return self.bar_name

class Comment(models.Model):
    bar = models.ForeignKey(Bar, on_delete=models.CASCADE, related_name='comment')
    name = models.CharField(max_length=50)
    comment = models.TextField()
    # image = models.ImageField(upload_to='images/', blank=True)
    image = CloudinaryField('image', blank = TRUE)
    
    def __str__(self):
        return self.comment
    
class Games(models.Model):
    bar = models.ForeignKey(Bar, on_delete=models.CASCADE, related_name='game')
    sport = models.CharField(max_length=100)
    gametime = models.TextField()
    teamOne = models.TextField(default="")
    teamTwo = models.TextField(default="")
    timeofpost = models.DateTimeField(default=datetime.now())
    showing = [('Y','Yes'),('N','No')]
    
    
    def __str__(self):
        return self.sport